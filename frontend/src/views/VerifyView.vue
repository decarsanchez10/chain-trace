<template>
  <div class="verify-page">

    <!-- HEADER -->
    <header class="verify-header">
      <div class="brand">
        <div class="logo-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
            <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
            <line x1="12" y1="22.08" x2="12" y2="12"/>
          </svg>
        </div>
        <div class="brand-text">
          <span class="brand-name">CHAINTRACE</span>
          <span class="brand-tagline">TRACE. VERIFY. TRUST.</span>
        </div>
      </div>

      <nav class="header-nav">
        <router-link to="/dashboard">Dashboard</router-link>
        <router-link to="/verify" class="nav-active">Verify</router-link>
        <router-link to="/login">Login</router-link>
      </nav>

      <div class="header-actions">
        <button class="icon-btn" @click="toggleTheme" title="Toggle theme">
          <svg v-if="darkMode" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
          <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
        <button class="btn-wallet">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 3H5a3 3 0 0 0-3 3v1h18V6a3 3 0 0 0-3-3z"/><circle cx="17" cy="14" r="1.5" fill="currentColor"/></svg>
          Connect Wallet
        </button>
      </div>
    </header>

    <!-- HERO SECTION -->
    <section class="hero-section">
      <div class="hero-text">
        <p class="hero-pre">BLOCKCHAIN VERIFICATION</p>
        <h1 class="hero-title">
          PUBLIC VERIFICATION<br>
          <span class="hero-accent">INTERFACE</span>
        </h1>
        <p class="hero-subtitle">Verify payload hashes against Bitcoin Cash (BCH) on-chain data.</p>

        <div class="trust-indicators">
          <div class="trust-item">
            <div class="trust-icon">🔒</div>
            <div>
              <div class="trust-label">IMMUTABLE</div>
              <div class="trust-desc">Anchored on Bitcoin Cash</div>
            </div>
          </div>
          <div class="trust-item">
            <div class="trust-icon">🌐</div>
            <div>
              <div class="trust-label">TRANSPARENT</div>
              <div class="trust-desc">Anyone can verify the records</div>
            </div>
          </div>
          <div class="trust-item">
            <div class="trust-icon">⚡</div>
            <div>
              <div class="trust-label">TRUSTLESS</div>
              <div class="trust-desc">No central authority required</div>
            </div>
          </div>
        </div>
      </div>

      <div class="hero-visual">
        <img src="/img/bch_cube_hologram.png" alt="BCH Blockchain Cube" class="hero-image" />
      </div>
    </section>

    <!-- MAIN CONTENT -->
    <section class="main-content">

      <!-- LEFT: VERIFICATION PANEL -->
      <div class="verification-panel">
        <div class="panel-header">
          <h2>Verify Payload Hash</h2>
          <p>Enter a transaction ID or paste the payload hash to verify its existence on the Bitcoin Cash blockchain.</p>
        </div>

        <!-- TABS -->
        <div class="tabs">
          <button :class="['tab-btn', activeTab === 'txid' ? 'tab-active' : '']" @click="switchTab('txid')">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>
            Transaction ID
          </button>
          <button :class="['tab-btn', activeTab === 'hash' ? 'tab-active' : '']" @click="switchTab('hash')">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/></svg>
            Payload Hash
          </button>
        </div>

        <!-- TXID TAB -->
        <div v-if="activeTab === 'txid'" class="tab-content">
          <div class="input-group">
            <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
            <input
              v-model="txid"
              type="text"
              class="verify-input"
              placeholder="Enter Bitcoin Cash transaction ID (txid)..."
              @keyup.enter="verifyNow"
            />
          </div>
          <button class="btn-verify" @click="verifyNow" :disabled="isLoading">
            <span v-if="isLoading" class="spinner"></span>
            <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            {{ isLoading ? 'VERIFYING...' : 'VERIFY NOW' }}
          </button>
          <div class="example-txid">
            <span class="example-label">Example TXID:</span>
            <code class="txid-badge">{{ exampleTxid }}<button class="copy-btn" @click="copyTxid" title="Copy to clipboard">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            </button></code>
          </div>
        </div>

        <!-- PAYLOAD HASH TAB -->
        <div v-if="activeTab === 'hash'" class="tab-content">
          <div class="input-group">
            <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/></svg>
            <input
              v-model="payloadHash"
              type="text"
              class="verify-input"
              placeholder="Paste SHA-256 payload hash (64 hex characters)..."
              @keyup.enter="verifyNow"
            />
          </div>
          <button class="btn-verify" @click="verifyNow" :disabled="isLoading">
            <span v-if="isLoading" class="spinner"></span>
            <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            {{ isLoading ? 'VERIFYING...' : 'VERIFY NOW' }}
          </button>
          <div class="example-txid">
            <span class="example-label">Example SHA-256 Hash:</span>
            <code class="txid-badge">{{ exampleHash }}<button class="copy-btn" @click="copyHash" title="Copy to clipboard">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            </button></code>
          </div>
        </div>

        <!-- RESULT -->
        <div v-if="verificationResult === 'success'" class="result-card result-success">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          <div>
            <div class="result-title">Verification Successful</div>
            <div class="result-msg">Hash matched on-chain. This record is authentic and has not been tampered with.</div>
          </div>
        </div>

        <div v-if="verificationResult === 'fail'" class="result-card result-fail">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>
          <div>
            <div class="result-title">Verification Failed</div>
            <div class="result-msg">Hash mismatch or record not found. The data may have been tampered with or does not exist on-chain.</div>
          </div>
        </div>
      </div>

      <!-- RIGHT: HOW IT WORKS -->
      <div class="how-it-works-panel">
        <h3 class="how-title">HOW IT WORKS</h3>
        <div class="steps-list">
          <div v-for="(step, i) in steps" :key="i" class="step-item">
            <div class="step-number">{{ i + 1 }}</div>
            <div class="step-connector" v-if="i < steps.length - 1"></div>
            <div class="step-body">
              <div class="step-title">{{ step.title }}</div>
              <div class="step-desc">{{ step.desc }}</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- RECENT VERIFICATIONS -->
    <section class="recent-section">
      <div class="recent-header">
        <h2>Recent Verifications</h2>
        <button class="btn-clear" @click="clearHistory" v-if="recentVerifications.length">Clear History</button>
      </div>

      <div v-if="recentVerifications.length" class="table-wrapper">
        <table class="verif-table">
          <thead>
            <tr>
              <th>TXID</th>
              <th>Type</th>
              <th>Block Height</th>
              <th>Status</th>
              <th>Verified At</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in recentVerifications" :key="row.txid">
              <td>
                <a :href="`https://chipnet.imaginary.cash/tx/${row.txid}`" target="_blank" class="txid-link">
                  {{ row.txid.substring(0, 10) + '...' + row.txid.slice(-6) }}
                </a>
              </td>
              <td><span class="badge badge-type">Transaction</span></td>
              <td class="block-height">{{ row.blockHeight.toLocaleString() }}</td>
              <td><span :class="['badge', row.status === 'Verified' ? 'badge-verified' : 'badge-failed']">{{ row.status }}</span></td>
              <td class="verified-at">{{ row.verifiedAt }}</td>
              <td>
                <button class="btn-view" @click="viewDetails(row)">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                  View Details
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-else class="empty-state">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <p>No verifications yet.</p>
        <span>Your verified transactions will appear here.</span>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="verify-footer">
      <div class="footer-left">
        <div class="footer-brand">
          <div class="logo-icon small">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
            </svg>
          </div>
          <span class="footer-name">CHAINTRACE</span>
        </div>
        <p class="footer-copy">© 2025 ChainTrace Capstone Project | Eastern Samar State University – College of Engineering</p>
      </div>
      <div class="footer-icons">
        <a href="#" title="GitHub" class="footer-icon-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
        </a>
        <a href="#" title="Documentation" class="footer-icon-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        </a>
        <a href="mailto:chaintrace@essu.edu.ph" title="Contact" class="footer-icon-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        </a>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { gsap } from 'gsap'

