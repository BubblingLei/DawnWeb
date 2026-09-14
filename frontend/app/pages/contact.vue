<script setup lang="ts">
import { products } from '~/data/products'

const { t } = useI18n()
const route = useRoute()

const prefillProduct = computed(() => {
  const slug = route.query.product as string | undefined
  if (!slug) return ''
  const product = products.find((p) => p.slug === slug)
  return product ? product.name.en : ''
})

useSeoMeta({
  title: () => `${t('nav.contact')} — ${t('brand')}`,
  description: () => t('contact.metaDescription'),
})
</script>

<template>
  <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
    <h1 class="text-h2 text-text">{{ t('contact.title') }}</h1>
    <p class="mt-4 max-w-2xl text-lg text-text-muted">{{ t('contact.subtitle') }}</p>

    <div class="mt-12 grid gap-12 lg:grid-cols-[1fr_1.4fr]">
      <!-- 联系方式 -->
      <div class="space-y-6">
        <div>
          <p class="text-xs uppercase tracking-wider text-accent">
            {{ t('contact.info.emailLabel') }}
          </p>
          <p class="mt-1 text-text">{{ t('contact.email') }}</p>
        </div>
        <div>
          <p class="text-xs uppercase tracking-wider text-accent">
            {{ t('contact.info.phoneLabel') }}
          </p>
          <p class="mt-1 text-text">{{ t('contact.phone') }}</p>
        </div>
        <div>
          <p class="text-xs uppercase tracking-wider text-accent">
            {{ t('contact.info.addressLabel') }}
          </p>
          <p class="mt-1 text-text">{{ t('contact.address') }}</p>
        </div>
        <p class="text-sm text-text-muted">{{ t('contact.info.note') }}</p>
      </div>

      <!-- 询盘表单 -->
      <div class="rounded-3xl border border-border p-8">
        <h2 class="text-xl font-semibold text-text">{{ t('contact.form.title') }}</h2>
        <p class="mb-6 mt-2 text-sm text-text-muted">{{ t('contact.form.subtitle') }}</p>
        <InquiryForm :initial-product="prefillProduct" />
      </div>
    </div>
  </div>
</template>
