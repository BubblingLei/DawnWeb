<script setup lang="ts">
import type { CategorySlug } from '~/types/product'

const props = defineProps<{
  tone: number
  category: CategorySlug
}>()

// 各分类的简单剪影路径（占位用，之后替换为真实产品图）
const silhouettes: Record<CategorySlug, string> = {
  baskets: 'M70 150 h60 l-8 -20 h8 l-10 -18 h-40 l-10 18 h8 z',
  ceramics: 'M82 70 h36 l-6 18 c14 8 16 26 10 44 l-44 0 c-6 -18 -4 -36 10 -44 z',
  other: 'M78 74 h44 l-5 16 c16 10 18 30 10 48 l-54 0 c-8 -18 -6 -38 10 -48 z',
}
</script>

<template>
  <div
    class="relative aspect-[4/5] w-full overflow-hidden"
    :style="{ backgroundColor: `hsl(${props.tone} 28% 86%)` }"
  >
    <!-- 柔和高光 -->
    <div
      class="absolute inset-0"
      :style="{
        background: `radial-gradient(120% 80% at 30% 20%, hsl(${props.tone} 32% 92%) 0%, hsl(${props.tone} 26% 80%) 100%)`,
      }"
    />
    <!-- 剪影 -->
    <svg
      viewBox="0 0 200 200"
      class="absolute inset-0 m-auto h-3/5 w-3/5 opacity-25"
      :style="{ fill: `hsl(${props.tone} 30% 55%)` }"
      aria-hidden="true"
    >
      <path :d="silhouettes[props.category]" />
    </svg>
  </div>
</template>
