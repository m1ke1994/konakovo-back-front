<script setup>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

const page = {
  title: "Волонтерские программы",
  subtitle:
    "Практические форматы участия в развитии пространства: от разовых выездов до регулярной вовлеченности в проекты.",
  content: [
    {
      type: "text",
      heading: "Зачем мы это делаем",
      value:
        "Волонтерские программы в «Новом Конаково» — это не только помощь территории, но и способ быть частью сообщества, которое создает живое пространство своими руками.",
    },
    {
      type: "text",
      value:
        "Мы строим участие так, чтобы в него было легко войти: понятные задачи, ясная коммуникация, поддержка координаторов и команда рядом на всех этапах.",
    },
    {
      type: "image",
      src: "/images/news3.jpg",
      alt: "Волонтерский день в Новом Конаково",
    },
    {
      type: "text",
      heading: "Как устроен волонтерский день",
      value:
        "Обычно день делится на три части: вводный брифинг, практический блок и общий круг завершения. Такой ритм помогает сохранить энергию и видеть конкретный результат.",
    },
    {
      type: "text",
      value:
        "В зависимости от сезона задачи могут включать подготовку троп, работу с зонами отдыха, помощь в навигации, поддержку событий и организационные процессы.",
    },
    {
      type: "video",
      src: "https://www.youtube.com/embed/ysz5S6PUM-U",
    },
    {
      type: "text",
      heading: "Для кого подходит участие",
      value:
        "Для новичков, кто хочет впервые включиться в общественный проект; для опытных участников, которым важно делать что-то полезное в команде; для локальных жителей и гостей.",
    },
    {
      type: "image",
      src: "/images/news6.jpg",
      alt: "Команда волонтеров на маршруте",
    },
    {
      type: "text",
      value:
        "Участие можно выбрать в удобном режиме: разовый выезд, ежемесячный формат или серия задач на сезон. Мы поддерживаем гибкость, чтобы волонтерство было устойчивой частью жизни, а не перегрузом.",
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
      <article v-for="(block, index) in page.content" :key="`volunteer-${index}`" class="content-page__block">
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
