<template>
  <div class="scenario">
    <div class="scenario__layout">
      <section class="scenario__main">
        <h2 class="scenario__title">Соберите сценарий дня</h2>

        <div class="services">
          <div v-for="service in servicesWithTariffs" :key="service.id" class="service">
            <button class="service__header" @click="toggleService(service.id)">
              <span class="service__name">
                {{ service.title }}
              </span>

              <span class="service__toggle">
                {{ openServiceId === service.id ? "−" : "+" }}
              </span>
            </button>

            <div v-if="openServiceId === service.id" class="service__body">
              <div
                v-for="tariff in service.tariffs"
                :key="tariff.id"
                class="tariff"
                :class="{ active: selectedTariffIds.includes(tariff.id) }"
              >
                <div class="tariff__row">
                  <span class="tariff__title">
                    {{ tariff.title }}
                  </span>

                  <span class="tariff__price">
                    {{ formatPrice(tariff.price) }}
                  </span>

                  <button
                    class="tariff__btn"
                    :class="{ active: selectedTariffIds.includes(tariff.id) }"
                    @click="toggleTariff(tariff.id)"
                  >
                    {{ selectedTariffIds.includes(tariff.id) ? "✓" : "+" }}
                  </button>
                </div>

                <div class="tariff__desc">
                  {{ tariff.description }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <aside class="scenario__aside">
        <div class="panel">
          <input type="text" v-model="name" placeholder="Имя" />

          <input
            type="text"
            v-model="contact"
            placeholder="Email или номер телефона"
          />

          <input type="date" v-model="date" placeholder="Выберите дату" />
          <input
            type="number"
            min="1"
            max="10"
            v-model.number="guests"
            placeholder="Количество гостей"
          />
          <textarea rows="3" v-model="comment" placeholder="Комментарий"></textarea>

          <div class="summary">
            <div class="summary__row">
              <span>Итого</span>
              <strong>{{ formatPrice(total) }}</strong>
            </div>

            <div v-for="t in selectedTariffs" :key="t.tariffId" class="summary__item">
              {{ t.serviceTitle }} — {{ t.title }}
            </div>
          </div>

          <button class="btn-primary" @click="handleConfirm">
            Согласовать
          </button>
        </div>
      </aside>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { formatPrice, loadServices, useServices } from "../composables/useServices";

const { servicesWithTariffs } = useServices();

const selectedTariffIds = ref([]);
const openServiceId = ref(null);
const name = ref("");
const contact = ref("");
const date = ref("");
const guests = ref("");
const comment = ref("");

onMounted(() => {
  loadServices();
});

const toggleService = (id) => {
  openServiceId.value = openServiceId.value === id ? null : id;
};

const toggleTariff = (id) => {
  selectedTariffIds.value = selectedTariffIds.value.includes(id)
    ? selectedTariffIds.value.filter((item) => item !== id)
    : [...selectedTariffIds.value, id];
};

const selectedTariffs = computed(() =>
  servicesWithTariffs.value.flatMap((service) =>
    service.tariffs
      .filter((tariff) => selectedTariffIds.value.includes(tariff.id))
      .map((tariff) => ({
        tariffId: tariff.id,
        title: tariff.title,
        price: tariff.price,
        serviceTitle: service.title,
      }))
  )
);

const total = computed(() => selectedTariffs.value.reduce((sum, tariff) => sum + tariff.price, 0));

const handleConfirm = () => {
  console.log({
    tariffs: selectedTariffs.value,
    total: total.value,
    name: name.value,
    contact: contact.value,
    date: date.value,
    guests: guests.value,
    comment: comment.value,
  });
};
</script>

<style scoped>
.scenario {
  padding: 32px 0;
}

.scenario__layout {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 40px;
}

.scenario__title {
  margin-bottom: 20px;
  font-size: 20px;
}

.service {
  border-bottom: 1px solid var(--border);
}

.service__header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 0;
  border: none;
  background: none;
  cursor: pointer;
  font-weight: 600;
}

.service__name {
  font-size: 15px;
}

.service__toggle {
  font-size: 18px;
}

.service__body {
  padding-bottom: 12px;
}

.tariff {
  padding: 8px 0;
  border-top: 1px solid var(--border);
}

.tariff__row {
  display: grid;
  grid-template-columns: 1fr 90px 36px;
  align-items: center;
  gap: 10px;
}

.tariff__title {
  font-size: 13px;
  font-weight: 600;
}

.tariff__price {
  text-align: right;
  font-size: 13px;
  font-weight: 600;
}

.tariff__btn {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  border: 1px solid var(--border);
  background: transparent;
  cursor: pointer;
}

.tariff__btn.active {
  background: var(--primary);
  border-color: var(--primary);
  color: var(--color-dark-deep);
}

.tariff__desc {
  font-size: 12px;
  color: var(--muted);
  margin-top: 4px;
}

.panel {
  position: sticky;
  top: 90px;
  display: grid;
  gap: 10px;
  padding: 16px;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: var(--card);
}

.panel input,
.panel textarea {
  padding: 8px;
  font-size: 13px;
  border-radius: 6px;
  border: 1px solid var(--border);
  background: var(--bg-elevated);
}

.summary__row {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  margin-bottom: 6px;
}

.summary__item {
  font-size: 12px;
  color: var(--muted);
}

@media (max-width: 980px) {
  .scenario__layout {
    grid-template-columns: 1fr;
  }

  .panel {
    position: static;
  }
}
</style>
