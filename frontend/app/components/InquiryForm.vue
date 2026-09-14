<script setup lang="ts">
const props = defineProps<{ initialProduct?: string }>()

const { t } = useI18n()

const form = reactive({
  name: '',
  email: '',
  country: '',
  product: props.initialProduct ?? '',
  message: '',
})

const errors = reactive<Record<string, string>>({})
const submitted = ref(false)
const submitting = ref(false)

function validate(): boolean {
  errors.name = form.name.trim() ? '' : t('contact.form.errors.name')
  errors.email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())
    ? ''
    : t('contact.form.errors.email')
  errors.message = form.message.trim() ? '' : t('contact.form.errors.message')
  return !errors.name && !errors.email && !errors.message
}

async function onSubmit() {
  if (!validate()) return

  submitting.value = true
  // TODO(Phase 2): 提交到后端 POST /api/inquiries。当前为占位，前端先跑通流程。
  await new Promise((resolve) => setTimeout(resolve, 600))
  submitting.value = false
  submitted.value = true
}

function resetForm() {
  form.name = ''
  form.email = ''
  form.country = ''
  form.product = props.initialProduct ?? ''
  form.message = ''
  submitted.value = false
}
</script>

<template>
  <div>
    <form
      v-if="!submitted"
      class="space-y-5"
      novalidate
      @submit.prevent="onSubmit"
    >
      <div class="grid gap-5 sm:grid-cols-2">
        <div>
          <label class="mb-1.5 block text-sm text-text-muted">
            {{ t('contact.form.name') }} *
          </label>
          <input
            v-model="form.name"
            type="text"
            class="w-full rounded-xl border border-border bg-white px-4 py-3 text-sm outline-none transition-colors duration-fast focus:border-accent"
            :class="errors.name ? 'border-red-400' : ''"
          />
          <p v-if="errors.name" class="mt-1 text-xs text-red-500">{{ errors.name }}</p>
        </div>
        <div>
          <label class="mb-1.5 block text-sm text-text-muted">
            {{ t('contact.form.email') }} *
          </label>
          <input
            v-model="form.email"
            type="email"
            class="w-full rounded-xl border border-border bg-white px-4 py-3 text-sm outline-none transition-colors duration-fast focus:border-accent"
            :class="errors.email ? 'border-red-400' : ''"
          />
          <p v-if="errors.email" class="mt-1 text-xs text-red-500">{{ errors.email }}</p>
        </div>
      </div>

      <div class="grid gap-5 sm:grid-cols-2">
        <div>
          <label class="mb-1.5 block text-sm text-text-muted">
            {{ t('contact.form.country') }}
          </label>
          <input
            v-model="form.country"
            type="text"
            class="w-full rounded-xl border border-border bg-white px-4 py-3 text-sm outline-none transition-colors duration-fast focus:border-accent"
          />
        </div>
        <div>
          <label class="mb-1.5 block text-sm text-text-muted">
            {{ t('contact.form.product') }}
          </label>
          <input
            v-model="form.product"
            type="text"
            class="w-full rounded-xl border border-border bg-white px-4 py-3 text-sm outline-none transition-colors duration-fast focus:border-accent"
          />
        </div>
      </div>

      <div>
        <label class="mb-1.5 block text-sm text-text-muted">
          {{ t('contact.form.message') }} *
        </label>
        <textarea
          v-model="form.message"
          rows="5"
          class="w-full rounded-xl border border-border bg-white px-4 py-3 text-sm outline-none transition-colors duration-fast focus:border-accent"
          :class="errors.message ? 'border-red-400' : ''"
        />
        <p v-if="errors.message" class="mt-1 text-xs text-red-500">{{ errors.message }}</p>
      </div>

      <button
        type="submit"
        :disabled="submitting"
        class="rounded-full bg-accent-strong px-8 py-3 text-sm font-semibold text-white transition-transform duration-fast hover:scale-[1.03] disabled:opacity-60"
      >
        {{ submitting ? t('contact.form.submitting') : t('contact.form.submit') }}
      </button>
    </form>

    <div
      v-else
      class="rounded-2xl border border-accent/30 bg-accent/10 p-8 text-center"
    >
      <p class="text-xl font-semibold text-accent-strong">
        {{ t('contact.form.successTitle') }}
      </p>
      <p class="mt-2 text-text-muted">{{ t('contact.form.successMessage') }}</p>
      <button
        class="mt-5 text-sm text-accent-strong hover:underline"
        @click="resetForm"
      >
        {{ t('contact.form.again') }}
      </button>
    </div>
  </div>
</template>