const darkMode = ref(true)
const activeTab = ref('txid')
const txid = ref('')
const payloadHash = ref('')
const isLoading = ref(false)
const verificationResult = ref(null) // null | 'success' | 'fail'

const exampleTxid = '9f4e2a7c1b3d5f8e2a1c4b7d9e3f0a2c9f4e2a7c1b3da8f0'
const exampleHash = 'a3f5c8e2d1b4f7c9e2a3f5c8e2d1b4f7c9e2a3f5c8e292c0'

const steps = [
  { title: 'Enter TXID or payload hash', desc: 'Provide the transaction ID from the BCH blockchain or the SHA-256 payload hash.' },
  { title: 'Fetch on-chain data', desc: 'Retrieve the OP_RETURN data embedded in the Bitcoin Cash transaction.' },
  { title: 'Compare & verify', desc: 'Check whether the stored hash matches the on-chain record exactly.' },
  { title: 'View results', desc: 'Display verification result with full block details and timestamp.' },
]

const recentVerifications = ref([
  {
    txid: '9f4e2a7c1b3d5f8e2a1c4b7d9e3f0a2c9f4e2a7c1b3da8f0',
    blockHeight: 2756483,
    status: 'Verified',
    verifiedAt: 'May 24, 2025 · 2:45 PM',
  },
])

