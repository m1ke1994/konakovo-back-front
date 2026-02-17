<script setup>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

const page = {
  title: "Беговой клуб",
  subtitle:
    "Сообщество регулярных тренировок и маршрутов в живом природном ритме: без давления, с поддержкой и устойчивой динамикой.",
  content: [
    {
      type: "text",
      heading: "Идея клуба",
      value:
        "Беговой клуб в «Новом Конаково» создан для тех, кто хочет двигаться регулярно и бережно. Мы делаем акцент не на рекорды, а на устойчивость: ритм, который можно сохранить надолго.",
    },
    {
      type: "image",
      src: "/images/video-2.jpg",
      alt: "Утренняя тренировка бегового клуба",
    },
    {
      type: "text",
      value:
        "Тренировки проходят в разных форматах: короткие утренние сессии, длинные маршруты по выходным и восстановительные занятия в спокойном темпе.",
    },
    {
      type: "text",
      heading: "Как строится занятие",
      value:
        "Каждая встреча включает разминку, основной блок и мягкое завершение. Это позволяет постепенно повышать выносливость и снижает риск перегруза.",
    },
    {
      type: "video",
      src: "https://www.youtube.com/embed/dQw4w9WgXcQ",
    },
    {
      type: "text",
      value:
        "Маршруты подбираются с учетом уровня группы и погодных условий. Для новых участников всегда есть безопасный вход и вариант нагрузки попроще.",
    },
    {
      type: "image",
      src: "/images/news5.jpg",
      alt: "Маршрут бегового клуба у воды",
    },
    {
      type: "text",
      heading: "Что дает регулярность",
      value:
        "Через несколько недель участники обычно замечают не только физический прогресс, но и более ровное состояние в течение дня: выше концентрация, меньше внутренней суеты.",
    },
    {
      type: "text",
      value:
        "Клуб работает как сообщество: поддержка, обмен опытом и ощущение команды помогают не выпадать из тренировочного ритма даже в насыщенные периоды.",
    },
  ],
};
</script>

<template>
  <AppHeader />

  <main class="content-page">
    <header class="content-page__hero">
      <h1 class="content-page__title">{{ page.title }}</h1>
      <p class="content-page__subtitle">{{ page.subtitle }}</p>
    </header>

    <section class="content-page__body">
      <article v-for="(block, index) in page.content" :key="`running-${index}`" class="content-page__block">
        <template v-if="block.type === 'text'">
          <h2 v-if="block.heading" class="content-page__h2">{{ block.heading }}</h2>
          <p class="content-page__text">{{ block.value }}</p>
        </template>

        <img
          v-else-if="block.type === 'image'"
          class="content-page__image"
          :src="block.src"
          :alt="block.alt || page.title"
          loading="lazy"
          decoding="async"
        />

        <div v-else-if="block.type === 'video'" class="content-page__video-wrap">
          <iframe
            class="content-page__video"
            :src="block.src"
            title="Видео"
            loading="lazy"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
          ></iframe>
        </div>
      </article>
    </section>
  </main>

  <AppFooter />
</template>

<style scoped>
.content-page {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px 72px;
  display: grid;
  gap: 22px;
}

.content-page__hero {
  display: grid;
  gap: 10px;
}

.content-page__title {
  margin: 0;
  font-size: clamp(34px, 6vw, 52px);
  line-height: 1.05;
  color: var(--text-strong);
}

.content-page__subtitle {
  margin: 0;
  color: var(--muted);
  font-size: 16px;
  line-height: 1.6;
}

.content-page__body {
  display: grid;
  gap: 18px;
}

.content-page__block {
  display: grid;
  gap: 10px;
}

.content-page__h2 {
  margin: 0;
  font-size: clamp(22px, 4vw, 30px);
  color: var(--text-strong);
}

.content-page__text {
  margin: 0;
  font-size: 16px;
  line-height: 1.75;
  color: var(--text);
}

.content-page__image {
  width: 100%;
  border-radius: 18px;
  object-fit: cover;
  display: block;
}

.content-page__video-wrap {
  border-radius: 18px;
  overflow: hidden;
}

.content-page__video {
  width: 100%;
  aspect-ratio: 16 / 9;
  border: 0;
  display: block;
}

@media (max-width: 720px) {
  .content-page {
    padding: 0 14px 58px;
  }

  .content-page__text {
    font-size: 15px;
  }
}
</style>
