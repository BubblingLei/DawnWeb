<script setup lang="ts">
import type { Product } from '~/types/product'
import { categoryBySlug } from '~/data/products'

const props = defineProps<{ product: Product }>()

const { lt } = useLocalized()
const localePath = useLocalePath()
const { t } = useI18n()

const href = computed(() => localePath(`/products/${props.product.slug}`))
const category = computed(() => categoryBySlug(props.product.category))
</script>

<template>
  <NuxtLinkLocale
    :to="href"
    class="group block overflow-hidden rounded-2xl bg-white shadow-sm ring-1 ring-black/5 transition-all duration-normal hover:-translate-y-1 hover:shadow-lg"
  >
    <div class="overflow-hidden">
      <ProductPlaceholder :tone="product.tone" :category="product.category" />
    </div>
    <div class="p-5">
      <p class="text-xs uppercase tracking-wider text-accent">
        {{ lt(category.name) }}
      </p>
      <h3 class="mt-1 text-lg font-semibold text-text group-hover:text-accent-strong">
        {{ lt(product.name) }}
      </h3>
      <p class="mt-2 text-sm text-text-muted">{{ lt(product.summary) }}</p>
      <div class="mt-4 flex items-center justify-between text-xs text-text-muted">
        <span>{{ lt(product.material) }}</span>
        <span>MOQ {{ product.moq }}</span>
      </div>
    </div>
  </NuxtLinkLocale>
</template>