onMounted(() => {
  // Page load animations
  gsap.from('.verify-header', { y: -50, opacity: 0, duration: 0.8, ease: 'power3.out' })
  
  gsap.from('.hero-text .hero-pre', { x: -30, opacity: 0, duration: 0.6, delay: 0.2 })
  gsap.from('.hero-text .hero-title', { x: -40, opacity: 0, duration: 0.8, delay: 0.3, ease: 'power3.out' })
  gsap.from('.hero-text .hero-subtitle', { x: -30, opacity: 0, duration: 0.6, delay: 0.5 })
  
  gsap.from('.trust-item', { 
    scale: 0.9, 
    opacity: 0, 
    stagger: 0.1, 
    duration: 0.6, 
    delay: 0.6, 
    ease: 'back.out(1.5)' 
  })
  
  gsap.from('.hero-visual', { scale: 0.8, opacity: 0, duration: 1, delay: 0.4, ease: 'back.out(1.2)' })
  
  // Continuous hologram float animation
  gsap.to('.hero-image', {
    y: -15,
    duration: 3,
    repeat: -1,
    yoyo: true,
    ease: 'power1.inOut'
  })
  
  gsap.from('.verification-panel', { y: 40, opacity: 0, duration: 0.8, delay: 0.7, ease: 'power3.out' })
  gsap.from('.how-it-works-panel', { y: 40, opacity: 0, duration: 0.8, delay: 0.85, ease: 'power3.out' })
  
  gsap.from('.step-item', { 
    opacity: 0, 
    x: 20, 
    stagger: 0.1, 
    duration: 0.6, 
    delay: 1, 
    ease: 'power2.out' 
  })
  
  gsap.from('.recent-section', { opacity: 0, y: 30, duration: 0.8, delay: 1.1 })
})

function toggleTheme() {
  darkMode.value = !darkMode.value
}

function switchTab(tab) {
  activeTab.value = tab
  verificationResult.value = null
}

function copyTxid() {
  navigator.clipboard.writeText('9f4e2a7c1b3d5f8e2a1c4b7d9e3f0a2c9f4e2a7c1b3da8f0')
}

function copyHash() {
  navigator.clipboard.writeText('a3f5c8e2d1b4f7c9e2a3f5c8e2d1b4f7c9e2a3f5c8e292c0')
}

async function verifyNow() {
  const query = activeTab.value === 'txid' ? txid.value : payloadHash.value
  if (!query.trim()) return

  isLoading.value = true
  verificationResult.value = null

  // Simulate async verification call
  await new Promise(resolve => setTimeout(resolve, 1500))

  // Mock result: always success for demo
  const now = new Date()
  const dateStr = now.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
    + ' · ' + now.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true })

  verificationResult.value = 'success'
  recentVerifications.value.unshift({
    txid: query.length >= 16 ? query : query.padEnd(48, '0'),
    blockHeight: Math.floor(Math.random() * 200000) + 2700000,
    status: 'Verified',
    verifiedAt: dateStr,
  })

  isLoading.value = false

  // Animate the verification result card and table row
  await nextTick()
  gsap.from('.result-card', {
    scale: 0.9,
    opacity: 0,
    duration: 0.5,
    ease: 'back.out(1.5)'
  })

  gsap.from('.verif-table tbody tr:first-child', {
    backgroundColor: 'rgba(0, 210, 211, 0.25)',
    opacity: 0,
    y: -15,
    duration: 0.6,
    clearProps: 'backgroundColor'
  })
}

