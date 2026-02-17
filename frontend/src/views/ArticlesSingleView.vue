<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import { materials } from "../data/articles";

const route = useRoute();

const article = computed(() => {
  const id = Number(route.params.id);
  return materials.find((item) => item.id === id) ?? null;
});

const formattedDate = computed(() => {
  if (!article.value) return "";
  return new Date(article.value.date).toLocaleDateString("ru-RU", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  });
});
</script>

<template>
  <AppHeader />

  <main class="single-article">
    <section v-if="article" class="single-article__content">
      <router-link class="single-article__back" to="/articles">Назад к статьям</router-link>
      <p class="single-article__date">{{ formattedDate }}</p>
      <h1 class="single-article__title">{{ article.title }}</h1>
      <img class="single-article__cover" :src="article.image" :alt="article.title" />

      <div v-if="article.videoUrl" class="single-article__video">
        <iframe
          :src="article.videoUrl"
          title="Видео в статье"
          loading="lazy"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen
        ></iframe>
      </div>

      <div class="single-article__text" v-html="article.content"></div>
    </section>

    <section v-else class="single-article__not-found glass-card">
      <h1>Материал не найден</h1>
      <router-link class="single-article__back" to="/articles">Назад к статьям</router-link>
    </section>
  </main>

  <AppFooter />
</template>

<style scoped>
.single-article {
  max-width: 920px;
  margin: 0 auto;
  padding: 0 20px 72px;
}

.single-article__content {
  display: grid;
  gap: 16px;
}

.single-article__back {
  justify-self: start;
  padding: 9px 14px;
  border-radius: 999px;
  border: 1px solid var(--border);
  background: var(--primary-soft);
  color: var(--text-strong);
  font-size: 13px;
  transition: transform 160ms ease, box-shadow 160ms ease;
}

.single-article__back:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 18px var(--shadow);
}

.single-article__date {
  margin: 0;
  font-size: 13px;
  color: var(--muted);
}

.single-article__title {
  margin: 0;
  font-size: clamp(30px, 5vw, 46px);
  line-height: 1.1;
  color: var(--text-strong);
}

.single-article__cover {
  width: 100%;
  border-radius: 20px;
  max-height: 460px;
  object-fit: cover;
}

.single-article__video {
  border-radius: 18px;
  overflow: hidden;
}

.single-article__video iframe {
  width: 100%;
  aspect-ratio: 16 / 9;
  border: 0;
  display: block;
}

.single-article__text {
  font-size: 16px;
  line-height: 1.7;
  color: var(--text);
}

.single-article__text :deep(p) {
  margin: 0 0 14px;
}

.single-article__not-found {
  margin-top: 24px;
  padding: 22px;
  display: grid;
  gap: 12px;
}

.single-article__not-found h1 {
  margin: 0;
  font-size: 28px;
  color: var(--text-strong);
}

@media (max-width: 720px) {
  .single-article {
    padding: 0 14px 58px;
  }

  .single-article__text {
    font-size: 15px;
  }
}
</style>
