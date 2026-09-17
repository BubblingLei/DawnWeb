<script setup lang="ts">
const { locale, t } = useI18n()
const switchLocalePath = useSwitchLocalePath()

const nav = [
  { key: 'home', to: '/' },
  { key: 'products', to: '/products' },
  { key: 'custom', to: '/custom' },
  { key: 'about', to: '/about' },
  { key: 'contact', to: '/contact' },
] as const

const otherLocale = computed(() => (locale.value === 'en' ? 'zh' : 'en'))
</script>

<template>
  <header
    class="sticky top-0 z-20 border-b border-border bg-surface/90 backdrop-blur"
  >
    <div class="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
      <NuxtLinkLocale
        to="/"
        class="font-display text-xl tracking-tight text-text"
      >
        {{ t('brand') }}
      </NuxtLinkLocale>

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
        class="rounded-full border border-border px-4 py-1.5 text-sm text-text-muted transition-colors duration-fast hover:border-accent hover:text-accent-strong"
      >
        {{ otherLocale === 'zh' ? '中文' : 'English' }}
      </NuxtLink>
    </div>
  </header>
</template>
