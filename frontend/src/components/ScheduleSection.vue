<template>
  <div class="month-schedule">
    <div class="month-schedule__top">
      <h2>Расписание программ</h2>

      <div class="month-schedule__months" role="tablist" aria-label="Выбор месяца">
        <button
          v-for="month in groupedEvents"
          :key="month.monthKey"
          class="month-schedule__month-tab"
          :class="{ active: activeMonth === month.monthKey }"
          type="button"
          role="tab"
          :aria-selected="activeMonth === month.monthKey"
          @click="setActiveMonth(month.monthKey)"
        >
          {{ month.monthLabel }}
        </button>
      </div>

      <div
        v-if="activeMonthDays.length"
        ref="daysStripRef"
        class="month-schedule__days"
        aria-label="Даты выбранного месяца"
      >
        <button
          v-for="day in activeMonthDays"
          :key="day.dateKey"
          class="month-schedule__day"
          :class="{
            active: activeDay === day.dateKey,
            today: day.dateKey === todayDateKey
          }"
          type="button"
          :ref="(el) => setDayButtonRef(day.dateKey, el)"
          @click="focusDay(day.dateKey)"
        >
          <span class="month-schedule__day-label">{{ day.ribbonWeekday }}</span>
          <span class="month-schedule__day-number">{{ day.ribbonDay }}</span>
        </button>
      </div>

      <div v-if="activeMonthGroup" class="month-schedule__meta">
        <span>{{ activeMonthGroup.days.length }} {{ pluralizeDays(activeMonthGroup.days.length) }}</span>
        <span>•</span>
        <span>{{ activeMonthEventsCount }} {{ pluralizeEvents(activeMonthEventsCount) }}</span>
      </div>
    </div>

    <div class="month-schedule__list">
      <section v-if="activeMonthGroup" :key="activeMonthGroup.monthKey" class="month-schedule__month">
        <h3 class="month-schedule__month-title">{{ activeMonthGroup.monthLabel }}</h3>

        <section
          v-for="dayGroup in visibleMonthDays"
          :key="dayGroup.dateKey"
          class="month-schedule__day-group"
          :class="{ 'month-schedule__day-group--open': isDayOpen(dayGroup.dateKey) }"
        >
          <button
            class="month-schedule__date"
            type="button"
            :aria-expanded="isDayOpen(dayGroup.dateKey)"
            @click="toggleDay(dayGroup.dateKey)"
          >
            <span class="month-schedule__date-main">
              <span>{{ dayGroup.dateLabel }}</span>
              <span class="month-schedule__date-count">{{ dayGroup.events.length }}</span>
            </span>
            <span
              class="month-schedule__date-chevron"
              :class="{ 'month-schedule__date-chevron--open': isDayOpen(dayGroup.dateKey) }"
              aria-hidden="true"
            >
              ▾
            </span>
          </button>

          <div
            class="month-schedule__day-body"
            :class="{ 'month-schedule__day-body--open': isDayOpen(dayGroup.dateKey) }"
          >
            <div class="month-schedule__date-events">
              <div
                v-for="event in dayGroup.events"
                :key="event.id"
                class="program-card"
                @click="openModal(event)"
              >
                <div class="program-card__bar" :style="{ background: event.color }"></div>

                <div class="program-card__content">
                  <div class="program-card__time">
                    {{ event.start }} — {{ event.end }}
                  </div>

                  <div class="program-card__title">
                    {{ event.title }}
                  </div>

                  <div class="program-card__meta">
                    {{ event.category }}
                  </div>
                </div>

                <div class="program-card__price">
                  {{ formatPrice(event.price) }}
                </div>
              </div>
            </div>
          </div>
        </section>

        <button
          v-if="hasMoreDays"
          class="month-schedule__more"
          type="button"
          @click="showMoreDays"
        >
          Показать больше дат
        </button>
      </section>

      <div v-if="!activeMonthGroup" class="month-schedule__empty">
        В расписании пока нет событий
      </div>
    </div>

    <div v-if="activeEvent" class="program-modal" @click.self="activeEvent = null">
      <div class="program-modal__card">
        <button class="program-modal__close" @click="activeEvent = null">✕</button>

        <h3>{{ activeEvent.title }}</h3>

        <p class="program-modal__time">
          {{ activeEvent.start }} — {{ activeEvent.end }}
        </p>

        <img :src="activeEvent.image" class="program-modal__image" />

        <p class="program-modal__desc">
          {{ activeEvent.description }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, nextTick, ref, watch } from "vue";

