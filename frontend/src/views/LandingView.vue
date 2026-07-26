<template>
  <div class="landing-page">
    <!-- Animated Background Canvas -->
    <canvas class="bg-canvas" ref="bgCanvas"></canvas>

    <!-- ══════════════════════════════════════════════════
         1. HEADER / NAVIGATION
    ══════════════════════════════════════════════════ -->
    <header class="landing-header">
      <div class="brand">
        <!-- Glowing Geometric Cube Logo -->
        <div class="logo-icon" aria-hidden="true">
          <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <filter id="logo-glow">
                <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
                <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
            </defs>
            <g filter="url(#logo-glow)">
              <!-- Cube top face -->
              <polygon points="20,4 34,12 20,20 6,12" fill="rgba(0,212,212,0.15)" stroke="#00d4d4" stroke-width="1.2"/>
              <!-- Cube left face -->
              <polygon points="6,12 20,20 20,36 6,28" fill="rgba(0,212,212,0.08)" stroke="#00d4d4" stroke-width="1.2"/>
              <!-- Cube right face -->
              <polygon points="34,12 20,20 20,36 34,28" fill="rgba(0,100,255,0.12)" stroke="#00b4ff" stroke-width="1.2"/>
              <!-- Vertical center line -->
              <line x1="20" y1="4" x2="20" y2="20" stroke="#00d4d4" stroke-width="0.8" stroke-dasharray="2,2"/>
            </g>
          </svg>
        </div>
        <div class="brand-text">
          <span class="brand-name">CHAINTRACE</span>
          <span class="brand-tagline">TRACE. VERIFY. TRUST.</span>
        </div>
      </div>

      <nav class="landing-nav" aria-label="Main navigation">
        <a href="#home" class="nav-link active" id="nav-home">HOME</a>
        <a href="#overview" class="nav-link" id="nav-overview">OVERVIEW</a>
        <a href="#architecture" class="nav-link" id="nav-architecture">ARCHITECTURE</a>
        <a href="#features" class="nav-link" id="nav-features">FEATURES</a>
        <a href="#tech" class="nav-link" id="nav-tech">TECH STACK</a>
        <a href="#project" class="nav-link" id="nav-project">PROJECT</a>
        <a href="#contact" class="nav-link" id="nav-contact">CONTACT</a>
      </nav>
    </header>

    <!-- ══════════════════════════════════════════════════
         2. HERO SECTION
    ══════════════════════════════════════════════════ -->
    <section id="home" class="hero-section" aria-labelledby="hero-headline">
      <!-- Grid overlay texture -->
      <div class="hero-grid-overlay" aria-hidden="true"></div>

      <!-- ── LEFT COLUMN ── -->
      <div class="hero-left">

        <!-- System Status Badge -->
        <div class="status-badge" role="status" aria-label="System status: online">
          <span class="status-dot status-green" aria-hidden="true"></span>
          <span class="status-text">SYSTEM ONLINE</span>
          <span class="status-divider" aria-hidden="true">|</span>
          <span class="status-text cyan">BCH ANCHORED</span>
          <span class="status-divider" aria-hidden="true">|</span>
          <span class="status-text">ESP32 SCAN NODE</span>
        </div>

        <!-- Headline -->
        <h1 class="hero-title" id="hero-headline">
          <span class="title-line">EVERY HANDOFF.</span>
          <span class="title-line">CRYPTOGRAPHICALLY</span>
          <span class="title-line highlight-cyan">TRACEABLE.</span>
        </h1>

        <!-- Description -->
        <p class="hero-subtitle">
          ChainTrace is a Bitcoin Cash–anchored chain-of-custody system with custom IoT-based scan-logging hardware.
        </p>
        <p class="hero-desc">
          Every scan is hashed, stored, and anchored on the Bitcoin Cash blockchain—making tampering detectable and trust verifiable by anyone.
        </p>

        <!-- CTA Buttons -->
        <div class="hero-actions">
          <button id="btn-explore" class="btn btn-primary" @click="goTo('/dashboard')">
            EXPLORE THE SYSTEM <span class="btn-arrow">→</span>
          </button>
          <button id="btn-verify" class="btn btn-secondary" @click="goTo('/verify')">
            VERIFY A RECORD <span class="btn-arrow">↗</span>
          </button>
        </div>

        <!-- Feature Metrics Panel -->
        <div class="metrics-panel" role="list" aria-label="Key features">
          <div class="metric-item" role="listitem">
            <div class="metric-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="3" y="7" width="18" height="14" rx="2"/>
                <path d="M8 7V5a4 4 0 0 1 8 0v2"/>
                <circle cx="12" cy="14" r="2"/>
                <path d="M12 14v3" stroke-linecap="round"/>
              </svg>
            </div>
            <div class="metric-text">
              <span class="metric-label">REAL-TIME</span>
              <span class="metric-sublabel">SCAN LOGGING</span>
            </div>
          </div>
          <div class="metric-divider" aria-hidden="true"></div>
          <div class="metric-item" role="listitem">
            <div class="metric-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M12 2L3 7v6c0 5.25 3.75 10.15 9 11.25C17.25 23.15 21 18.25 21 13V7L12 2z"/>
                <path d="M9 12l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="metric-text">
              <span class="metric-label">TAMPER-EVIDENT</span>
              <span class="metric-sublabel">HASH VERIFICATION</span>
            </div>
          </div>
          <div class="metric-divider" aria-hidden="true"></div>
          <div class="metric-item" role="listitem">
            <div class="metric-icon metric-icon-bch" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <circle cx="12" cy="12" r="10"/>
                <path d="M9 8h4.5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
                <path d="M9 13h5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
                <line x1="11" y1="6" x2="11" y2="8"/>
                <line x1="13" y1="6" x2="13" y2="8"/>
                <line x1="11" y1="18" x2="11" y2="20"/>
                <line x1="13" y1="18" x2="13" y2="20"/>
              </svg>
            </div>
            <div class="metric-text">
              <span class="metric-label">ANCHORED ON</span>
              <span class="metric-sublabel">BITCOIN CASH</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ── RIGHT COLUMN (Visual Panel) ── -->
      <div class="hero-right">
        <div class="visual-panel" aria-label="Holographic blockchain visualization">
          <!-- Glow ring decorations -->
          <div class="panel-glow-ring panel-glow-ring--top" aria-hidden="true"></div>
          <div class="panel-glow-ring panel-glow-ring--bot" aria-hidden="true"></div>

          <!-- Floating status card – top left -->
          <div class="float-card float-card--top" role="status">
            <span class="float-dot float-dot--green" aria-hidden="true"></span>
            <div class="float-card-text">
              <span class="float-card-title">LIVE SCAN NODE</span>
              <span class="float-card-sub">ESP32 RFID v1.2</span>
            </div>
          </div>

          <!-- Main visual image -->
          <div class="visual-image-wrap">
            <img
              src="/img/hero_scan_node_blockchain.png"
              alt="ESP32 RFID scan node held in a hand with holographic blockchain network visualization"
              class="visual-image"
              loading="eager"
            />
            <!-- Blockchain network SVG overlay -->
            <div class="blockchain-overlay" aria-hidden="true">
              <svg class="blockchain-svg" viewBox="0 0 520 380" fill="none" xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <filter id="node-glow">
                    <feGaussianBlur stdDeviation="3" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                  <filter id="line-glow">
                    <feGaussianBlur stdDeviation="2" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                </defs>
                <!-- Connection lines -->
                <g filter="url(#line-glow)" opacity="0.5">
                  <line x1="260" y1="140" x2="120" y2="80" stroke="#00d4d4" stroke-width="1"/>
                  <line x1="260" y1="140" x2="400" y2="70" stroke="#00d4d4" stroke-width="1"/>
                  <line x1="260" y1="140" x2="80" y2="220" stroke="#00b4ff" stroke-width="1"/>
                  <line x1="260" y1="140" x2="440" y2="230" stroke="#00b4ff" stroke-width="1"/>
                  <line x1="120" y1="80" x2="400" y2="70" stroke="#00d4d4" stroke-width="0.5" stroke-dasharray="4,4"/>
                  <line x1="80" y1="220" x2="440" y2="230" stroke="#00b4ff" stroke-width="0.5" stroke-dasharray="4,4"/>
                </g>
                <!-- Center anchor cube -->
                <g filter="url(#node-glow)" class="svg-cube-center">
                  <rect x="210" y="100" width="100" height="80" rx="6" fill="rgba(0,212,212,0.08)" stroke="#00d4d4" stroke-width="1.5"/>
                  <text x="260" y="128" text-anchor="middle" fill="#00d4d4" font-size="7" font-family="monospace" font-weight="bold">ANCHORED ON</text>
                  <text x="260" y="142" text-anchor="middle" fill="#ffffff" font-size="9" font-family="monospace" font-weight="bold">BITCOIN</text>
                  <text x="260" y="156" text-anchor="middle" fill="#ffffff" font-size="9" font-family="monospace" font-weight="bold">CASH</text>
                  <text x="260" y="170" text-anchor="middle" fill="#00d4d4" font-size="7" font-family="monospace">CHAIN</text>
                </g>
                <!-- Block nodes -->
                <g filter="url(#node-glow)" opacity="0.9">
                  <rect x="75" y="52" width="90" height="56" rx="4" fill="rgba(0,100,255,0.1)" stroke="#00b4ff" stroke-width="1"/>
                  <text x="120" y="72" text-anchor="middle" fill="#00b4ff" font-size="5.5" font-family="monospace">BLOCK #892441</text>
                  <text x="120" y="84" text-anchor="middle" fill="#a0b4c8" font-size="5" font-family="monospace">TS: 2026-07-26</text>
                  <text x="120" y="96" text-anchor="middle" fill="#a0b4c8" font-size="4.5" font-family="monospace">0xa3f1...c82d</text>
                  <text x="120" y="107" text-anchor="middle" fill="#22c55e" font-size="5" font-family="monospace">✓ CONFIRMED</text>
                </g>
                <g filter="url(#node-glow)" opacity="0.9">
                  <rect x="356" y="44" width="90" height="56" rx="4" fill="rgba(120,40,220,0.1)" stroke="#a855f7" stroke-width="1"/>
                  <text x="401" y="64" text-anchor="middle" fill="#c084fc" font-size="5.5" font-family="monospace">BLOCK #892440</text>
                  <text x="401" y="76" text-anchor="middle" fill="#a0b4c8" font-size="5" font-family="monospace">TS: 2026-07-26</text>
                  <text x="401" y="88" text-anchor="middle" fill="#a0b4c8" font-size="4.5" font-family="monospace">0xf7e2...1a09</text>
                  <text x="401" y="99" text-anchor="middle" fill="#22c55e" font-size="5" font-family="monospace">✓ CONFIRMED</text>
                </g>
                <g filter="url(#node-glow)" opacity="0.8">
                  <rect x="30" y="194" width="90" height="56" rx="4" fill="rgba(0,212,212,0.08)" stroke="#00d4d4" stroke-width="1"/>
                  <text x="75" y="214" text-anchor="middle" fill="#00d4d4" font-size="5.5" font-family="monospace">SHA-256 HASH</text>
                  <text x="75" y="226" text-anchor="middle" fill="#a0b4c8" font-size="4.5" font-family="monospace">3b4c...f92a</text>
                  <text x="75" y="238" text-anchor="middle" fill="#a0b4c8" font-size="4.5" font-family="monospace">RFID: E200...</text>
                  <text x="75" y="249" text-anchor="middle" fill="#22c55e" font-size="5" font-family="monospace">VERIFIED ✓</text>
                </g>
                <g filter="url(#node-glow)" opacity="0.8">
                  <rect x="398" y="202" width="90" height="56" rx="4" fill="rgba(0,180,255,0.08)" stroke="#00b4ff" stroke-width="1"/>
                  <text x="443" y="222" text-anchor="middle" fill="#00b4ff" font-size="5.5" font-family="monospace">OP_RETURN TX</text>
                  <text x="443" y="234" text-anchor="middle" fill="#a0b4c8" font-size="4.5" font-family="monospace">9d1f...b347</text>
                  <text x="443" y="246" text-anchor="middle" fill="#a0b4c8" font-size="4.5" font-family="monospace">BCH CHIPNET</text>
                  <text x="443" y="257" text-anchor="middle" fill="#22c55e" font-size="5" font-family="monospace">ANCHORED ✓</text>
                </g>
              </svg>
            </div>
          </div>

          <!-- Floating verification card – bottom left -->
          <div class="float-card float-card--bot" role="status">
            <div class="float-card-shield" aria-hidden="true">
              <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M10 2L3 5.5v5c0 4.4 3.13 8.47 7 9.5 3.87-1.03 7-5.1 7-9.5v-5L10 2z"/>
                <path d="M7 10l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="float-card-text">
              <span class="float-card-title">BLOCKCHAIN ANCHORED</span>
              <div class="float-card-status">
                <span class="float-dot float-dot--green" aria-hidden="true"></span>
                <span class="float-card-sub">HASH VERIFIED</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         3. HOW IT WORKS
    ══════════════════════════════════════════════════ -->
    <section id="overview" class="how-it-works" aria-labelledby="overview-title">
      <h2 class="section-title" id="overview-title">HOW IT WORKS</h2>
      <div class="process-steps">
        <div class="step">
          <div class="step-icon" aria-hidden="true">1</div>
          <h3>RFID SCAN</h3>
          <p>Handler scans the asset tag using the ESP32 scan node.</p>
        </div>
        <div class="step-arrow" aria-hidden="true">→</div>
        <div class="step">
          <div class="step-icon" aria-hidden="true">2</div>
          <h3>HASH &amp; LOG</h3>
          <p>UID, timestamp, and sensor data are hashed using SHA-256 and stored off-chain.</p>
        </div>
        <div class="step-arrow" aria-hidden="true">→</div>
        <div class="step">
          <div class="step-icon" aria-hidden="true">3</div>
          <h3>BACKEND API</h3>
          <p>The event is sent to the Django backend and stored in PostgreSQL.</p>
        </div>
        <div class="step-arrow" aria-hidden="true">→</div>
        <div class="step">
          <div class="step-icon" aria-hidden="true">4</div>
          <h3>ANCHOR</h3>
          <p>The hash is anchored to Bitcoin Cash via an OP_RETURN transaction.</p>
        </div>
        <div class="step-arrow" aria-hidden="true">→</div>
        <div class="step">
          <div class="step-icon" aria-hidden="true">5</div>
          <h3>VERIFY ANYTIME</h3>
          <p>Anyone can verify the record by comparing the stored hash with the on-chain data.</p>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         4. CORE FEATURES
    ══════════════════════════════════════════════════ -->
    <section id="features" class="features-section" aria-labelledby="features-title">
      <h2 class="section-title" id="features-title">CORE FEATURES</h2>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon" aria-hidden="true">📡</div>
          <h3>HARDWARE-BASED SCAN LOGGING</h3>
          <p>Custom ESP32 node captures every custody handoff.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon" aria-hidden="true">⏱️</div>
          <h3>OFFLINE-READY TIMESTAMPING</h3>
          <p>DS3231 RTC ensures accurate timestamps even when offline.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon" aria-hidden="true">🚨</div>
          <h3>TAMPER DETECTION</h3>
          <p>Reed switch and motion sensors detect tampering or shocks.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon" aria-hidden="true">🔐</div>
          <h3>CRYPTOGRAPHIC INTEGRITY</h3>
          <p>Every event is hashed using SHA-256.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon" aria-hidden="true">🔗</div>
          <h3>BITCOIN CASH ANCHORING</h3>
          <p>Hashes are anchored on-chain via OP_RETURN outputs.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon" aria-hidden="true">✅</div>
          <h3>INDEPENDENT VERIFICATION</h3>
          <p>Anyone can verify records without trusting the system operator.</p>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         5. SYSTEM ARCHITECTURE
    ══════════════════════════════════════════════════ -->
    <section id="architecture" class="architecture-section" aria-labelledby="arch-title">
      <h2 class="section-title" id="arch-title">SYSTEM ARCHITECTURE</h2>
      <div class="architecture-diagram">
        <div class="arch-node">ESP32 SCAN NODE</div>
        <div class="arch-arrow" aria-hidden="true">↓</div>
        <div class="arch-node">DJANGO REST API</div>
        <div class="arch-arrow" aria-hidden="true">↓</div>
        <div class="arch-node">POSTGRESQL DATABASE</div>
        <div class="arch-arrow" aria-hidden="true">↓</div>
        <div class="arch-node">ANCHOR QUEUE</div>
        <div class="arch-arrow" aria-hidden="true">↓</div>
        <div class="arch-node highlight-node">BITCOIN CASH CHIPNET</div>
        <div class="arch-connector" aria-hidden="true"></div>
        <div class="arch-node verification-node">VERIFICATION DASHBOARD</div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         6. PROJECT STATUS
    ══════════════════════════════════════════════════ -->
    <section id="project" class="project-status" aria-labelledby="project-title">
      <h2 class="section-title" id="project-title">PROJECT STATUS</h2>
      <div class="timeline-container">
        <div class="timeline-item active-status">
          <span class="status-dot-item" aria-hidden="true"></span>
          <span class="status-label">Backend API</span>
          <span class="status-badge in-progress">IN PROGRESS</span>
        </div>
        <div class="timeline-item active-status">
          <span class="status-dot-item" aria-hidden="true"></span>
          <span class="status-label">Frontend</span>
          <span class="status-badge in-progress">IN PROGRESS</span>
        </div>
        <div class="timeline-item active-status">
          <span class="status-dot-item" aria-hidden="true"></span>
          <span class="status-label">Hardware Prototype</span>
          <span class="status-badge in-progress">IN PROGRESS</span>
        </div>
        <div class="timeline-item pending-status">
          <span class="status-dot-item" aria-hidden="true"></span>
          <span class="status-label">PCB Design Rev 1</span>
          <span class="status-badge pending">PENDING</span>
        </div>
        <div class="timeline-item pending-status">
          <span class="status-dot-item" aria-hidden="true"></span>
          <span class="status-label">PCB Fab &amp; Bring-up</span>
          <span class="status-badge pending">PENDING</span>
        </div>
        <div class="timeline-item pending-status">
          <span class="status-dot-item" aria-hidden="true"></span>
          <span class="status-label">System Integration</span>
          <span class="status-badge pending">PENDING</span>
        </div>
        <div class="timeline-item pending-status">
          <span class="status-dot-item" aria-hidden="true"></span>
          <span class="status-label">Evaluation &amp; Testing</span>
          <span class="status-badge pending">PENDING</span>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         7. TECH STACK
    ══════════════════════════════════════════════════ -->
    <section id="tech" class="tech-stack" aria-labelledby="tech-title">
      <h2 class="section-title" id="tech-title">TECH STACK</h2>
      <div class="tech-grid">
        <div class="tech-item">ESP32</div>
        <div class="tech-item">RFID RC522</div>
        <div class="tech-item">Django</div>
        <div class="tech-item">PostgreSQL</div>
        <div class="tech-item">Vue 3</div>
        <div class="tech-item highlight-tech">Bitcoin Cash Chipnet</div>
        <div class="tech-item">Docker</div>
        <div class="tech-item">KiCad</div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         8. CTA SECTION
    ══════════════════════════════════════════════════ -->
    <section id="contact" class="cta-section" aria-labelledby="cta-title">
      <div class="cta-content">
        <h2 class="cta-title" id="cta-title">TRUST THE RECORD.<br>VERIFY THE PROOF.</h2>
        <p class="cta-desc">ChainTrace makes every custody handoff transparent, tamper-evident, and verifiable—forever.</p>
        <div class="hero-actions">
          <button id="btn-cta-explore" class="btn btn-primary" @click="goTo('/dashboard')">
            EXPLORE THE SYSTEM <span class="btn-arrow">→</span>
          </button>
          <button id="btn-cta-verify" class="btn btn-secondary" @click="goTo('/verify')">
            VERIFY A RECORD <span class="btn-arrow">↗</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         9. FOOTER
    ══════════════════════════════════════════════════ -->
    <footer class="landing-footer">
      <div class="footer-content">
        <div class="footer-logo">CHAINTRACE</div>
        <p class="footer-copy">© 2024 ChainTrace Capstone Project | Eastern Samar State University – College of Engineering</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted, onBeforeUnmount } from 'vue'

