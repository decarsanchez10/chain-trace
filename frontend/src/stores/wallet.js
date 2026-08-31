import { defineStore } from 'pinia'

export const useWalletStore = defineStore('wallet', {
  state: () => ({
    address: null,
    isConnected: false,
  }),
  actions: {
    async connectWallet() {
      // Connect BCH wallet logic for Paytaca
      if (typeof window.paytaca !== 'undefined') {
        try {
          // Paytaca extension API request
          const accounts = await window.paytaca.requestAccount();
          if (accounts) {
            this.address = accounts;
            this.isConnected = true;
          }
        } catch (error) {
          console.error("Failed to connect Paytaca:", error);
          alert("Failed to connect Paytaca wallet.");
        }
      } else {
        alert("Paytaca extension not found. Please install the Paytaca wallet extension to connect.");
      }
    },
    disconnectWallet() {
      this.address = null;
      this.isConnected = false;
    }
  }
})
