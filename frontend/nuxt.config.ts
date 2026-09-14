// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  css: ['~/assets/css/main.css'],

  modules: ['@nuxtjs/i18n', '@nuxtjs/sitemap'],

  vite: {
    plugins: [tailwindcss()],
  },

  // 站点信息（sitemap 与 SEO 使用）—— 上线前替换为真实域名
  site: {
    url: 'https://dawnhandicrafts.example.com',
    name: 'Dawn Handicrafts',
  },

  i18n: {
    strategy: 'prefix_except_default',
    defaultLocale: 'en',
    langDir: 'locales',
    locales: [
      { code: 'en', language: 'en-US', name: 'English', file: 'en.json' },
      { code: 'zh', language: 'zh-CN', name: '中文', file: 'zh.json' },
    ],
  },
})