const router = useRouter()
const bgCanvas = ref(null)
let animFrame = null

const goTo = (path) => {
  router.push(path)
}

// ── Particle + circuit-line canvas background ──────────────────────────────
function initCanvas() {
  const canvas = bgCanvas.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')

  const resize = () => {
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
  }
  resize()
  window.addEventListener('resize', resize)

  const PARTICLE_COUNT = 55
  const particles = Array.from({ length: PARTICLE_COUNT }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 1.5 + 0.3,
    vx: (Math.random() - 0.5) * 0.25,
    vy: (Math.random() - 0.5) * 0.25,
    alpha: Math.random() * 0.5 + 0.1,
  }))

  const draw = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Subtle grid
    ctx.strokeStyle = 'rgba(0, 180, 200, 0.04)'
    ctx.lineWidth = 0.5
    const gridSize = 60
    for (let x = 0; x < canvas.width; x += gridSize) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke()
    }
    for (let y = 0; y < canvas.height; y += gridSize) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke()
    }

    // Particles
    particles.forEach(p => {
      p.x += p.vx
      p.y += p.vy
      if (p.x < 0) p.x = canvas.width
      if (p.x > canvas.width) p.x = 0
      if (p.y < 0) p.y = canvas.height
      if (p.y > canvas.height) p.y = 0

      ctx.beginPath()
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
      ctx.fillStyle = `rgba(0, 212, 212, ${p.alpha})`
      ctx.fill()
    })

    // Connection lines between nearby particles
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x
        const dy = particles[i].y - particles[j].y
        const dist = Math.sqrt(dx * dx + dy * dy)
        if (dist < 120) {
          ctx.beginPath()
          ctx.moveTo(particles[i].x, particles[i].y)
          ctx.lineTo(particles[j].x, particles[j].y)
          ctx.strokeStyle = `rgba(0, 180, 200, ${0.06 * (1 - dist / 120)})`
          ctx.lineWidth = 0.5
          ctx.stroke()
        }
      }
    }

    animFrame = requestAnimationFrame(draw)
  }
  draw()

  return () => window.removeEventListener('resize', resize)
}

