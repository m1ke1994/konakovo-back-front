<script setup>
import { computed } from "vue";
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import NewsCard from "../components/NewsCard.vue";
import { newsItems } from "../data/news";

const sortedNews = computed(() =>
  [...newsItems].sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
);
</script>

<template>
  <AppHeader />

  <main class="news-page">
    <section class="news-page__hero">
      <h1 class="news-page__title">Новости</h1>
      <p class="news-page__subtitle">
        Актуальные обновления «Нового Конаково»: события, форматы, изменения расписания и важные анонсы.
      </p>
    </section>

    <section class="news-page__grid">
      <NewsCard v-for="item in sortedNews" :key="item.id" :item="item" />
    </section>
  </main>

  <AppFooter />
</template>

<style scoped>
.news-page {
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 24px 80px;
  display: grid;
  gap: 22px;
}

.news-page__hero {
  display: grid;
  gap: 10px;
  padding-top: 12px;
}

.news-page__title {
  margin: 0;
  font-size: clamp(32px, 5vw, 46px);
  color: var(--text-strong);
}

.news-page__subtitle {
  margin: 0;
  max-width: 780px;
  font-size: 15px;
  line-height: 1.6;
  color: var(--muted);
}

.news-page__grid {
  display: grid;
  gap: 18px;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  align-items: stretch;
}

@media (max-width: 1024px) {
  .news-page__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .news-page {
    padding: 0 16px 64px;
  }

  .news-page__grid {
    grid-template-columns: 1fr;
  }
}
</style>
