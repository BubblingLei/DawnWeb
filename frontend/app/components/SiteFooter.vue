<script setup lang="ts">
const { t } = useI18n()

const links = [
  { key: 'home', to: '/' },
  { key: 'products', to: '/products' },
  { key: 'custom', to: '/custom' },
  { key: 'about', to: '/about' },
  { key: 'contact', to: '/contact' },
] as const
</script>

<template>
  <footer class="border-t border-border bg-surface-muted">
    <div class="mx-auto max-w-6xl px-6 py-14">
      <div class="grid gap-10 md:grid-cols-3">
        <div>
          <p class="font-display text-lg text-text">{{ t('brand') }}</p>
          <p class="mt-3 max-w-xs text-sm text-text-muted">
            {{ t('footer.tagline') }}
          </p>
        </div>

        <nav class="flex flex-col gap-2 text-sm">
          <p class="mb-1 text-xs uppercase tracking-wider text-text-muted">
            {{ t('footer.quickLinks') }}
          </p>
          <NuxtLinkLocale
            v-for="link in links"
            :key="link.key"
            :to="link.to"
            class="text-text-muted transition-colors duration-fast hover:text-accent-strong"
          >
            {{ t(`nav.${link.key}`) }}
          </NuxtLinkLocale>
        </nav>

        <div class="text-sm text-text-muted">
          <p class="mb-1 text-xs uppercase tracking-wider">
            {{ t('footer.contact') }}
          </p>
          <p>{{ t('contact.email') }}</p>
          <p>{{ t('contact.phone') }}</p>
          <p>{{ t('contact.address') }}</p>
        </div>
      </div>

      <p class="mt-12 border-t border-border pt-6 text-xs text-text-muted">
        © {{ new Date().getFullYear() }} {{ t('brand') }}. {{ t('footer.rights') }}
      </p>
    </div>
  </footer>
</template>
