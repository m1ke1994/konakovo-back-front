<script setup>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

const page = {
  title: "Обо мне",
  subtitle:
    "История проекта «Новое Конаково», принципы работы и подход к созданию пространства, где отдых становится восстановлением.",
  content: [
    {
      type: "text",
      heading: "Как родилась идея",
      value:
        "Проект начался не как бизнес-идея, а как ответ на личный запрос: найти место, где можно замедлиться без чувства вины за паузу. Из этого постепенно выросла среда, где в центре не развлечение, а качество присутствия.",
    },
    {
      type: "text",
      value:
        "Я переехала из города в Конаково, чтобы вернуть себе более живой ритм. В процессе стало очевидно, что подобный запрос есть у многих: людям нужен не еще один быстрый формат, а безопасное пространство для восстановления.",
    },
    {
      type: "image",
      src: "/images/article-1.jpg",
      alt: "Природный маршрут в Новом Конаково",
    },
    {
      type: "text",
      heading: "Философия пространства",
      value:
        "Мы строим программы вокруг простых вещей: движение, тишина, внимание, диалог. Чем меньше визуального и информационного шума, тем лучше слышно себя и легче принимать решения без внутреннего давления.",
    },
    {
      type: "text",
      value:
        "В «Новом Конаково» нет цели заполнить каждую минуту событиями. Наоборот, мы оставляем место для пауз, потому что именно они дают глубину любому формату — от прогулки до чайной встречи.",
    },
    {
      type: "video",
      src: "https://www.youtube.com/embed/ScMzIvxBSi4",
    },
    {
      type: "text",
      heading: "Как мы работаем с гостями",
      value:
        "Каждый сценарий собирается под состояние и запрос человека. Кому-то нужен активный день с маршрутом и практиками, а кому-то — спокойный темп, разговор и время у воды. Оба варианта одинаково ценны.",
    },
    {
      type: "image",
      src: "/images/article-2.jpg",
      alt: "Береговая зона для отдыха",
    },
    {
      type: "text",
      heading: "Что остается после визита",
      value:
        "Главный результат — не вау-эффект на один вечер, а ровное устойчивое состояние. Участники чаще всего уезжают с ощущением ясности, собранности и пониманием, как сохранить этот ритм в обычной жизни.",
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
      <article v-for="(block, index) in page.content" :key="`about-${index}`" class="content-page__block">
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
