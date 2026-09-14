<script setup lang="ts">
import { categoryBySlug, products } from '~/data/products'

const { t } = useI18n()
const { lt } = useLocalized()
const route = useRoute()
const localePath = useLocalePath()

const slug = computed(() => String(route.params.slug))
const product = computed(() => products.find((p) => p.slug === slug.value))

const related = computed(() => {
  if (!product.value) return []
  return products
    .filter((p) => p.category === product.value!.category && p.id !== product.value!.id)
    .slice(0, 3)
})

const category = computed(() => (product.value ? categoryBySlug(product.value.category) : null))

const inquiryHref = computed(() =>
  product.value ? localePath(`/contact?product=${product.value.slug}`) : localePath('/contact'),
)

useSeoMeta({
  title: () => (product.value ? `${lt(product.value.name)} — ${t('brand')}` : t('brand')),
  description: () => product.value?.summary.en ?? t('products.metaDescription'),
})

if (!product.value) {
  throw createError({ statusCode: 404, statusMessage: 'Product not found' })
}
</script>

<template>
  <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
    <nav class="mb-8 text-sm text-text-muted">
      <NuxtLinkLocale to="/products" class="hover:text-accent-strong">
        {{ t('nav.products') }}
      </NuxtLinkLocale>
      <span class="mx-2">/</span>
      <span v-if="category">{{ lt(category.name) }}</span>
    </nav>

    <div class="grid gap-10 lg:grid-cols-2">
      <!-- 大图占位 -->
      <div class="lg:sticky lg:top-24 lg:self-start">
        <ProductPlaceholder :tone="product.tone" :category="product.category" />
      </div>

      <!-- 信息 -->
      <div>
        <p class="text-sm uppercase tracking-wider text-accent">
          {{ lt(category!.name) }}
        </p>
        <h1 class="mt-2 text-h2 text-text">{{ lt(product.name) }}</h1>
        <p class="mt-4 text-lg text-text-muted">{{ lt(product.summary) }}</p>
        <p class="mt-4 text-text-muted">{{ lt(product.description) }}</p>

        <!-- 规格表 -->
        <dl class="mt-8 overflow-hidden rounded-2xl border border-border">
          <div class="grid grid-cols-3 border-b border-border bg-surface-muted px-5 py-3 text-sm">
            <dt class="font-medium text-text">{{ t('product.material') }}</dt>
            <dd class="col-span-2 text-text-muted">{{ lt(product.material) }}</dd>
          </div>
          <div class="grid grid-cols-3 border-b border-border px-5 py-3 text-sm">
            <dt class="font-medium text-text">{{ t('product.sizes') }}</dt>
            <dd class="col-span-2 text-text-muted">{{ product.sizes.join(' · ') }}</dd>
          </div>
          <div class="grid grid-cols-3 px-5 py-3 text-sm">
            <dt class="font-medium text-text">{{ t('product.moq') }}</dt>
            <dd class="col-span-2 text-text-muted">{{ product.moq }} {{ t('product.units') }}</dd>
          </div>
        </dl>

        <NuxtLinkLocale
          :to="inquiryHref"
          class="mt-8 inline-block rounded-full bg-accent-strong px-8 py-3.5 text-sm font-semibold text-white transition-transform duration-fast hover:scale-[1.03]"
        >
          {{ t('cta.inquiry') }}
        </NuxtLinkLocale>
      </div>
    </div>

    <!-- 相关产品 -->
    <section v-if="related.length" class="mt-20">
      <h2 class="text-h2 text-text">{{ t('product.related') }}</h2>
      <div class="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <ProductCard
          v-for="p in related"
          :key="p.id"
          :product="p"
        />
      </div>
    </section>
  </div>
</template>