onMounted(() => {
  const cleanup = initCanvas()
  onBeforeUnmount(() => {
    if (animFrame) cancelAnimationFrame(animFrame)
    cleanup?.()
  })
})
</script>

<style scoped>
/* ════════════════════════════════════════════════════
   DESIGN TOKENS
════════════════════════════════════════════════════ */
:root {
  --cyan:        #00d4d4;
  --cyan-dim:    rgba(0, 212, 212, 0.18);
  --cyan-glow:   rgba(0, 212, 212, 0.35);
  --blue:        #00b4ff;
  --bg-base:     #040a18;
  --bg-card:     rgba(8, 16, 36, 0.75);
  --text-primary:   #ffffff;
  --text-muted:     #7a90a8;
  --border-subtle:  rgba(0, 212, 212, 0.14);
  --border-active:  rgba(0, 212, 212, 0.45);
}

/* ════════════════════════════════════════════════════
   BASE
════════════════════════════════════════════════════ */
.landing-page {
  background-color: #040a18;
  color: #e0e8f0;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  overflow-x: hidden;
  position: relative;
}

.bg-canvas {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
}

.section-title {
  text-align: center;
  font-size: clamp(1.6rem, 3vw, 2.5rem);
  letter-spacing: 3px;
  margin-bottom: 3rem;
  color: #ffffff;
  text-transform: uppercase;
  font-weight: 800;
}

