import { defineStore } from 'pinia'

export const useWalletStore = defineStore('wallet', {
  state: () => ({
    address: null,
    isConnected: false,
  }),
  actions: {
    connectWallet() {
      // Connect BCH wallet logic
    }
  }
})
