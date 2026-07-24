import { defineStore } from 'pinia'
import client from '../api/client'

export const useCustodyStore = defineStore('custody', {
  state: () => ({
    events: [],
    loading: false,
  }),
  actions: {
    async fetchEvents() {
      this.loading = true
      try {
        const response = await client.get('/custody/events/')
        this.events = response.data
      } catch (err) {
        console.error('Failed to fetch custody events', err)
      } finally {
        this.loading = false
      }
    }
  }
})