/* ════════════════════════════════════════════════════
   BUTTONS
════════════════════════════════════════════════════ */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.75rem;
  font-size: 0.875rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  white-space: nowrap;
}

.btn-primary {
  background: #00d4d4;
  color: #040a18;
  box-shadow: 0 0 22px rgba(0, 212, 212, 0.38);
}
.btn-primary:hover {
  background: #22eaea;
  box-shadow: 0 0 36px rgba(0, 212, 212, 0.6);
  transform: translateY(-1px);
}

.btn-secondary {
  background: rgba(0, 212, 212, 0.05);
  color: #00d4d4;
  border: 1px solid rgba(0, 212, 212, 0.45);
}
.btn-secondary:hover {
  background: rgba(0, 212, 212, 0.12);
  border-color: #00d4d4;
  box-shadow: 0 0 18px rgba(0, 212, 212, 0.2);
  transform: translateY(-1px);
}

.btn-arrow {
  font-size: 1rem;
  line-height: 1;
}

/* ════════════════════════════════════════════════════
   1. HEADER
════════════════════════════════════════════════════ */
.landing-header {
  position: fixed;
  top: 0; left: 0; right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.9rem 4rem;
  background: rgba(4, 10, 24, 0.82);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(0, 212, 212, 0.18);
  z-index: 100;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.logo-icon {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
  filter: drop-shadow(0 0 6px rgba(0, 212, 212, 0.6));
}

.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1;
}