function clearHistory() {
  recentVerifications.value = []
}

function viewDetails(row) {
  window.open(`https://chipnet.imaginary.cash/tx/${row.txid}`, '_blank')
}
</script>

<style scoped>
/* ─── Base ─── */
.verify-page {
  background-color: #050a1a;
  color: #e0e6ed;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
}

/* ─── Header ─── */
.verify-header {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 4rem;
  background: rgba(5, 10, 26, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(0, 210, 211, 0.15);
  gap: 2rem;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-shrink: 0;
}

.logo-icon {
  width: 36px;
  height: 36px;
  color: #00d2d3;
  filter: drop-shadow(0 0 6px rgba(0, 210, 211, 0.5));
}

.logo-icon.small {
  width: 24px;
  height: 24px;
}

.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1;
}

.brand-name {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 2px;
  color: #fff;
}

.brand-tagline {
  font-size: 0.6rem;
  letter-spacing: 1px;
  color: #00d2d3;
  margin-top: 2px;
}

.header-nav {
  display: flex;
  gap: 2rem;
}

.header-nav a {
  color: #8892a4;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  transition: color 0.2s;
  padding-bottom: 4px;
  border-bottom: 2px solid transparent;
}

.header-nav a:hover {
  color: #fff;
}

.nav-active {
  color: #00d2d3 !important;
  border-bottom-color: #00d2d3 !important;
  text-shadow: 0 0 8px rgba(0, 210, 211, 0.4);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-shrink: 0;
}

.icon-btn {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #8892a4;
  width: 36px;
  height: 36px;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  padding: 6px;
}

.icon-btn svg { width: 100%; height: 100%; }

.icon-btn:hover {
  border-color: #00d2d3;
  color: #00d2d3;
}

.btn-wallet {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.25rem;
  background: rgba(0, 210, 211, 0.1);
  border: 1px solid rgba(0, 210, 211, 0.4);
  color: #00d2d3;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  transition: all 0.2s;
  font-family: inherit;
}

.btn-wallet svg { width: 16px; height: 16px; }

.btn-wallet:hover {
  background: rgba(0, 210, 211, 0.2);
  box-shadow: 0 0 12px rgba(0, 210, 211, 0.2);
}

/* ─── Hero ─── */
.hero-section {
  display: flex;
  align-items: center;
  padding: 5rem 4rem 3rem;
  gap: 3rem;
  background: radial-gradient(ellipse at 60% 40%, rgba(0, 210, 211, 0.08) 0%, transparent 60%);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.hero-text { flex: 1; }

.hero-pre {
  font-size: 0.75rem;
  letter-spacing: 3px;
  color: #00d2d3;
  margin-bottom: 1rem;
  font-weight: 600;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1.25rem;
  color: #fff;
  letter-spacing: -0.5px;
}

.hero-accent {
  color: #00d2d3;
  text-shadow: 0 0 20px rgba(0, 210, 211, 0.5);
}

.hero-subtitle {
  font-size: 1.1rem;
  color: #8892a4;
  max-width: 500px;
  line-height: 1.6;
  margin-bottom: 2.5rem;
}

.trust-indicators {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

.trust-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}

.trust-icon {
  font-size: 1.5rem;
  margin-top: 2px;
}

.trust-label {
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: #fff;
}

.trust-desc {
  font-size: 0.8rem;
  color: #8892a4;
  margin-top: 2px;
}

.hero-visual {
  flex: 0 0 400px;
  display: flex;
  justify-content: center;
}

.hero-image {
  max-width: 100%;
  border-radius: 12px;
  box-shadow: 0 0 60px rgba(0, 210, 211, 0.2);
  border: 1px solid rgba(0, 210, 211, 0.1);
  mask-image: linear-gradient(to bottom, black 70%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 70%, transparent 100%);
}

/* ─── Main Content ─── */
.main-content {
  display: flex;
  gap: 2rem;
  padding: 3rem 4rem;
  flex: 1;
  align-items: flex-start;
}

/* ─── Verification Panel ─── */
.verification-panel {
  flex: 3;
  background: rgba(10, 18, 40, 0.6);
  border: 1px solid rgba(0, 210, 211, 0.15);
  border-radius: 12px;
  padding: 2rem;
  backdrop-filter: blur(10px);
}

.panel-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.5rem;
}

