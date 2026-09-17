<script setup lang="ts">
const { state, close } = useInquiryModal()
const { t } = useI18n()

function onKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape') close()
}

watch(
  () => state.value.open,
  (open) => {
    if (import.meta.client) document.body.style.overflow = open ? 'hidden' : ''
  },
)

onMounted(() => window.addEventListener('keydown', onKeydown))
onBeforeUnmount(() => window.removeEventListener('keydown', onKeydown))
</script>

<template>
  <Teleport to="body">
    <div
      v-if="state.open"
      class="fixed inset-0 z-50 flex items-center justify-center p-4"
    >
      <div class="absolute inset-0 bg-black/50" @click="close" />

      <div
        role="dialog"
        aria-modal="true"
        :aria-label="t('cta.inquiry')"
        class="relative z-10 max-h-[90vh] w-full max-w-lg overflow-y-auto rounded-2xl bg-white p-6 shadow-2xl sm:p-8"
      >
        <button
          type="button"
          class="absolute right-4 top-4 flex h-8 w-8 items-center justify-center rounded-full text-text-muted transition-colors duration-fast hover:bg-surface-muted hover:text-text"
          :aria-label="t('contact.form.close')"
          @click="close"
        >
          ✕
        </button>

        <InquiryForm :initial-type="state.type" :initial-product="state.product" />
      </div>
    </div>
  </Teleport>
</template>
