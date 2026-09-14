<script setup lang="ts">
const { t } = useI18n()

const values = ['craft', 'sustainable', 'reliable', 'partner'] as const

useSeoMeta({
  title: () => `${t('nav.about')} — ${t('brand')}`,
  description: () => t('about.metaDescription'),
})
</script>

<template>
  <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
    <h1 class="text-h2 text-text">{{ t('about.title') }}</h1>
    <p class="mt-4 max-w-3xl text-lg text-text-muted">{{ t('about.intro') }}</p>

    <div class="mt-14 grid gap-10 md:grid-cols-2">
      <div class="rounded-3xl bg-surface-muted p-10">
        <h2 class="text-xl font-semibold text-text">{{ t('about.story.title') }}</h2>
        <p class="mt-4 text-text-muted">{{ t('about.story.body1') }}</p>
        <p class="mt-4 text-text-muted">{{ t('about.story.body2') }}</p>
      </div>

      <div class="rounded-3xl border border-border p-10">
        <h2 class="text-xl font-semibold text-text">{{ t('about.craft.title') }}</h2>
        <p class="mt-4 text-text-muted">{{ t('about.craft.body') }}</p>
        <ul class="mt-5 space-y-2 text-sm text-text-muted">
          <li v-for="i in 3" :key="i">— {{ t(`about.craft.point${i}`) }}</li>
        </ul>
      </div>
    </div>

    <section class="mt-16">
      <h2 class="text-h2 text-text">{{ t('about.values.title') }}</h2>
      <div class="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div
          v-for="v in values"
          :key="v"
          class="rounded-2xl border border-border p-6"
        >
          <h3 class="text-lg font-semibold text-text">
            {{ t(`about.values.${v}.title`) }}
          </h3>
          <p class="mt-2 text-sm text-text-muted">{{ t(`about.values.${v}.desc`) }}</p>
        </div>
      </div>
    </section>

    <section class="mt-16 rounded-3xl bg-accent-strong p-10 text-white">
      <h2 class="text-xl font-semibold">{{ t('about.cta') }}</h2>
      <p class="mt-3 text-white/80">{{ t('about.ctaSubtitle') }}</p>
      <NuxtLinkLocale
        to="/contact"
        class="mt-6 inline-block rounded-full bg-white px-7 py-3 text-sm font-semibold text-accent-strong transition-transform duration-fast hover:scale-[1.03]"
      >
        {{ t('cta.inquiry') }}
      </NuxtLinkLocale>
    </section>
  </div>
</template>
