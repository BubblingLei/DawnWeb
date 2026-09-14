<script setup lang="ts">
import { categories, products } from '~/data/products'
import type { LocalizedText, SortKey } from '~/types/product'

const { t } = useI18n()
const { lt } = useLocalized()
const route = useRoute()
const router = useRouter()

// 单一筛选状态，从 URL 初始化（URL 即状态，可分享/可回退）
const filters = reactive({
  category: (route.query.category as string) || 'all',
  material: (route.query.material as string) || 'all',
  q: (route.query.q as string) || '',
  sort: (route.query.sort as SortKey) || 'featured',
})

// 状态 → URL 同步
watch(
  () => ({ ...filters }),
  (val) => {
    const query: Record<string, string> = {}
    if (val.category !== 'all') query.category = val.category
    if (val.material !== 'all') query.material = val.material
    if (val.q) query.q = val.q
    if (val.sort !== 'featured') query.sort = val.sort
    router.replace({ query })
  },
)

// 可选材质列表（去重，按英文 key 稳定排序）
const materials = computed(() => {
  const map = new Map<string, LocalizedText>()
  for (const p of products) map.set(p.material.en, p.material)
  return [...map.entries()].map(([key, label]) => ({ key, label }))
})

const filtered = computed(() => {
  let list = [...products]

  if (filters.category !== 'all') {
    list = list.filter((p) => p.category === filters.category)
  }
  if (filters.material !== 'all') {
    list = list.filter((p) => p.material.en === filters.material)
  }
  const q = filters.q.trim().toLowerCase()
  if (q) {
    list = list.filter(
      (p) =>
        p.name.en.toLowerCase().includes(q) ||
        p.name.zh.includes(q) ||
        p.summary.en.toLowerCase().includes(q),
    )
  }

  switch (filters.sort) {
    case 'name':
      list.sort((a, b) => lt(a.name).localeCompare(lt(b.name)))
      break
    case 'moq-asc':
      list.sort((a, b) => a.moq - b.moq)
      break
    case 'moq-desc':
      list.sort((a, b) => b.moq - a.moq)
      break
    default:
      list.sort((a, b) => Number(b.featured) - Number(a.featured))
  }

  return list
})

const activeCategoryName = computed(() => {
  if (filters.category === 'all') return t('products.all')
  const c = categories.find((c) => c.slug === filters.category)
  return c ? lt(c.name) : ''
})

function clearFilters() {
  filters.category = 'all'
  filters.material = 'all'
  filters.q = ''
  filters.sort = 'featured'
}

useSeoMeta({
  title: () => `${t('nav.products')} — ${t('brand')}`,
  description: () => t('products.metaDescription'),
})
</script>

<template>
  <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
    <h1 class="text-h2 text-text">{{ t('products.title') }}</h1>
    <p class="mt-3 max-w-2xl text-text-muted">{{ t('products.subtitle') }}</p>

    <!-- 顶部工具条：搜索 + 排序 -->
    <div class="mt-10 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
      <div class="relative w-full sm:max-w-xs">
        <input
          v-model="filters.q"
          type="search"
          :placeholder="t('products.searchPlaceholder')"
          class="w-full rounded-full border border-border bg-white px-5 py-2.5 text-sm outline-none transition-colors duration-fast focus:border-accent"
        />
      </div>

      <div class="flex items-center gap-3">
        <label class="text-sm text-text-muted">{{ t('products.sortBy') }}</label>
        <select
          v-model="filters.sort"
          class="rounded-full border border-border bg-white px-4 py-2.5 text-sm outline-none transition-colors duration-fast focus:border-accent"
        >
          <option value="featured">{{ t('products.sort.featured') }}</option>
          <option value="name">{{ t('products.sort.name') }}</option>
          <option value="moq-asc">{{ t('products.sort.moqAsc') }}</option>
          <option value="moq-desc">{{ t('products.sort.moqDesc') }}</option>
        </select>
      </div>
    </div>

    <div class="mt-10 grid gap-10 lg:grid-cols-[220px_1fr]">
      <!-- 侧边栏：分类 + 材质 -->
      <aside class="lg:sticky lg:top-24 lg:self-start">
        <div class="space-y-8">
          <div>
            <p class="mb-3 text-xs uppercase tracking-wider text-text-muted">
              {{ t('products.filter.category') }}
            </p>
            <div class="flex flex-col gap-1">
              <button
                class="rounded-lg px-3 py-2 text-left text-sm transition-colors duration-fast"
                :class="filters.category === 'all' ? 'bg-accent-strong text-white' : 'text-text-muted hover:bg-surface-muted'"
                @click="filters.category = 'all'"
              >
                {{ t('products.all') }}
              </button>
              <button
                v-for="c in categories"
                :key="c.slug"
                class="rounded-lg px-3 py-2 text-left text-sm transition-colors duration-fast"
                :class="filters.category === c.slug ? 'bg-accent-strong text-white' : 'text-text-muted hover:bg-surface-muted'"
                @click="filters.category = c.slug"
              >
                {{ lt(c.name) }}
              </button>
            </div>
          </div>

          <div>
            <p class="mb-3 text-xs uppercase tracking-wider text-text-muted">
              {{ t('products.filter.material') }}
            </p>
            <div class="flex flex-col gap-1">
              <button
                v-for="m in materials"
                :key="m.key"
                class="rounded-lg px-3 py-2 text-left text-sm transition-colors duration-fast"
                :class="filters.material === m.key ? 'bg-accent-strong text-white' : 'text-text-muted hover:bg-surface-muted'"
                @click="filters.material = filters.material === m.key ? 'all' : m.key"
              >
                {{ lt(m.label) }}
              </button>
            </div>
          </div>
        </div>
      </aside>

      <!-- 结果区 -->
      <div>
        <p class="mb-6 text-sm text-text-muted">
          {{ activeCategoryName }}
          <span class="text-accent">· {{ filtered.length }}</span>
          {{ t('products.results') }}
        </p>

        <div v-if="filtered.length" class="grid gap-6 sm:grid-cols-2 xl:grid-cols-3">
          <ProductCard
            v-for="product in filtered"
            :key="product.id"
            :product="product"
          />
        </div>

        <div v-else class="rounded-2xl border border-border p-12 text-center">
          <p class="text-text-muted">{{ t('products.empty') }}</p>
          <button
            class="mt-4 text-sm text-accent-strong hover:underline"
            @click="clearFilters"
          >
            {{ t('products.clearFilters') }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
