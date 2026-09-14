// 产品与分类的共享类型定义

export interface LocalizedText {
  en: string
  zh: string
}

export type CategorySlug = 'baskets' | 'ceramics' | 'other'

export interface Category {
  slug: CategorySlug
  name: LocalizedText
  description: LocalizedText
}

export interface Product {
  id: string
  slug: string
  category: CategorySlug
  name: LocalizedText
  summary: LocalizedText
  description: LocalizedText
  material: LocalizedText
  sizes: string[]
  /** 起订量（Minimum Order Quantity） */
  moq: number
  featured: boolean
  /** 占位图使用的柔和色相（HSL） */
  tone: number
}

export type SortKey = 'featured' | 'name' | 'moq-asc' | 'moq-desc'
