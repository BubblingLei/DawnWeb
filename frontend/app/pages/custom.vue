<script setup lang="ts">
import { categories } from '~/data/products'

const { t } = useI18n()
const { lt } = useLocalized()
const { open } = useInquiryModal()

const pathways = [
  { key: 'image', icon: '◐' },
  { key: 'idea', icon: '◡' },
] as const

const capabilities = [
  { key: 'size', icon: '◱' },
  { key: 'color', icon: '◐' },
  { key: 'material', icon: '✧' },
  { key: 'logo', icon: '✎' },
  { key: 'packaging', icon: '▣' },
  { key: 'moq', icon: '◷' },
] as const

useSeoMeta({
  title: () => `${t('brand')} — ${t('custom.metaTitle')}`,
  description: () => t('custom.metaDescription'),
  ogTitle: () => `${t('brand')} — ${t('custom.metaTitle')}`,
  ogDescription: () => t('custom.metaDescription'),
})
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="mx-auto max-w-6xl px-6 pt-16 md:pt-24">
      <div class="max-w-3xl">
        <p class="mb-4 text-sm uppercase tracking-[0.2em] text-terracotta">
          {{ t('custom.heroEyebrow') }}
        </p>
        <h1 class="text-hero text-text">{{ t('custom.heroTitle') }}</h1>
        <p class="mt-6 max-w-xl text-lg text-text-muted">
          {{ t('custom.heroSubtitle') }}
        </p>
        <button
          type="button"
          class="mt-10 rounded-full bg-accent-strong px-7 py-3 text-sm font-medium text-white transition-transform duration-fast hover:scale-[1.03]"
          @click="open('custom')"
        >
          {{ t('custom.ctaButton') }}
        </button>
      </div>
    </section>

    <!-- 两种定制方式 -->
    <section class="mx-auto max-w-6xl px-6 py-20 md:py-28">
      <h2 class="text-h2 text-text">{{ t('custom.pathwaysTitle') }}</h2>
      <p class="mt-3 max-w-xl text-text-muted">{{ t('custom.pathwaysSubtitle') }}</p>

      <div class="mt-10 grid gap-6 md:grid-cols-2">
        <div class="rounded-3xl bg-accent-strong p-8 text-white sm:p-10">
          <span class="text-3xl" aria-hidden="true">{{ pathways[0].icon }}</span>
          <h3 class="mt-5 text-2xl font-semibold">{{ t('custom.pathwayImageTitle') }}</h3>
          <p class="mt-3 text-white/80">{{ t('custom.pathwayImageDesc') }}</p>
        </div>
        <div class="rounded-3xl border border-border p-8 sm:p-10">
          <span class="text-3xl text-terracotta" aria-hidden="true">{{ pathways[1].icon }}</span>
          <h3 class="mt-5 text-2xl font-semibold text-text">{{ t('custom.pathwayIdeaTitle') }}</h3>
          <p class="mt-3 text-text-muted">{{ t('custom.pathwayIdeaDesc') }}</p>
        </div>
      </div>
    </section>

    <!-- 可定制项 -->
    <section class="bg-surface-muted">
      <div class="mx-auto max-w-6xl px-6 py-20 md:py-28">
        <h2 class="text-h2 text-text">{{ t('custom.capabilitiesTitle') }}</h2>
        <p class="mt-3 max-w-xl text-text-muted">{{ t('custom.capabilitiesSubtitle') }}</p>

        <div class="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <div
            v-for="cap in capabilities"
            :key="cap.key"
            class="rounded-2xl bg-white p-6 shadow-sm ring-1 ring-black/5 transition-all duration-normal hover:-translate-y-1 hover:shadow-lg"
          >
            <span class="text-2xl text-terracotta" aria-hidden="true">{{ cap.icon }}</span>
            <h3 class="mt-4 text-lg font-semibold text-text">
              {{ t(`custom.capabilities.${cap.key}.title`) }}
            </h3>
            <p class="mt-2 text-sm text-text-muted">
              {{ t(`custom.capabilities.${cap.key}.desc`) }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 可定制品类 -->
    <section class="mx-auto max-w-6xl px-6 py-20 md:py-28">
      <h2 class="text-h2 text-text">{{ t('custom.categoriesTitle') }}</h2>
      <p class="mt-3 max-w-xl text-text-muted">{{ t('custom.categoriesSubtitle') }}</p>

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
    </section>

    <!-- CTA -->
    <section class="mx-auto max-w-6xl px-6 pb-24">
      <div class="rounded-3xl bg-accent-strong px-8 py-16 text-center text-white">
        <h2 class="text-h2">{{ t('custom.ctaTitle') }}</h2>
        <p class="mx-auto mt-4 max-w-xl text-white/80">
          {{ t('custom.ctaSubtitle') }}
        </p>
        <button
          type="button"
          class="mt-8 inline-block rounded-full bg-white px-7 py-3 text-sm font-semibold text-accent-strong transition-transform duration-fast hover:scale-[1.03]"
          @click="open('custom')"
        >
          {{ t('custom.ctaButton') }}
        </button>
      </div>
    </section>
  </div>
</template>
