import type { LocalizedText } from '~/types/product'

/**
 * 返回按当前语言取文本的辅助函数。
 * 用法：const { lt } = useLocalized(); lt(product.name)
 */
export function useLocalized() {
  const { locale } = useI18n()
  const lt = (text: LocalizedText): string => (locale.value === 'zh' ? text.zh : text.en)
  return { lt }
}
