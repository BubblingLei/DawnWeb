<script setup lang="ts">
import { categories, products } from '~/data/products'

const { t, locale } = useI18n()
const { lt } = useLocalized()
const localePath = useLocalePath()

const featured = computed(() => products.filter((p) => p.featured).slice(0, 4))

const advantages = [
  { key: 'quality', icon: '✦' },
  { key: 'moq', icon: '◆' },
  { key: 'export', icon: '●' },
  { key: 'custom', icon: '▲' },
] as const

useSeoMeta({
  title: () => `${t('brand')} — ${t('home.metaTitle')}`,
  description: () => t('home.metaDescription'),
  ogTitle: () => `${t('brand')} — ${t('home.metaTitle')}`,
  ogDescription: () => t('home.metaDescription'),
})
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="mx-auto max-w-6xl px-6 pt-16 md:pt-24">
      <div class="grid items-center gap-12 md:grid-cols-2">
        <div>
          <p class="mb-4 text-sm uppercase tracking-[0.2em] text-accent">
            {{ t('brand') }}
          </p>
          <h1 class="text-hero text-text">
            {{ t('home.heroTitle') }}
          </h1>
          <p class="mt-6 max-w-xl text-lg text-text-muted">
            {{ t('home.heroSubtitle') }}
          </p>
          <div class="mt-10 flex flex-wrap gap-4">
            <NuxtLinkLocale
              to="/contact"
              class="rounded-full bg-accent-strong px-7 py-3 text-sm font-medium text-white transition-transform duration-fast hover:scale-[1.03]"
            >
              {{ t('cta.inquiry') }}
            </NuxtLinkLocale>
            <NuxtLinkLocale
              to="/products"
              class="rounded-full border border-border px-7 py-3 text-sm font-medium text-text transition-colors duration-fast hover:border-accent hover:text-accent-strong"
            >
              {{ t('cta.viewProducts') }}
            </NuxtLinkLocale>
          </div>
        </div>

        <div
          class="relative aspect-square overflow-hidden rounded-3xl bg-[hsl(80_28%_86%)]"
        >
          <div
            class="absolute inset-0 bg-[radial-gradient(120%_90%_at_30%_20%,hsl(80_32%_92%)_0%,hsl(80_26%_78%)_100%)]"
          />
          <svg
            viewBox="0 0 200 200"
            class="absolute inset-0 m-auto h-2/3 w-2/3 opacity-30"
            fill="hsl(80_30%_50%)"
            aria-hidden="true"
          >
            <path d="M70 150 h60 l-8 -20 h8 l-10 -18 h-40 l-10 18 h8 z" />
            <path d="M82 70 h36 l-6 18 c14 8 16 26 10 44 l-44 0 c-6 -18 -4 -36 10 -44 z" />
          </svg>
        </div>
      </div>
    </section>

    <!-- 精选产品 -->
    <section class="mx-auto max-w-6xl px-6 py-20 md:py-28">
      <div class="mb-10 flex items-end justify-between">
        <div>
          <p class="text-sm uppercase tracking-wider text-accent">
            {{ t('home.featuredEyebrow') }}
          </p>
          <h2 class="mt-2 text-h2 text-text">{{ t('home.featuredTitle') }}</h2>
        </div>
        <NuxtLinkLocale
          to="/products"
          class="hidden text-sm text-accent-strong hover:underline md:block"
        >
          {{ t('home.viewAll') }} →
        </NuxtLinkLocale>
      </div>

      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <ProductCard
          v-for="product in featured"
          :key="product.id"
          :product="product"
        />
      </div>
    </section>

    <!-- 分类入口 -->
    <section class="bg-surface-muted">
      <div class="mx-auto max-w-6xl px-6 py-20 md:py-28">
        <h2 class="text-h2 text-text">{{ t('home.categoriesTitle') }}</h2>
        <div class="mt-10 grid gap-6 md:grid-cols-3">
          <NuxtLinkLocale
            v-for="category in categories"
            :key="category.slug"
            :to="`/products?category=${category.slug}`"
            class="group rounded-2xl bg-white p-8 shadow-sm ring-1 ring-black/5 transition-all duration-normal hover:-translate-y-1 hover:shadow-lg"
          >
            <h3 class="text-xl font-semibold text-text group-hover:text-accent-strong">
              {{ lt(category.name) }}
            </h3>
            <p class="mt-3 text-sm text-text-muted">{{ lt(category.description) }}</p>
            <span class="mt-5 inline-block text-sm text-accent-strong">
              {{ t('home.browse') }} →
            </span>
          </NuxtLinkLocale>
        </div>
      </div>
    </section>

    <!-- 优势 -->
    <section class="mx-auto max-w-6xl px-6 py-20 md:py-28">
      <h2 class="text-h2 text-text">{{ t('home.advantagesTitle') }}</h2>
      <div class="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div
          v-for="adv in advantages"
          :key="adv.key"
          class="rounded-2xl border border-border p-6"
        >
          <span class="text-2xl text-terracotta" aria-hidden="true">{{ adv.icon }}</span>
          <h3 class="mt-4 text-lg font-semibold text-text">
            {{ t(`home.advantage.${adv.key}.title`) }}
          </h3>
          <p class="mt-2 text-sm text-text-muted">
            {{ t(`home.advantage.${adv.key}.desc`) }}
          </p>
        </div>
      </div>
    </section>

    <!-- 询盘 CTA -->
    <section class="mx-auto max-w-6xl px-6 pb-24">
      <div
        class="rounded-3xl bg-accent-strong px-8 py-16 text-center text-white"
      >
        <h2 class="text-h2">{{ t('home.ctaTitle') }}</h2>
        <p class="mx-auto mt-4 max-w-xl text-white/80">
          {{ t('home.ctaSubtitle') }}
        </p>
        <NuxtLinkLocale
          to="/contact"
          class="mt-8 inline-block rounded-full bg-white px-7 py-3 text-sm font-semibold text-accent-strong transition-transform duration-fast hover:scale-[1.03]"
        >
          {{ t('cta.inquiry') }}
        </NuxtLinkLocale>
      </div>
    </section>
  </div>
</template>
