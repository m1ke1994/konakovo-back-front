<script setup>
import { computed } from "vue";
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import ProfileHero from "../components/Profile/ProfileHero.vue";
import ProductGrid from "../components/Profile/ProductGrid.vue";
import ScheduleSection from "../components/ScheduleSection.vue";
import FeedbackSection from "../components/FeedbackSection.vue";
import ReviewsSection from "../components/Profile/ReviewsSection.vue";
import ArticleCard from "../components/ArticleCard.vue";
import NewsCard from "../components/NewsCard.vue";
import { materials } from "../data/articles";
import { newsItems } from "../data/news";

const menuItems = [
  { label: "Обо мне", to: "/about" },
  { label: "Братство Лосей", to: "/moose" },
  { label: "Волонтерские программы", to: "/volunteer" },
  { label: "Беговой клуб", to: "/running-club" },
  { label: "Услуги и цены", href: "#services", mobileOnly: true },
  { label: "Статьи / Видео", to: "/articles" },
  { label: "Новости", to: "/news" },
  { label: "Расписание", to: "/schedule" },
  { label: "Контакты", to: "/contacts" },
];

const latestMaterials = computed(() =>
  [...materials]
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
    .slice(0, 4)
);

const latestNews = computed(() =>
  [...newsItems]
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
    .slice(0, 4)
);
</script>

<template>
  <div class="profile-page">
    <AppHeader />
    <section class="site-shell">
      <div class="profile-content">
        <ProfileHero :menu-items="menuItems" />

        <section id="services" class="app-section" v-reveal>
          <div class="app-section__inner">
            <h2 class="app-section__title">Услуги и форматы</h2>
            <div class="app-section__content">
              <ProductGrid />
            </div>
          </div>
        </section>

        <section id="articles" class="app-section" v-reveal>
          <div class="app-section__inner">
            <div class="articles-home__head">
              <h2 class="app-section__title articles-home__title">Статьи / Видео</h2>
            </div>

            <div class="articles-home__grid">
              <ArticleCard
                v-for="item in latestMaterials"
                :key="item.id"
                :item="item"
                :show-description="false"
              />
            </div>
            <div class="articles-home__footer">
              <router-link class="articles-home__link btn-secondary" to="/articles">Все материалы / Видео</router-link>
            </div>
          </div>
        </section>

        <section id="schedule" class="app-section" v-reveal>
          <div class="app-section__inner">
            <h2 class="app-section__title">Расписание занятий</h2>
            <div class="app-section__content">
              <ScheduleSection />
            </div>
          </div>
        </section>

        <section id="feedback" class="app-section" v-reveal>
          <div class="app-section__inner">
            <h2 class="app-section__title">Собери сценарий дня</h2>
            <div class="app-section__content">
              <FeedbackSection />
            </div>
          </div>
        </section>

        <section id="reviews" class="app-section" v-reveal>
          <div class="app-section__inner">
            <h2 class="app-section__title">Отзывы</h2>
            <div class="app-section__content">
              <ReviewsSection />
            </div>
          </div>
        </section>

        <section id="news" class="app-section" v-reveal>
          <div class="app-section__inner">
            <div class="news-home__head">
              <h2 class="app-section__title news-home__title">Новости</h2>
            </div>
            <div class="news-home__grid">
              <NewsCard v-for="item in latestNews" :key="item.id" :item="item" />
            </div>
            <div class="news-home__footer">
              <router-link class="news-home__link btn-secondary" to="/news">Все новости</router-link>
            </div>
          </div>
        </section>
      </div>
    </section>
    <AppFooter />
  </div>
</template>

<style scoped>
.profile-page {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
  padding: 0 0 60px;
  box-sizing: border-box;
  --header-offset: 124px;
}

.site-shell {
  width: 100%;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
  background: var(--bg);
}

.profile-content {
  padding: 0;
  box-sizing: border-box;
}

.app-section {
  width: 100%;
  padding: var(--section-padding, 64px) 0;
  background: var(--bg);
  scroll-margin-top: var(--header-offset, 120px);
}

.app-section__inner {
  max-width: var(--container-max, 1200px);
  margin: 0 auto;
  padding: 0 28px;
  box-sizing: border-box;
}

.app-section__title {
  margin: 0 0 28px;
  text-align: center;
  font-size: 28px;
  color: var(--text);
}

.app-section__content {
  width: 100%;
}

.articles-home__head {
  display: grid;
  gap: 12px;
  justify-items: center;
}

.articles-home__title {
  margin-bottom: 0;
}

.articles-home__grid {
  margin-top: 22px;
  display: grid;
  gap: 18px;
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.articles-home__footer {
  margin-top: 18px;
  display: flex;
  justify-content: flex-end;
}

.news-home__head {
  display: grid;
  gap: 12px;
  justify-items: center;
}

.news-home__title {
  margin-bottom: 0;
}

.news-home__grid {
  margin-top: 22px;
  display: grid;
  gap: 18px;
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.news-home__footer {
  margin-top: 18px;
  display: flex;
  justify-content: flex-end;
}

@media (max-width: 1200px) {
  .articles-home__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .news-home__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .app-section {
    padding: var(--section-padding-mobile, 40px) 0;
  }

  .app-section__inner {
    padding: 0 18px;
  }

  .app-section__title {
    font-size: 24px;
  }

  .articles-home__grid {
    grid-template-columns: 1fr;
  }

  .news-home__grid {
    grid-template-columns: 1fr;
  }

  .articles-home__footer,
  .news-home__footer {
    justify-content: center;
  }

  .articles-home__link,
  .news-home__link {
    width: 100%;
  }
}
</style>
