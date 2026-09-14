// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite'

// 站点公开域名：本地开发用 localhost，上线时通过 NUXT_PUBLIC_SITE_URL 覆盖
const SITE_URL = process.env.NUXT_PUBLIC_SITE_URL || 'http://localhost:3000'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  css: ['~/assets/css/main.css'],

  modules: ['@nuxtjs/i18n', '@nuxtjs/sitemap'],

  vite: {
    plugins: [tailwindcss()],
  },

  // 站点信息（sitemap 与 SEO 使用）
  site: {
    url: SITE_URL,
    name: 'Dawn Handicrafts',
  },

  i18n: {
    baseUrl: SITE_URL,
    strategy: 'prefix_except_default',
    defaultLocale: 'en',
    langDir: 'locales',
    locales: [
      { code: 'en', language: 'en-US', name: 'English', file: 'en.json' },
      { code: 'zh', language: 'zh-CN', name: '中文', file: 'zh.json' },
    ],
  },
})