.panel-header p {
  color: #8892a4;
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 1.75rem;
}

/* Tabs */
.tabs {
  display: flex;
  gap: 0;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 4px;
  margin-bottom: 1.5rem;
  background: rgba(0, 0, 0, 0.2);
}

.tab-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.65rem 1rem;
  background: transparent;
  border: none;
  color: #8892a4;
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  border-radius: 6px;
  transition: all 0.2s;
}

.tab-btn svg { width: 15px; height: 15px; }

.tab-btn:hover { color: #fff; }

.tab-active {
  background: rgba(0, 210, 211, 0.15) !important;
  color: #00d2d3 !important;
  box-shadow: 0 0 10px rgba(0, 210, 211, 0.1);
}

.tab-content { display: flex; flex-direction: column; gap: 1rem; }

.input-group {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 1rem;
  width: 18px;
  height: 18px;
  color: #8892a4;
  pointer-events: none;
}

.verify-input {
  width: 100%;
  padding: 0.85rem 1rem 0.85rem 3rem;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: #e0e6ed;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  transition: all 0.2s;
  outline: none;
}

.verify-input:focus {
  border-color: #00d2d3;
  box-shadow: 0 0 0 3px rgba(0, 210, 211, 0.1);
}

.verify-input::placeholder { color: #4a5568; }

.btn-verify {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.9rem;
  background: #00d2d3;
  color: #050a1a;
  border: none;
  border-radius: 8px;
  font-family: inherit;
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 0 20px rgba(0, 210, 211, 0.3);
}

.btn-verify svg { width: 18px; height: 18px; }

.btn-verify:hover:not(:disabled) {
  background: #00f0f0;
  box-shadow: 0 0 30px rgba(0, 210, 211, 0.5);
}

.btn-verify:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(5, 10, 26, 0.3);
  border-top-color: #050a1a;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
  display: inline-block;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.example-txid {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.example-label {
  font-size: 0.8rem;
  color: #4a5568;
}

.txid-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.3rem 0.75rem;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 6px;
  font-family: 'Courier New', monospace;
  font-size: 0.8rem;
  color: #00d2d3;
}

.copy-btn {
  background: transparent;
  border: none;
  color: #4a5568;
  cursor: pointer;
  padding: 0;
  display: flex;
  align-items: center;
  transition: color 0.2s;
}
.copy-btn:hover { color: #00d2d3; }
.copy-btn svg { width: 14px; height: 14px; }

/* Result Cards */
.result-card {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem 1.25rem;
  border-radius: 8px;
  margin-top: 0.5rem;
}

.result-card svg { width: 24px; height: 24px; flex-shrink: 0; margin-top: 2px; }

.result-success {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.3);
  color: #10b981;
}

.result-fail {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #ef4444;
}

.result-title {
  font-weight: 700;
  font-size: 1rem;
  margin-bottom: 0.25rem;
}

.result-msg {
  font-size: 0.85rem;
  opacity: 0.8;
  line-height: 1.5;
}

/* ─── How It Works ─── */
.how-it-works-panel {
  flex: 1;
  background: rgba(10, 18, 40, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 2rem 1.5rem;
}

.how-title {
  font-size: 0.8rem;
  letter-spacing: 2px;
  color: #00d2d3;
  margin-bottom: 2rem;
  font-weight: 700;
}

.steps-list {
  display: flex;
  flex-direction: column;
}

.step-item {
  display: grid;
  grid-template-columns: 36px auto 1fr;
  gap: 0 1rem;
  align-items: start;
  position: relative;
}

.step-number {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 2px solid #00d2d3;
  background: rgba(0, 210, 211, 0.1);
  color: #00d2d3;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 0.85rem;
  box-shadow: 0 0 10px rgba(0, 210, 211, 0.2);
  z-index: 1;
}

.step-connector {
  width: 2px;
  height: 100%;
  min-height: 40px;
  background: linear-gradient(to bottom, rgba(0, 210, 211, 0.4), rgba(0, 210, 211, 0.05));
  margin-left: 17px;
  margin-top: 0;
  grid-column: 1;
  grid-row: 2;
}

.step-body {
  grid-column: 3;
  padding-bottom: 2rem;
}

.step-title {
  font-size: 0.9rem;
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.4rem;
}

.step-desc {
  font-size: 0.8rem;
  color: #8892a4;
  line-height: 1.5;
}

/* ─── Recent Verifications ─── */
.recent-section {
  padding: 0 4rem 4rem;
}

.recent-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}

.recent-header h2 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #fff;
}

.btn-clear {
  padding: 0.4rem 0.9rem;
  background: transparent;
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #ef4444;
  border-radius: 6px;
  cursor: pointer;
  font-family: inherit;
  font-size: 0.8rem;
  transition: all 0.2s;
}

.btn-clear:hover {
  background: rgba(239, 68, 68, 0.1);
}

.table-wrapper {
  overflow-x: auto;
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.06);
}

