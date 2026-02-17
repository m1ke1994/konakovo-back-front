<script setup>
import PageTemplate from '../components/PageTemplate.vue';
import AppHeader from '../components/AppHeader.vue';
import AppFooter from '../components/AppFooter.vue';

const pageData = {
    title: 'Братство лосей',
    subtitle:
        'Экскурсии и встречи в духе «Нового Конаково»: мягкий ритм, внимательные истории и контакт с природой, который остаётся с вами надолго.',
    heroImage: '/2.jpeg',
    sections: [
        {
            title: 'Экскурсии с заботой',
            text: 'Маршруты строятся так, чтобы вы успели замедлиться, услышать лес и увидеть главное — без спешки.',
        },
        {
            title: 'Наблюдение и тишина',
            text: 'Встречи с животными, наблюдения за природой и небольшие практики внимания.',
        },
        {
            title: 'Сообщество',
            text: 'После прогулки остаётся желание вернуться: общение, поддержка и ощущение «своего круга».',
        },
    ],
    gallery: ['/2.jpeg', '/1.jpeg', '/3.jpeg', '/6.jpeg'],
};
</script>

<template>
    <AppHeader />
    <PageTemplate v-bind="pageData" />
    <AppFooter />
</template>
