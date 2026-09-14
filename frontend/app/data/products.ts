import type { Category, CategorySlug, Product } from '~/types/product'

// 占位产品数据（后续由后端/后台提供，此处先用占位内容跑通流程）

export const categories: Category[] = [
  {
    slug: 'baskets',
    name: { en: 'Flower Baskets', zh: '花篮' },
    description: {
      en: 'Woven baskets for flowers, storage and gifting.',
      zh: '用于插花、收纳与礼赠的编织花篮。',
    },
  },
  {
    slug: 'ceramics',
    name: { en: 'Ceramic Jars', zh: '陶瓷罐' },
    description: {
      en: 'Hand-glazed ceramic jars and vases.',
      zh: '手工上釉的陶瓷罐与花瓶。',
    },
  },
  {
    slug: 'other',
    name: { en: 'Other Crafts', zh: '其他工艺品' },
    description: {
      en: 'Other natural-material handicrafts.',
      zh: '其他天然材质的手工艺品。',
    },
  },
]

export const products: Product[] = [
  {
    id: 'p-001',
    slug: 'willow-flower-basket',
    category: 'baskets',
    name: { en: 'Woven Willow Flower Basket', zh: '柳编花篮' },
    summary: {
      en: 'Lightweight willow basket with a natural finish, ideal for floral arrangements.',
      zh: '轻巧的柳编花篮，天然色泽，适合插花装饰。',
    },
    description: {
      en: 'Hand-woven from sustainably harvested willow, this basket pairs a natural finish with a sturdy frame. Suitable for fresh flowers, dried arrangements, or retail display.',
      zh: '采用可持续采收的柳条手工编织，天然色泽搭配坚固框架。适用于鲜花、干花或陈列展示。',
    },
    material: { en: 'Willow', zh: '柳条' },
    sizes: ['S (20cm)', 'M (28cm)', 'L (36cm)'],
    moq: 200,
    featured: true,
    tone: 80,
  },
  {
    id: 'p-002',
    slug: 'rattan-storage-basket',
    category: 'baskets',
    name: { en: 'Rattan Storage Basket', zh: '藤编收纳篮' },
    summary: {
      en: 'Durable rattan basket for home storage with a warm honey tone.',
      zh: '耐用的藤编收纳篮，温暖蜂蜜色泽。',
    },
    description: {
      en: 'Tightly woven from premium rattan, this storage basket is durable yet lightweight. A versatile piece for laundry, blankets, or general household storage.',
      zh: '采用优质藤材紧密编织，耐用且轻便。适合衣物、毛毯或日常家居收纳。',
    },
    material: { en: 'Rattan', zh: '藤' },
    sizes: ['30L', '45L', '60L'],
    moq: 300,
    featured: true,
    tone: 95,
  },
  {
    id: 'p-003',
    slug: 'seagrass-picnic-basket',
    category: 'baskets',
    name: { en: 'Seagrass Picnic Basket', zh: '海草野餐篮' },
    summary: {
      en: 'Classic seagrass picnic basket with lid and carry handles.',
      zh: '经典海草野餐篮，带盖与提手。',
    },
    description: {
      en: 'A classic lidded picnic basket woven from natural seagrass. Includes sturdy handles and a woven lid, perfect for outdoor dining and gifting.',
      zh: '经典带盖野餐篮，天然海草编织，配坚固提手与编织盖，适合户外野餐与送礼。',
    },
    material: { en: 'Seagrass', zh: '海草' },
    sizes: ['Standard', 'Large'],
    moq: 250,
    featured: false,
    tone: 120,
  },
  {
    id: 'p-004',
    slug: 'bamboo-fruit-basket',
    category: 'baskets',
    name: { en: 'Bamboo Fruit Basket', zh: '竹编果篮' },
    summary: {
      en: 'Open bamboo basket for fruit display with a clean, light look.',
      zh: '开放式竹编果篮，清新浅色外观。',
    },
    description: {
      en: 'An open-top bamboo basket designed for fruit display. Light in colour and weight, it brings a clean, natural accent to kitchens and shops.',
      zh: '顶部开放式竹编果篮，浅色轻便，为厨房与门店增添清新自然气息。',
    },
    material: { en: 'Bamboo', zh: '竹' },
    sizes: ['25cm', '32cm'],
    moq: 400,
    featured: false,
    tone: 140,
  },
  {
    id: 'p-005',
    slug: 'glazed-ceramic-vase',
    category: 'ceramics',
    name: { en: 'Glazed Ceramic Vase', zh: '釉面陶瓷花瓶' },
    summary: {
      en: 'Hand-thrown ceramic vase with a soft reactive glaze.',
      zh: '手工拉坯陶瓷花瓶，柔和的反应釉。',
    },
    description: {
      en: 'Each vase is hand-thrown and finished with a reactive glaze, giving every piece a unique, one-of-a-kind surface. Available in muted, natural tones.',
      zh: '每只花瓶均手工拉坯并以反应釉收尾，釉面独一无二。提供柔和自然色调。',
    },
    material: { en: 'Ceramic', zh: '陶瓷' },
    sizes: ['H 18cm', 'H 25cm', 'H 32cm'],
    moq: 150,
    featured: true,
    tone: 30,
  },
  {
    id: 'p-006',
    slug: 'terracotta-storage-jar',
    category: 'ceramics',
    name: { en: 'Terracotta Storage Jar', zh: '陶土收纳罐' },
    summary: {
      en: 'Rustic terracotta jar with lid, for kitchen storage.',
      zh: '质朴陶土带盖罐，用于厨房收纳。',
    },
    description: {
      en: 'A rustic, unglazed terracotta jar with a fitted lid. Ideal for storing tea, spices, or dry goods with a warm, earthy presence.',
      zh: '质朴无釉陶土带盖罐，适合存放茶叶、香料或干货，温暖质朴。',
    },
    material: { en: 'Terracotta', zh: '陶土' },
    sizes: ['500ml', '1L', '2L'],
    moq: 200,
    featured: false,
    tone: 45,
  },
  {
    id: 'p-007',
    slug: 'stoneware-planter-pot',
    category: 'ceramics',
    name: { en: 'Stoneware Planter Pot', zh: '炻器花盆' },
    summary: {
      en: 'Minimal stoneware planter with drainage hole.',
      zh: '极简炻器花盆，带排水孔。',
    },
    description: {
      en: 'A minimal stoneware planter with a matte finish and drainage hole, made for indoor plants and modern interiors.',
      zh: '极简炻器花盆，哑光质地，带排水孔，适合室内植物与现代家居。',
    },
    material: { en: 'Stoneware', zh: '炻器' },
    sizes: ['12cm', '16cm', '20cm'],
    moq: 300,
    featured: true,
    tone: 60,
  },
  {
    id: 'p-008',
    slug: 'ceramic-table-lamp-base',
    category: 'other',
    name: { en: 'Ceramic Table Lamp Base', zh: '陶瓷台灯底座' },
    summary: {
      en: 'Handmade ceramic lamp base, a warm accent for any room.',
      zh: '手工陶瓷灯座，为空间增添温暖。',
    },
    description: {
      en: 'A handmade ceramic lamp base with a textured, natural finish. Pairs with standard lamp fittings for a warm, artisanal lighting accent.',
      zh: '手工陶瓷灯座，纹理自然。搭配标准灯头，营造温暖手作光影。',
    },
    material: { en: 'Ceramic', zh: '陶瓷' },
    sizes: ['H 20cm', 'H 28cm'],
    moq: 100,
    featured: false,
    tone: 90,
  },
]

export function categoryBySlug(slug: CategorySlug): Category {
  return categories.find((c) => c.slug === slug) ?? categories[0]
}
