<template>
  <div class="flex min-h-screen flex-col bg-surface text-text">
    <SiteHeader />
    <main class="flex-1">
      <slot />
    </main>
    <SiteFooter />
    <InquiryModal />
  </div>
</template>