.brand-name {
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: 3px;
  color: #fff;
  line-height: 1.2;
}

.brand-tagline {
  font-size: 0.6rem;
  letter-spacing: 2px;
  color: #00d4d4;
  margin-top: 2px;
  font-family: 'Courier New', monospace;
}

.landing-nav {
  display: flex;
  gap: 1.75rem;
}

.nav-link {
  color: #7a90a8;
  text-decoration: none;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 1.5px;
  transition: color 0.25s ease;
  padding-bottom: 3px;
  border-bottom: 2px solid transparent;
}

.nav-link:hover {
  color: #00d4d4;
}

.nav-link.active {
  color: #00d4d4;
  border-bottom-color: #00d4d4;
  text-shadow: 0 0 8px rgba(0, 212, 212, 0.4);
}

/* ════════════════════════════════════════════════════
   2. HERO SECTION
════════════════════════════════════════════════════ */
.hero-section {
  min-height: 100vh;
  padding: 9rem 4rem 5rem;
  display: flex;
  align-items: center;
  gap: 3rem;
  position: relative;
  z-index: 1;
  background:
    radial-gradient(ellipse 60% 50% at 70% 50%, rgba(0, 180, 200, 0.07) 0%, transparent 70%),
    radial-gradient(ellipse 40% 40% at 15% 60%, rgba(0, 100, 255, 0.05) 0%, transparent 60%);
}