.verif-table {
  width: 100%;
  border-collapse: collapse;
  background: rgba(10, 18, 40, 0.5);
}

.verif-table thead tr {
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.verif-table th {
  padding: 0.9rem 1.25rem;
  text-align: left;
  font-size: 0.7rem;
  letter-spacing: 1.5px;
  color: #4a5568;
  font-weight: 700;
  white-space: nowrap;
}

.verif-table td {
  padding: 1rem 1.25rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  font-size: 0.88rem;
}

.verif-table tr:last-child td { border-bottom: none; }

.verif-table tr:hover td {
  background: rgba(0, 210, 211, 0.04);
}

.txid-link {
  color: #00d2d3;
  font-family: 'Courier New', monospace;
  font-size: 0.85rem;
  text-decoration: none;
  transition: color 0.2s;
}

.txid-link:hover { text-decoration: underline; }

.badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.65rem;
  border-radius: 12px;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.badge-type {
  background: rgba(59, 130, 246, 0.12);
  color: #60a5fa;
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.badge-verified {
  background: rgba(16, 185, 129, 0.12);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.badge-failed {
  background: rgba(239, 68, 68, 0.12);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.block-height { font-variant-numeric: tabular-nums; color: #8892a4; }

.verified-at { color: #8892a4; font-size: 0.82rem; white-space: nowrap; }

.btn-view {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 0.85rem;
  background: transparent;
  border: 1px solid rgba(0, 210, 211, 0.3);
  color: #00d2d3;
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-view svg { width: 14px; height: 14px; }

.btn-view:hover {
  background: rgba(0, 210, 211, 0.1);
  box-shadow: 0 0 10px rgba(0, 210, 211, 0.15);
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
  background: rgba(10, 18, 40, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  color: #4a5568;
}

.empty-state svg {
  width: 56px;
  height: 56px;
  margin-bottom: 1.25rem;
  opacity: 0.3;
}

.empty-state p {
  font-size: 1rem;
  font-weight: 600;
  color: #8892a4;
  margin-bottom: 0.4rem;
}

.empty-state span {
  font-size: 0.85rem;
}

/* ─── Footer ─── */
.verify-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 2rem 4rem;
  background: rgba(3, 6, 18, 0.8);
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  flex-wrap: wrap;
  gap: 1.5rem;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.footer-name {
  font-weight: 800;
  letter-spacing: 2px;
  font-size: 1rem;
  color: #fff;
}

.footer-copy {
  font-size: 0.78rem;
  color: #4a5568;
}

.footer-icons {
  display: flex;
  gap: 0.75rem;
}

.footer-icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: #4a5568;
  text-decoration: none;
  transition: all 0.2s;
}

.footer-icon-btn svg { width: 17px; height: 17px; }

.footer-icon-btn:hover {
  border-color: #00d2d3;
  color: #00d2d3;
  box-shadow: 0 0 10px rgba(0, 210, 211, 0.1);
}

/* ─── Responsive ─── */
@media (max-width: 1100px) {
  .main-content { flex-direction: column; }
  .how-it-works-panel { min-width: 0; }
}

@media (max-width: 768px) {
  .verify-header { padding: 1rem 1.5rem; }
  .header-nav { display: none; }
  .hero-section { flex-direction: column; padding: 4rem 1.5rem 2rem; text-align: center; }
  .hero-visual { flex: 0 0 auto; width: 100%; }
  .trust-indicators { justify-content: center; }
  .main-content { padding: 2rem 1.5rem; }
  .recent-section { padding: 0 1.5rem 3rem; }
  .hero-title { font-size: 2.4rem; }
  .verify-footer { flex-direction: column; align-items: flex-start; padding: 2rem 1.5rem; }
}
</style>
