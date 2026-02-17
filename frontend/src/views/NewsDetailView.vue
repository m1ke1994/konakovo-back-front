<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { getNewsBySlug } from '../data/news'
import AppHeader from '../components/AppHeader.vue'
import AppFooter from '../components/AppFooter.vue'

const route = useRoute()

const newsItem = computed(() => getNewsBySlug(route.params.slug))
</script>

<template>
  <AppHeader />
  <section class="news-detail">
    <div v-if="newsItem" class="news-detail__content">
      <router-link class="news-detail__back" to="/news">← Все новости</router-link>

      <article class="news-detail__article glass-card">
        <img :src="newsItem.image" :alt="newsItem.title" class="news-detail__image" />

        <div class="news-detail__inner">
          <div class="news-detail__meta">
            <span class="news-detail__chip">{{ newsItem.category }}</span>
            <span class="news-detail__date">{{ newsItem.date }}</span>
          </div>

          <h1 class="news-detail__title">{{ newsItem.title }}</h1>

          <p v-for="(paragraph, index) in newsItem.content" :key="`p-${index}`" class="news-detail__text">
            {{ paragraph }}
          </p>
        </div>
      </article>
    </div>

    <div v-else class="news-detail__empty glass-card">
      <h1 class="news-detail__empty-title">Новость не найдена</h1>
      <p class="news-detail__empty-text">Возможно, ссылка устарела или материал был перенесен.</p>
      <router-link class="news-detail__back" to="/news">Перейти к списку новостей</router-link>
    </div>
  </section>
  <AppFooter />
</template>

<style scoped>
.news-detail {
  min-height: 100vh;
  padding: calc(var(--header-h, 72px) + 28px) 24px 80px;
  max-width: var(--container-max);
  margin: 0 auto;
}

.news-detail__content {
  display: grid;
  gap: 14px;
}

.news-detail__back {
  width: fit-content;
  color: var(--text-strong);
  font-size: 14px;
}

.news-detail__article {
  overflow: hidden;
}

.news-detail__image {
  width: 100%;
  aspect-ratio: 16 / 7;
  object-fit: cover;
  display: block;
}

.news-detail__inner {
  padding: 20px;
  display: grid;
  gap: 12px;
}

.news-detail__meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.news-detail__chip {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  border: 1px solid var(--border);
  background: color-mix(in srgb, var(--card) 74%, transparent);
  padding: 6px 10px;
  font-size: 12px;
}

.news-detail__date {
  font-size: 12px;
  color: var(--muted);
}

.news-detail__title {
  margin: 0;
  color: var(--text-strong);
  font-size: 32px;
  line-height: 1.2;
}

.news-detail__text {
  margin: 0;
  color: var(--text);
  line-height: 1.75;
}

.news-detail__empty {
  padding: 20px;
  display: grid;
  gap: 10px;
}

.news-detail__empty-title {
  margin: 0;
  color: var(--text-strong);
  font-size: 24px;
}

.news-detail__empty-text {
  margin: 0;
  color: var(--muted);
}

@media (max-width: 768px) {
  .news-detail {
    padding: calc(var(--header-h, 72px) + 20px) 16px 56px;
  }

  .news-detail__title {
    font-size: 26px;
  }

  .news-detail__image {
    aspect-ratio: 4 / 3;
  }
}
</style>