/* Subtle grid texture on hero */
.hero-grid-overlay {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(0, 212, 212, 0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 212, 212, 0.035) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
}

/* ── Left Column ── */
.hero-left {
  flex: 0 0 45%;
  max-width: 45%;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* Status Badge */
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.45rem 1rem;
  border: 1px solid rgba(0, 212, 212, 0.38);
  border-radius: 20px;
  background: rgba(0, 212, 212, 0.04);
  backdrop-filter: blur(8px);
  margin-bottom: 2rem;
  width: fit-content;
}

.status-text {
  font-family: 'Courier New', monospace;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 1px;
  color: #7a90a8;
  text-transform: uppercase;
}

.status-text.cyan {
  color: #00d4d4;
}

.status-divider {
  color: rgba(0, 212, 212, 0.3);
  font-size: 0.7rem;
}

.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  flex-shrink: 0;
}

.status-green {
  background: #22c55e;
  box-shadow: 0 0 6px #22c55e;
  animation: pulse-green 2s ease-in-out infinite;
}

@keyframes pulse-green {
  0%, 100% { opacity: 1; box-shadow: 0 0 6px #22c55e; }
  50%       { opacity: 0.7; box-shadow: 0 0 12px #22c55e; }
}

/* Headline */
.hero-title {
  display: flex;
  flex-direction: column;
  font-size: clamp(2.5rem, 4.5vw, 4.2rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin: 0 0 1.5rem;
  color: #ffffff;
}

.title-line {
  display: block;
}

.highlight-cyan {
  color: #00d4d4;
  text-shadow:
    0 0 20px rgba(0, 212, 212, 0.55),
    0 0 40px rgba(0, 212, 212, 0.25);
}

.hero-subtitle {
  font-size: 1.1rem;
  color: #c8d8e8;
  margin: 0 0 0.75rem;
  max-width: 520px;
  line-height: 1.65;
}

.hero-desc {
  font-size: 0.95rem;
  color: #7a90a8;
  margin: 0 0 2.25rem;
  max-width: 520px;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  gap: 1.25rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

/* Metrics Panel */
.metrics-panel {
  display: flex;
  align-items: stretch;
  background: rgba(8, 16, 36, 0.65);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(0, 212, 212, 0.2);
  border-radius: 10px;
  padding: 0;
  overflow: hidden;
  max-width: 520px;
}

.metric-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.1rem 1.35rem;
  flex: 1;
}

.metric-icon {
  width: 32px;
  height: 32px;
  color: #00d4d4;
  flex-shrink: 0;
}

.metric-icon-bch {
  color: #22c55e;
}

.metric-text {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.metric-label {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: #ffffff;
  text-transform: uppercase;
}

.metric-sublabel {
  font-size: 0.6rem;
  letter-spacing: 0.8px;
  color: #00d4d4;
  font-family: 'Courier New', monospace;
  text-transform: uppercase;
}

.metric-divider {
  width: 1px;
  background: rgba(0, 212, 212, 0.18);
  align-self: stretch;
}

/* ── Right Column ── */
.hero-right {
  flex: 0 0 55%;
  max-width: 55%;
  z-index: 2;
  display: flex;
  justify-content: center;
  align-items: center;
}

.visual-panel {
  position: relative;
  width: 100%;
  max-width: 620px;
  border-radius: 16px;
  border: 1px solid rgba(0, 212, 212, 0.3);
  background: rgba(4, 10, 24, 0.4);
  backdrop-filter: blur(4px);
  overflow: hidden;
  box-shadow:
    0 0 40px rgba(0, 212, 212, 0.08),
    inset 0 0 60px rgba(0, 100, 200, 0.04);
  aspect-ratio: 16 / 11;
}

/* Glow rings */
.panel-glow-ring {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
}
.panel-glow-ring--top {
  width: 300px; height: 300px;
  top: -80px; right: -60px;
  background: radial-gradient(circle, rgba(0, 180, 255, 0.10) 0%, transparent 70%);
}
.panel-glow-ring--bot {
  width: 250px; height: 250px;
  bottom: -60px; left: 20px;
  background: radial-gradient(circle, rgba(0, 212, 212, 0.08) 0%, transparent 70%);
}

/* Visual image */
.visual-image-wrap {
  position: relative;
  width: 100%; height: 100%;
}

.visual-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

/* Blockchain SVG overlay */
.blockchain-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.blockchain-svg {
  width: 100%;
  height: 100%;
}

/* Cube center animation */
.svg-cube-center {
  animation: cube-pulse 3s ease-in-out infinite;
}
@keyframes cube-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

/* Floating status cards */
.float-card {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.6rem 0.9rem;
  background: rgba(4, 10, 24, 0.88);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(0, 212, 212, 0.35);
  border-radius: 8px;
  z-index: 10;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  animation: float-bob 4s ease-in-out infinite;
}

@keyframes float-bob {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-5px); }
}

.float-card--top {
  top: 16px;
  left: 16px;
  animation-delay: 0s;
}

.float-card--bot {
  bottom: 16px;
  left: 16px;
  animation-delay: 2s;
}

.float-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  flex-shrink: 0;
}

.float-dot--green {
  background: #22c55e;
  box-shadow: 0 0 6px #22c55e;
  animation: pulse-green 2s ease-in-out infinite;
}

.float-card-text {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.float-card-title {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: #ffffff;
  text-transform: uppercase;
}

.float-card-sub {
  font-size: 0.58rem;
  color: #00d4d4;
  font-family: 'Courier New', monospace;
  letter-spacing: 0.5px;
}

.float-card-status {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.float-card-shield {
  width: 22px;
  height: 22px;
  color: #00d4d4;
  flex-shrink: 0;
}

/* ════════════════════════════════════════════════════
   3. HOW IT WORKS
════════════════════════════════════════════════════ */
.how-it-works {
  padding: 6rem 4rem;
  background-color: #060d1e;
  border-top: 1px solid rgba(0, 212, 212, 0.1);
  border-bottom: 1px solid rgba(0, 212, 212, 0.1);
  position: relative;
  z-index: 1;
}

.process-steps {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  max-width: 1200px;
  margin: 0 auto;
}

.step {
  flex: 1;
  text-align: center;
  padding: 1rem;
}

.step-icon {
  width: 60px;
  height: 60px;
  margin: 0 auto 1.5rem;
  border-radius: 50%;
  background: rgba(0, 212, 212, 0.08);
  border: 2px solid #00d4d4;
  color: #00d4d4;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5rem;
  font-weight: 800;
  box-shadow: 0 0 15px rgba(0, 212, 212, 0.25);
}

.step h3 {
  font-size: 1rem;
  color: #fff;
  margin-bottom: 0.75rem;
  letter-spacing: 1px;
}

.step p {
  font-size: 0.88rem;
  color: #7a90a8;
  line-height: 1.6;
}

.step-arrow {
  color: #00d4d4;
  font-size: 2rem;
  margin-top: 1.5rem;
  opacity: 0.45;
}

/* ════════════════════════════════════════════════════
   4. FEATURES
════════════════════════════════════════════════════ */
.features-section {
  padding: 8rem 4rem;
  position: relative;
  z-index: 1;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
  max-width: 1100px;
  margin: 0 auto;
}

.feature-card {
  background: rgba(8, 16, 36, 0.6);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0, 212, 212, 0.16);
  padding: 2.25rem;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  border-color: rgba(0, 212, 212, 0.5);
  box-shadow: 0 12px 32px rgba(0, 212, 212, 0.12);
}

.feature-icon {
  font-size: 2.25rem;
  margin-bottom: 1.25rem;
}

.feature-card h3 {
  font-size: 0.95rem;
  color: #fff;
  margin-bottom: 0.75rem;
  letter-spacing: 1px;
  font-weight: 700;
}

.feature-card p {
  color: #7a90a8;
  line-height: 1.65;
  font-size: 0.9rem;
}

/* ════════════════════════════════════════════════════
   5. ARCHITECTURE
════════════════════════════════════════════════════ */
.architecture-section {
  padding: 6rem 4rem;
  background: #060d1e;
  position: relative;
  z-index: 1;
}

.architecture-diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
  margin: 0 auto;
}

.arch-node {
  background: rgba(8, 16, 36, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1rem 2rem;
  border-radius: 5px;
  font-weight: 600;
  letter-spacing: 1.5px;
  font-size: 0.9rem;
  min-width: 260px;
  text-align: center;
  z-index: 2;
}

.arch-arrow {
  color: #00d4d4;
  font-size: 1.5rem;
  margin: 0.4rem 0;
  opacity: 0.6;
}

.highlight-node {
  border-color: #00d4d4;
  color: #00d4d4;
  box-shadow: 0 0 18px rgba(0, 212, 212, 0.2);
}

.arch-connector {
  height: 40px;
  width: 2px;
  background: linear-gradient(to bottom, rgba(0, 212, 212, 0.5), transparent);
  margin: 0.75rem 0;
}

.verification-node {
  background: rgba(0, 212, 212, 0.06);
  border-color: rgba(0, 212, 212, 0.5);
  border-style: dashed;
  color: #00d4d4;
}

/* ════════════════════════════════════════════════════
   6. PROJECT STATUS
════════════════════════════════════════════════════ */
.project-status {
  padding: 8rem 4rem;
  position: relative;
  z-index: 1;
}

.timeline-container {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.timeline-item {
  display: flex;
  align-items: center;
  background: rgba(8, 16, 36, 0.55);
  padding: 1rem 1.75rem;
  border-radius: 6px;
  border-left: 2px solid;
}

.active-status { border-left-color: #00d4d4; }
.pending-status { border-left-color: #1e3048; opacity: 0.6; }

.status-dot-item {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 1.5rem;
  flex-shrink: 0;
}

.active-status .status-dot-item {
  background: #00d4d4;
  box-shadow: 0 0 8px #00d4d4;
}
.pending-status .status-dot-item { background: #1e3048; }

.status-label {
  flex: 1;
  font-size: 1.05rem;
  font-weight: 500;
}

.status-badge {
  font-size: 0.72rem;
  padding: 0.25rem 0.8rem;
  border-radius: 12px;
  font-weight: 700;
  letter-spacing: 1px;
}

.in-progress {
  background: rgba(0, 212, 212, 0.08);
  color: #00d4d4;
  border: 1px solid rgba(0, 212, 212, 0.3);
}

.pending {
  background: rgba(30, 48, 72, 0.25);
  color: #7a90a8;
  border: 1px solid rgba(30, 48, 72, 0.6);
}

/* ════════════════════════════════════════════════════
   7. TECH STACK
════════════════════════════════════════════════════ */
.tech-stack {
  padding: 6rem 4rem;
  background: #060d1e;
  position: relative;
  z-index: 1;
}

.tech-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.25rem;
  max-width: 900px;
  margin: 0 auto;
}

.tech-item {
  background: rgba(8, 16, 36, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.9rem 1.75rem;
  border-radius: 5px;
  font-weight: 600;
  font-size: 0.9rem;
  color: #7a90a8;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
}

.tech-item:hover {
  color: #fff;
  border-color: rgba(255, 255, 255, 0.28);
}

.highlight-tech {
  color: #00d4d4;
  border-color: rgba(0, 212, 212, 0.32);
}

.highlight-tech:hover {
  color: #00d4d4;
  border-color: #00d4d4;
  box-shadow: 0 0 16px rgba(0, 212, 212, 0.2);
}

/* ════════════════════════════════════════════════════
   8. CTA SECTION
════════════════════════════════════════════════════ */
.cta-section {
  padding: 8rem 4rem;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  position: relative;
  z-index: 1;
  background: radial-gradient(ellipse 60% 60% at 50% 50%, rgba(0, 180, 200, 0.06) 0%, transparent 70%);
}

.cta-content { max-width: 700px; }

.cta-title {
  font-size: clamp(2rem, 4vw, 3.5rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  color: #fff;
  letter-spacing: -0.5px;
}

.cta-desc {
  font-size: 1.1rem;
  color: #7a90a8;
  margin-bottom: 2.5rem;
  line-height: 1.65;
}

/* ════════════════════════════════════════════════════
   9. FOOTER
════════════════════════════════════════════════════ */
.landing-footer {
  background: #030812;
  padding: 2.5rem 4rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  text-align: center;
  position: relative;
  z-index: 1;
}

.footer-logo {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 3px;
  color: #fff;
  margin-bottom: 0.75rem;
}

.footer-copy {
  color: #3a5068;
  font-size: 0.82rem;
}

/* ════════════════════════════════════════════════════
   RESPONSIVE
════════════════════════════════════════════════════ */
@media (max-width: 1100px) {
  .hero-section {
    flex-direction: column;
    text-align: left;
    padding: 10rem 2.5rem 4rem;
    gap: 3rem;
  }
  .hero-left, .hero-right {
    flex: unset;
    max-width: 100%;
    width: 100%;
  }
  .metrics-panel { max-width: 100%; }
  .process-steps { flex-direction: column; align-items: center; gap: 1rem; }
  .step-arrow { transform: rotate(90deg); margin: 0; }
  .features-grid { grid-template-columns: repeat(2, 1fr); }
  .landing-header { padding: 0.9rem 2rem; }
}

@media (max-width: 768px) {
  .landing-nav { display: none; }
  .features-grid { grid-template-columns: 1fr; }
  .hero-title { font-size: 2.4rem; }
  .cta-title { font-size: 2rem; }
  .metrics-panel { flex-direction: column; }
  .metric-divider { width: auto; height: 1px; align-self: stretch; }
  .hero-section { padding: 9rem 1.5rem 3rem; }
  .how-it-works,
  .features-section,
  .architecture-section,
  .project-status,
  .tech-stack,
  .cta-section { padding: 4rem 1.5rem; }
}
</style>
