<script setup lang="ts">
const { locale, t } = useI18n()
const switchLocalePath = useSwitchLocalePath()

const nav = [
  { key: 'home', to: '/' },
  { key: 'products', to: '/products' },
  { key: 'about', to: '/about' },
  { key: 'contact', to: '/contact' },
] as const

const otherLocale = computed(() => (locale.value === 'en' ? 'zh' : 'en'))
</script>

<template>
  <div class="min-h-screen bg-surface text-text">
    <header
      class="flex items-center justify-between px-6 py-5 border-b border-border"
    >
      <span class="font-display text-xl tracking-tight">{{ t('brand') }}</span>

      <nav class="hidden items-center gap-8 text-sm md:flex">
        <NuxtLinkLocale
          v-for="item in nav"
          :key="item.key"
          :to="item.to"
          class="text-text-muted transition-colors duration-fast hover:text-accent-strong"
        >
          {{ t(`nav.${item.key}`) }}
        </NuxtLinkLocale>
      </nav>

      <NuxtLink
        :to="switchLocalePath(otherLocale)"
        class="rounded-full border border-border px-4 py-1.5 text-sm transition-colors duration-fast hover:border-accent hover:text-accent-strong"
      >
        {{ otherLocale === 'zh' ? '中文' : 'English' }}
      </NuxtLink>
    </header>

    <main class="mx-auto max-w-5xl px-6 py-24">
      <p class="mb-4 text-sm uppercase tracking-widest text-accent">
        {{ t('brand') }}
      </p>
      <h1 class="text-hero max-w-3xl text-text">
        {{ t('hero.title') }}
      </h1>
      <p class="mt-6 max-w-xl text-lg text-text-muted">
        {{ t('hero.subtitle') }}
      </p>
      <div class="mt-10 flex flex-wrap gap-4">
        <a
          href="/contact"
          class="rounded-full bg-accent-strong px-6 py-3 text-sm font-medium text-white transition-transform duration-fast hover:scale-[1.02]"
        >
          {{ t('cta.inquiry') }}
        </a>
        <a
          href="/products"
          class="rounded-full border border-border px-6 py-3 text-sm font-medium transition-colors duration-fast hover:border-accent hover:text-accent-strong"
        >
          {{ t('cta.viewProducts') }}
        </a>
      </div>
    </main>
  </div>
</template>
