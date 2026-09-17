export type InquiryType = 'inquiry' | 'custom'

export interface InquiryModalState {
  open: boolean
  type: InquiryType
  product: string
}

/**
 * 全站共用的询盘/定制弹窗状态。
 * 任意页面调用 open(type, product) 打开，InquiryModal 挂载在 default 布局里读取。
 */
export function useInquiryModal() {
  const state = useState<InquiryModalState>('inquiry-modal', () => ({
    open: false,
    type: 'inquiry',
    product: '',
  }))

  function open(type: InquiryType = 'inquiry', product = '') {
    state.value = { open: true, type, product }
  }

  function close() {
    state.value.open = false
  }

  return { state, open, close }
}