const pad = (value) => String(value).padStart(2, "0");

const toDateKey = (date) =>
  `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;

const toMonthKey = (date) => `${date.getFullYear()}-${pad(date.getMonth() + 1)}`;

const parseDateKey = (dateKey) => {
  const [year, month, day] = String(dateKey).split("-").map(Number);
  return new Date(year, month - 1, day);
};

const today = new Date();
const todayDateKey = toDateKey(today);
const INITIAL_VISIBLE_DAYS = 5;
const VISIBLE_DAYS_STEP = 5;
const MONTHS_AHEAD = 8;
const MIN_EVENTS_TARGET = 110;

const randomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

const eventTemplates = [
  {
    title: "Чайная церемония",
    category: "Авторская программа",
    price: [2800, 4200],
    image: "/2.jpeg",
    description: "Камерный формат с практикой внимания и спокойным ритмом.",
    color: "#E9B949",
  },
  {
    title: "Экскурсия в Братство Лосей",
    category: "Экскурсия",
    price: [3200, 5400],
    image: "/1.jpeg",
    description: "Маршрут по природной зоне с проводником и остановками в ключевых точках.",
    color: "#6BA368",
  },
  {
    title: "Беговой клуб",
    category: "Спорт",
    price: [1200, 2600],
    image: "/3.jpeg",
    description: "Легкая тренировка с акцентом на технику, темп и восстановление.",
    color: "#C88B3A",
  },
  {
    title: "Мастер-класс по дыханию",
    category: "Мастер-класс",
    price: [1800, 3200],
    image: "/4.jpeg",
    description: "Практика для фокуса, снижения напряжения и восстановления энергии.",
    color: "#7AA2F7",
  },
  {
    title: "Волонтерская программа",
    category: "Сообщество",
    price: [900, 1900],
    image: "/5.jpeg",
    description: "Практические задачи в команде с поддержкой координатора.",
    color: "#A68BFF",
  },
  {
    title: "Вечерний маршрут у воды",
    category: "Экскурсия",
    price: [2400, 3900],
    image: "/6.jpeg",
    description: "Неспешный формат с наблюдением природы и финальной рефлексией.",
    color: "#4FB3BF",
  },
];

const toTimeLabel = (hours, minutes = 0) =>
  `${pad(hours)}:${pad(minutes)}`;

const generateEvents = () => {
  const generated = [];
  let idCounter = 1;
  const eventsByDate = new Map();

  for (let monthOffset = 0; monthOffset < MONTHS_AHEAD; monthOffset += 1) {
    const monthDate = new Date(today.getFullYear(), today.getMonth() + monthOffset, 1);
    const year = monthDate.getFullYear();
    const monthIndex = monthDate.getMonth();
    const daysInMonth = new Date(year, monthIndex + 1, 0).getDate();

    const activeDaysCount = randomInt(8, 15);
    const daySet = new Set();
    while (daySet.size < Math.min(activeDaysCount, daysInMonth)) {
      daySet.add(randomInt(1, daysInMonth));
    }
    const sortedDayNumbers = Array.from(daySet).sort((a, b) => a - b);

    sortedDayNumbers.forEach((dayNumber) => {
      const dayDate = new Date(year, monthIndex, dayNumber);
      const dateKey = toDateKey(dayDate);
      const eventsPerDay = randomInt(1, 3);

      const baseHour = randomInt(8, 15);
      for (let i = 0; i < eventsPerDay; i += 1) {
        const template = eventTemplates[randomInt(0, eventTemplates.length - 1)];
        const startHour = Math.min(baseHour + i * 2, 20);
        const durationMinutes = [60, 90, 120][randomInt(0, 2)];
        const endTotalMinutes = startHour * 60 + durationMinutes;
        const endHour = Math.floor(endTotalMinutes / 60);
        const endMinutes = endTotalMinutes % 60;

        generated.push({
          id: idCounter++,
          date: dateKey,
          title: template.title,
          category: template.category,
          start: toTimeLabel(startHour),
          end: toTimeLabel(endHour, endMinutes),
          price: randomInt(template.price[0], template.price[1]),
          image: template.image,
          description: template.description,
          color: template.color,
        });

        eventsByDate.set(dateKey, (eventsByDate.get(dateKey) || 0) + 1);
      }
    });
  }

  if (generated.length < MIN_EVENTS_TARGET) {
    const sortedDates = Array.from(eventsByDate.keys()).sort((a, b) =>
      parseDateKey(a).getTime() - parseDateKey(b).getTime()
    );

    let dateCursor = 0;
    while (generated.length < MIN_EVENTS_TARGET && sortedDates.length) {
      const dateKey = sortedDates[dateCursor % sortedDates.length];
      const dateLoad = eventsByDate.get(dateKey) || 0;

      if (dateLoad < 3) {
        const template = eventTemplates[randomInt(0, eventTemplates.length - 1)];
        const startHour = 9 + dateLoad * 2;
        const durationMinutes = [60, 90, 120][randomInt(0, 2)];
        const endTotalMinutes = startHour * 60 + durationMinutes;
        const endHour = Math.floor(endTotalMinutes / 60);
        const endMinutes = endTotalMinutes % 60;

        generated.push({
          id: idCounter++,
          date: dateKey,
          title: template.title,
          category: template.category,
          start: toTimeLabel(startHour),
          end: toTimeLabel(endHour, endMinutes),
          price: randomInt(template.price[0], template.price[1]),
          image: template.image,
          description: template.description,
          color: template.color,
        });

        eventsByDate.set(dateKey, dateLoad + 1);
      }

      dateCursor += 1;
    }
  }

  return generated;
};

const events = ref(generateEvents());

const monthFormatter = new Intl.DateTimeFormat("ru-RU", {
  month: "long",
  year: "numeric",
});

const dayFormatter = new Intl.DateTimeFormat("ru-RU", {
  day: "numeric",
  month: "long",
  weekday: "long",
});

const ribbonWeekdayFormatter = new Intl.DateTimeFormat("ru-RU", {
  weekday: "short",
});

const capitalize = (text) => text.charAt(0).toUpperCase() + text.slice(1);

const groupedEvents = computed(() => {
  const sortedEvents = [...events.value].sort((a, b) => {
    const dateDiff = parseDateKey(a.date).getTime() - parseDateKey(b.date).getTime();
    if (dateDiff !== 0) return dateDiff;
    return String(a.start).localeCompare(String(b.start), "ru-RU");
  });

  const monthMap = new Map();

  sortedEvents.forEach((event) => {
    const dateObj = parseDateKey(event.date);
    const monthKey = toMonthKey(dateObj);

    if (!monthMap.has(monthKey)) {
      monthMap.set(monthKey, {
        monthKey,
        monthLabel: capitalize(monthFormatter.format(dateObj)),
        daysMap: new Map(),
      });
    }

    const monthGroup = monthMap.get(monthKey);
    const dateKey = event.date;

    if (!monthGroup.daysMap.has(dateKey)) {
      const weekdayLabel = ribbonWeekdayFormatter.format(dateObj).replace(".", "");

      monthGroup.daysMap.set(dateKey, {
        dateKey,
        dateLabel: capitalize(dayFormatter.format(dateObj)),
        ribbonWeekday: capitalize(weekdayLabel),
        ribbonDay: dateObj.getDate(),
        events: [],
      });
    }

    monthGroup.daysMap.get(dateKey).events.push(event);
  });

  return Array.from(monthMap.values()).map((monthGroup) => ({
    monthKey: monthGroup.monthKey,
    monthLabel: monthGroup.monthLabel,
    days: Array.from(monthGroup.daysMap.values()),
  }));
});

const activeMonth = ref("");
const activeDay = ref("");
const openedDays = ref({});
const visibleDayCount = ref(INITIAL_VISIBLE_DAYS);
const dayButtonRefs = ref({});
const daysStripRef = ref(null);

const activeMonthGroup = computed(
  () => groupedEvents.value.find((month) => month.monthKey === activeMonth.value) || null
);

const activeMonthDays = computed(() => activeMonthGroup.value?.days || []);
const visibleMonthDays = computed(() => activeMonthDays.value.slice(0, visibleDayCount.value));
const hasMoreDays = computed(() => activeMonthDays.value.length > visibleDayCount.value);
const activeMonthEventsCount = computed(() =>
  activeMonthDays.value.reduce((sum, day) => sum + day.events.length, 0)
);

const pluralizeDays = (count) => {
  if (count % 10 === 1 && count % 100 !== 11) return "день";
  if ([2, 3, 4].includes(count % 10) && ![12, 13, 14].includes(count % 100)) return "дня";
  return "дней";
};

const pluralizeEvents = (count) => {
  if (count % 10 === 1 && count % 100 !== 11) return "событие";
  if ([2, 3, 4].includes(count % 10) && ![12, 13, 14].includes(count % 100)) return "события";
  return "событий";
};

const findNearestUpcomingDay = (days) => {
  if (!days.length) return "";

  const todayStart = new Date(today);
  todayStart.setHours(0, 0, 0, 0);

  const nearest = days.find((day) => {
    const dayDate = parseDateKey(day.dateKey);
    dayDate.setHours(0, 0, 0, 0);
    return dayDate.getTime() >= todayStart.getTime();
  });

  return nearest?.dateKey || days[0].dateKey;
};

const setActiveMonth = (monthKey) => {
  if (activeMonth.value === monthKey) return;
  activeMonth.value = monthKey;
};

const setDayButtonRef = (dayKey, el) => {
  if (!el) {
    delete dayButtonRefs.value[dayKey];
    return;
  }
  dayButtonRefs.value[dayKey] = el;
};

const scrollRibbonToActiveDay = (smooth = true) => {
  const container = daysStripRef.value;
  const button = dayButtonRefs.value[activeDay.value];
  if (!container || !button) return;

  const targetLeft = button.offsetLeft - (container.clientWidth - button.clientWidth) / 2;
  container.scrollTo({
    left: Math.max(0, targetLeft),
    behavior: smooth ? "smooth" : "auto",
  });
};

const resetMonthView = async () => {
  const days = activeMonthDays.value;
  const defaultDay = findNearestUpcomingDay(days);
  const defaultDayIndex = days.findIndex((day) => day.dateKey === defaultDay);
  visibleDayCount.value = Math.max(INITIAL_VISIBLE_DAYS, defaultDayIndex + 1);

  activeDay.value = defaultDay;
  openedDays.value = defaultDay ? { [defaultDay]: true } : {};

  await nextTick();
  if (defaultDay) {
    scrollRibbonToActiveDay(false);
  }
};

const isDayOpen = (dayKey) => Boolean(openedDays.value[dayKey]);

const focusDay = async (dayKey) => {
  activeDay.value = dayKey;
  const dayIndex = activeMonthDays.value.findIndex((day) => day.dateKey === dayKey);
  if (dayIndex >= 0 && dayIndex + 1 > visibleDayCount.value) {
    visibleDayCount.value = dayIndex + 1;
  }
  if (!openedDays.value[dayKey]) {
    openedDays.value = { ...openedDays.value, [dayKey]: true };
  }

  await nextTick();
  scrollRibbonToActiveDay(true);
};

const toggleDay = (dayKey) => {
  activeDay.value = dayKey;
  openedDays.value = {
    ...openedDays.value,
    [dayKey]: !openedDays.value[dayKey],
  };
};

const showMoreDays = () => {
  visibleDayCount.value += VISIBLE_DAYS_STEP;
};

watch(
  groupedEvents,
  (months) => {
    if (!months.length) {
      activeMonth.value = "";
      activeDay.value = "";
      openedDays.value = {};
      return;
    }

    const currentMonthKey = toMonthKey(today);
    const hasActiveMonth = months.some((month) => month.monthKey === activeMonth.value);

    if (!hasActiveMonth) {
      activeMonth.value =
        months.find((month) => month.monthKey === currentMonthKey)?.monthKey || months[0].monthKey;
    }
  },
  { immediate: true }
);

watch(
  activeMonth,
  async () => {
    await resetMonthView();
  },
  { immediate: true }
);

const activeEvent = ref(null);

const openModal = (event) => {
  activeEvent.value = event;
};

const formatPrice = (value) => `${Number(value).toLocaleString("ru-RU")} ₽`;
</script>

<style scoped>
.month-schedule {
  padding: 40px 0;
}

.month-schedule__top {
  margin-bottom: 24px;
  display: grid;
  gap: 14px;
}

.month-schedule__months {
  display: flex;
  flex-wrap: nowrap;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 4px;
  -webkit-overflow-scrolling: touch;
}

.month-schedule__month-tab {
  border: 1px solid var(--border);
  background: var(--bg-elevated);
  color: var(--text);
  border-radius: 999px;
  padding: 8px 12px;
  font-size: 13px;
  cursor: pointer;
  white-space: nowrap;
  flex: 0 0 auto;
  transition: transform 120ms ease, background-color 120ms ease, border-color 120ms ease;
}

.month-schedule__month-tab:hover {
  transform: translateY(-1px);
}

.month-schedule__month-tab.active {
  background: var(--primary);
  color: var(--color-dark-deep);
  border-color: var(--primary);
}

.month-schedule__days {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 6px;
  -webkit-overflow-scrolling: touch;
  scroll-snap-type: x proximity;
}

.month-schedule__day {
  min-width: 68px;
  padding: 7px 8px;
  border-radius: 10px;
  border: 1px solid var(--border);
  background: var(--bg-elevated);
  font-size: 11px;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  flex: 0 0 auto;
  scroll-snap-align: center;
  transition: transform 120ms ease, border-color 120ms ease, background-color 120ms ease;
}

.month-schedule__day:hover {
  transform: translateY(-1px);
}

.month-schedule__day.active {
  background: var(--primary);
  color: var(--color-dark-deep);
  border-color: var(--primary);
}

.month-schedule__day.today:not(.active) {
  border-color: color-mix(in srgb, var(--primary) 70%, var(--border));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 30%, transparent);
}

.month-schedule__meta {
  font-size: 12px;
  color: var(--muted);
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.month-schedule__list {
  display: grid;
  gap: 22px;
}

.month-schedule__month {
  display: grid;
  gap: 14px;
}

.month-schedule__month-title {
  margin: 0;
  font-size: 22px;
  line-height: 1.2;
  color: var(--text-strong);
}

.month-schedule__day-group {
  display: grid;
  gap: 8px;
}

.month-schedule__date {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-strong);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: color-mix(in srgb, var(--bg-elevated) 84%, transparent);
  padding: 10px 12px;
  text-align: left;
  cursor: pointer;
  transition: border-color 140ms ease, background-color 140ms ease;
}

.month-schedule__date:hover {
  border-color: color-mix(in srgb, var(--primary) 45%, var(--border));
}

.month-schedule__date-main {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.month-schedule__date-count {
  min-width: 22px;
  height: 22px;
  border-radius: 999px;
  padding: 0 7px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  color: var(--text-strong);
  background: color-mix(in srgb, var(--primary) 22%, var(--bg-elevated));
}

.month-schedule__date-chevron {
  font-size: 14px;
  color: var(--muted);
  transition: transform 180ms ease;
}

.month-schedule__date-chevron--open {
  transform: rotate(180deg);
}

.month-schedule__day-body {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 220ms ease;
}

.month-schedule__day-body--open {
  grid-template-rows: 1fr;
}

.month-schedule__date-events {
  overflow: hidden;
  display: grid;
  gap: 10px;
}

.month-schedule__day-group--open .month-schedule__date-events {
  padding-top: 2px;
}

.month-schedule__more {
  justify-self: center;
  margin-top: 2px;
  border: 1px solid var(--border);
  background: var(--bg-elevated);
  color: var(--text-strong);
  border-radius: 999px;
  padding: 9px 14px;
  font-size: 13px;
  cursor: pointer;
  transition: transform 120ms ease, border-color 120ms ease;
}

.month-schedule__more:hover {
  transform: translateY(-1px);
  border-color: color-mix(in srgb, var(--primary) 50%, var(--border));
}

.month-schedule__empty {
  padding: 14px;
  border-radius: 10px;
  border: 1px dashed var(--border);
  color: var(--muted);
}

.program-card {
  display: grid;
  grid-template-columns: 6px 1fr auto;
  align-items: center;
  gap: 14px;
  padding: 12px 14px;
  border-radius: 10px;
  border: 1px solid var(--border);
  background: var(--card);
  cursor: pointer;
}

.program-card__bar {
  height: 100%;
  border-radius: 4px;
}

.program-card__title {
  font-weight: 600;
  margin: 2px 0;
}

.program-card__meta {
  font-size: 12px;
  color: var(--muted);
}

.program-card__price {
  font-weight: 600;
}

.program-modal {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.program-modal__card {
  width: 420px;
  background: var(--card);
  border-radius: 14px;
  padding: 24px;
  position: relative;
}

.program-modal__close {
  position: absolute;
  right: 16px;
  top: 16px;
  border: none;
  background: none;
  cursor: pointer;
}

.program-modal__image {
  width: 100%;
  border-radius: 10px;
  margin: 12px 0;
}

@media (max-width: 720px) {
  .month-schedule__month-tab {
    white-space: nowrap;
  }

  .month-schedule__day {
    min-width: 64px;
  }

  .program-card {
    grid-template-columns: 6px 1fr;
  }

  .program-card__price {
    grid-column: 2;
    justify-self: start;
  }

  .program-modal__card {
    width: min(420px, 92vw);
  }
}
</style>
