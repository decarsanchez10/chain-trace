<template>
  <div class="landing-page">
    <!-- Animated Background Canvas -->
    <canvas class="bg-canvas" ref="bgCanvas"></canvas>

    <!-- ══════════════════════════════════════════
         HEADER
    ══════════════════════════════════════════ -->
    <header class="landing-header">
      <div class="brand">
        <div class="logo-icon" aria-hidden="true">
          <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <filter id="logo-glow">
                <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
                <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
            </defs>
            <g filter="url(#logo-glow)">
              <polygon points="20,4 34,12 20,20 6,12" fill="rgba(0,212,212,0.15)" stroke="#00d4d4" stroke-width="1.2"/>
              <polygon points="6,12 20,20 20,36 6,28" fill="rgba(0,212,212,0.08)" stroke="#00d4d4" stroke-width="1.2"/>
              <polygon points="34,12 20,20 20,36 34,28" fill="rgba(0,100,255,0.12)" stroke="#00b4ff" stroke-width="1.2"/>
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
        <a href="#home"         class="nav-link active" id="nav-home">HOME</a>
        <a href="#overview"     class="nav-link" id="nav-overview">OVERVIEW</a>
        <a href="#architecture" class="nav-link" id="nav-architecture">ARCHITECTURE</a>
        <a href="#features"     class="nav-link" id="nav-features">FEATURES</a>
        <a href="#tech"         class="nav-link" id="nav-tech">TECH STACK</a>
        <a href="#project"      class="nav-link" id="nav-project">PROJECT</a>
        <a href="#contact"      class="nav-link" id="nav-contact">CONTACT</a>
      </nav>
    </header>

    <!-- ══════════════════════════════════════════
         HERO
    ══════════════════════════════════════════ -->
    <section id="home" class="hero-section" aria-labelledby="hero-headline">
      <div class="hero-grid-overlay" aria-hidden="true"></div>

      <div class="hero-left">
        <div class="status-badge" role="status">
          <span class="status-dot status-green" aria-hidden="true"></span>
          <span class="status-text">SYSTEM ONLINE</span>
          <span class="status-divider" aria-hidden="true">|</span>
          <span class="status-text cyan">BCH ANCHORED</span>
          <span class="status-divider" aria-hidden="true">|</span>
          <span class="status-text">ESP32 SCAN NODE</span>
        </div>

        <h1 class="hero-title" id="hero-headline">
          <span class="title-line">EVERY HANDOFF.</span>
          <span class="title-line">CRYPTOGRAPHICALLY</span>
          <span class="title-line highlight-cyan">TRACEABLE.</span>
        </h1>

        <p class="hero-subtitle">
          ChainTrace is a Bitcoin Cash–anchored chain-of-custody system with custom IoT-based scan-logging hardware.
        </p>
        <p class="hero-desc">
          Every scan is hashed, stored, and anchored on the Bitcoin Cash blockchain—making tampering detectable and trust verifiable by anyone.
        </p>

        <div class="hero-actions">
          <button id="btn-explore" class="btn btn-primary" @click="goTo('/dashboard')">
            EXPLORE THE SYSTEM <span class="btn-arrow">→</span>
          </button>
          <button id="btn-verify" class="btn btn-secondary" @click="goTo('/verify')">
            VERIFY A RECORD <span class="btn-arrow">↗</span>
          </button>
        </div>

        <div class="metrics-panel" role="list" aria-label="Key features">
          <div class="metric-item" role="listitem">
            <div class="metric-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="3" y="7" width="18" height="14" rx="2"/>
                <path d="M8 7V5a4 4 0 0 1 8 0v2"/><circle cx="12" cy="14" r="2"/>
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
                <line x1="11" y1="6" x2="11" y2="8"/><line x1="13" y1="6" x2="13" y2="8"/>
                <line x1="11" y1="18" x2="11" y2="20"/><line x1="13" y1="18" x2="13" y2="20"/>
              </svg>
            </div>
            <div class="metric-text">
              <span class="metric-label">ANCHORED ON</span>
              <span class="metric-sublabel">BITCOIN CASH</span>
            </div>
          </div>
        </div>
      </div>

      <div class="hero-right">
        <div class="visual-panel" aria-label="Holographic blockchain visualization">
          <div class="panel-glow-ring panel-glow-ring--top" aria-hidden="true"></div>
          <div class="panel-glow-ring panel-glow-ring--bot" aria-hidden="true"></div>

          <div class="float-card float-card--top" role="status">
            <span class="float-dot float-dot--green" aria-hidden="true"></span>
            <div class="float-card-text">
              <span class="float-card-title">LIVE SCAN NODE</span>
              <span class="float-card-sub">ESP32 RFID v1.2</span>
            </div>
          </div>

          <div class="visual-image-wrap">
            <img src="/img/hero_scan_node_blockchain.png"
              alt="ESP32 RFID scan node with holographic blockchain network"
              class="visual-image" loading="eager"/>
            <div class="blockchain-overlay" aria-hidden="true">
              <svg class="blockchain-svg" viewBox="0 0 520 380" fill="none" xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <filter id="node-glow"><feGaussianBlur stdDeviation="3" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
                  <filter id="line-glow"><feGaussianBlur stdDeviation="2" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
                </defs>
                <g filter="url(#line-glow)" opacity="0.5">
                  <line x1="260" y1="140" x2="120" y2="80" stroke="#00d4d4" stroke-width="1"/>
                  <line x1="260" y1="140" x2="400" y2="70" stroke="#00d4d4" stroke-width="1"/>
                  <line x1="260" y1="140" x2="80" y2="220" stroke="#00b4ff" stroke-width="1"/>
                  <line x1="260" y1="140" x2="440" y2="230" stroke="#00b4ff" stroke-width="1"/>
                  <line x1="120" y1="80" x2="400" y2="70" stroke="#00d4d4" stroke-width="0.5" stroke-dasharray="4,4"/>
                  <line x1="80" y1="220" x2="440" y2="230" stroke="#00b4ff" stroke-width="0.5" stroke-dasharray="4,4"/>
                </g>
                <g filter="url(#node-glow)" class="svg-cube-center">
                  <rect x="210" y="100" width="100" height="80" rx="6" fill="rgba(0,212,212,0.08)" stroke="#00d4d4" stroke-width="1.5"/>
                  <text x="260" y="128" text-anchor="middle" fill="#00d4d4" font-size="7" font-family="monospace" font-weight="bold">ANCHORED ON</text>
                  <text x="260" y="142" text-anchor="middle" fill="#ffffff" font-size="9" font-family="monospace" font-weight="bold">BITCOIN</text>
                  <text x="260" y="156" text-anchor="middle" fill="#ffffff" font-size="9" font-family="monospace" font-weight="bold">CASH</text>
                  <text x="260" y="170" text-anchor="middle" fill="#00d4d4" font-size="7" font-family="monospace">CHAIN</text>
                </g>
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

    <!-- ══════════════════════════════════════════
         HOW IT WORKS
    ══════════════════════════════════════════ -->
    <section id="overview" class="how-it-works" aria-labelledby="overview-title">
      <div class="section-label-tag" aria-hidden="true">// PROCESS OVERVIEW</div>
      <h2 class="section-title" id="overview-title">HOW IT WORKS</h2>
      <p class="section-subtitle">Five deterministic steps from physical scan to immutable blockchain record.</p>

      <div class="process-flow">
        <!-- Step 1 -->
        <div class="process-step">
          <div class="step-number-wrap">
            <div class="step-num">01</div>
            <div class="step-connector" aria-hidden="true"></div>
          </div>
          <div class="step-card">
            <div class="step-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="3" y="7" width="18" height="14" rx="2"/>
                <path d="M8 7V5a4 4 0 0 1 8 0v2"/>
                <circle cx="12" cy="14" r="2"/>
              </svg>
            </div>
            <div class="step-body">
              <span class="step-tag">STEP 01</span>
              <h3 class="step-title">RFID SCAN</h3>
              <p class="step-desc">Handler scans the asset tag using the ESP32 scan node. UID is captured in milliseconds.</p>
            </div>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="process-step">
          <div class="step-number-wrap">
            <div class="step-num">02</div>
            <div class="step-connector" aria-hidden="true"></div>
          </div>
          <div class="step-card">
            <div class="step-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M12 2L3 7v6c0 5.25 3.75 10.15 9 11.25C17.25 23.15 21 18.25 21 13V7L12 2z"/>
                <path d="M9 12l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="step-body">
              <span class="step-tag">STEP 02</span>
              <h3 class="step-title">HASH &amp; LOG</h3>
              <p class="step-desc">UID, timestamp, and sensor data are hashed using SHA-256 and stored off-chain locally.</p>
            </div>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="process-step">
          <div class="step-number-wrap">
            <div class="step-num">03</div>
            <div class="step-connector" aria-hidden="true"></div>
          </div>
          <div class="step-card">
            <div class="step-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="2" y="3" width="20" height="14" rx="2"/>
                <path d="M8 21h8M12 17v4" stroke-linecap="round"/>
                <path d="M6 8h.01M10 8h8" stroke-linecap="round"/>
                <path d="M6 11h.01M10 11h8" stroke-linecap="round"/>
              </svg>
            </div>
            <div class="step-body">
              <span class="step-tag">STEP 03</span>
              <h3 class="step-title">BACKEND API</h3>
              <p class="step-desc">The event is transmitted to the Django REST API and stored in a PostgreSQL database.</p>
            </div>
          </div>
        </div>

        <!-- Step 4 -->
        <div class="process-step">
          <div class="step-number-wrap">
            <div class="step-num">04</div>
            <div class="step-connector" aria-hidden="true"></div>
          </div>
          <div class="step-card">
            <div class="step-icon-box step-icon-box--green" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <circle cx="12" cy="12" r="10"/>
                <path d="M9 8h4.5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
                <path d="M9 13h5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
                <line x1="11" y1="6" x2="11" y2="8"/><line x1="13" y1="6" x2="13" y2="8"/>
                <line x1="11" y1="18" x2="11" y2="20"/><line x1="13" y1="18" x2="13" y2="20"/>
              </svg>
            </div>
            <div class="step-body">
              <span class="step-tag step-tag--green">STEP 04</span>
              <h3 class="step-title">BCH ANCHOR</h3>
              <p class="step-desc">The SHA-256 hash is anchored to Bitcoin Cash via an OP_RETURN transaction—permanently.</p>
            </div>
          </div>
        </div>

        <!-- Step 5 -->
        <div class="process-step">
          <div class="step-number-wrap">
            <div class="step-num step-num--last">05</div>
          </div>
          <div class="step-card">
            <div class="step-icon-box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/>
                <circle cx="12" cy="12" r="3"/>
              </svg>
            </div>
            <div class="step-body">
              <span class="step-tag">STEP 05</span>
              <h3 class="step-title">VERIFY ANYTIME</h3>
              <p class="step-desc">Anyone can verify the record by comparing the stored hash against on-chain data—no trust required.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════
         CORE FEATURES
    ══════════════════════════════════════════ -->
    <section id="features" class="features-section" aria-labelledby="features-title">
      <div class="section-label-tag" aria-hidden="true">// CORE CAPABILITIES</div>
      <h2 class="section-title" id="features-title">CORE FEATURES</h2>
      <p class="section-subtitle">Every layer of ChainTrace is purpose-built for trust, integrity, and verifiability.</p>

      <div class="features-grid">
        <div class="feature-card" id="feat-scan">
          <div class="feature-icon-wrap" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="3" y="7" width="18" height="14" rx="2"/>
              <path d="M8 7V5a4 4 0 0 1 8 0v2"/>
              <circle cx="12" cy="14" r="2"/>
            </svg>
          </div>
          <div class="feature-tag">HARDWARE</div>
          <h3>HARDWARE-BASED SCAN LOGGING</h3>
          <p>Custom ESP32 node captures every custody handoff with precision and reliability.</p>
        </div>

        <div class="feature-card" id="feat-time">
          <div class="feature-icon-wrap" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <circle cx="12" cy="12" r="10"/>
              <path d="M12 6v6l4 2" stroke-linecap="round"/>
            </svg>
          </div>
          <div class="feature-tag">FIRMWARE</div>
          <h3>OFFLINE-READY TIMESTAMPING</h3>
          <p>DS3231 RTC module ensures accurate timestamps even in zero-connectivity environments.</p>
        </div>

        <div class="feature-card" id="feat-tamper">
          <div class="feature-icon-wrap feature-icon-wrap--red" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
              <line x1="12" y1="9" x2="12" y2="13" stroke-linecap="round"/>
              <line x1="12" y1="17" x2="12.01" y2="17" stroke-linecap="round"/>
            </svg>
          </div>
          <div class="feature-tag feature-tag--red">SECURITY</div>
          <h3>TAMPER DETECTION</h3>
          <p>Reed switch and motion sensors detect physical tampering or shock events in real time.</p>
        </div>

        <div class="feature-card" id="feat-hash">
          <div class="feature-icon-wrap" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M12 2L3 7v6c0 5.25 3.75 10.15 9 11.25C17.25 23.15 21 18.25 21 13V7L12 2z"/>
              <path d="M9 12l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="feature-tag">CRYPTOGRAPHY</div>
          <h3>CRYPTOGRAPHIC INTEGRITY</h3>
          <p>Every custody event is hashed using SHA-256, creating a unique, unforgeable fingerprint.</p>
        </div>

        <div class="feature-card feature-card--accent" id="feat-bch">
          <div class="feature-icon-wrap feature-icon-wrap--bch" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <circle cx="12" cy="12" r="10"/>
              <path d="M9 8h4.5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
              <path d="M9 13h5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
              <line x1="11" y1="6" x2="11" y2="8"/><line x1="13" y1="6" x2="13" y2="8"/>
              <line x1="11" y1="18" x2="11" y2="20"/><line x1="13" y1="18" x2="13" y2="20"/>
            </svg>
          </div>
          <div class="feature-tag feature-tag--bch">BLOCKCHAIN</div>
          <h3>BITCOIN CASH ANCHORING</h3>
          <p>Hashes anchored on-chain via OP_RETURN—providing permanent, public, tamper-proof proof of record.</p>
        </div>

        <div class="feature-card" id="feat-verify">
          <div class="feature-icon-wrap" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/>
              <circle cx="12" cy="12" r="3"/>
            </svg>
          </div>
          <div class="feature-tag">TRANSPARENCY</div>
          <h3>INDEPENDENT VERIFICATION</h3>
          <p>Anyone can verify records without trusting the system operator—open, permissionless, and auditable.</p>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════
         SYSTEM ARCHITECTURE
    ══════════════════════════════════════════ -->
    <section id="architecture" class="architecture-section" aria-labelledby="arch-title">
      <div class="section-label-tag" aria-hidden="true">// SYSTEM DESIGN</div>
      <h2 class="section-title" id="arch-title">SYSTEM ARCHITECTURE</h2>
      <p class="section-subtitle">A five-layer pipeline from physical hardware to immutable blockchain record.</p>

      <div class="arch-pipeline">
        <div class="arch-layer" id="arch-esp32">
          <div class="arch-layer-side">
            <span class="arch-layer-num">L1</span>
            <div class="arch-layer-line" aria-hidden="true"></div>
          </div>
          <div class="arch-layer-card arch-layer-card--hardware">
            <div class="arch-layer-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="4" y="4" width="16" height="16" rx="2"/>
                <rect x="9" y="9" width="6" height="6" rx="1"/>
                <path d="M9 2v2M15 2v2M9 20v2M15 20v2M2 9h2M2 15h2M20 9h2M20 15h2"/>
              </svg>
            </div>
            <div class="arch-layer-body">
              <div class="arch-layer-badge arch-layer-badge--hardware">HARDWARE LAYER</div>
              <h3>ESP32 SCAN NODE</h3>
              <p>RFID RC522 reader · DS3231 RTC · Reed tamper switch · Wi-Fi uplink · Local SHA-256 hashing</p>
            </div>
            <div class="arch-layer-status">
              <span class="arch-dot arch-dot--green" aria-hidden="true"></span>
              <span>ACTIVE</span>
            </div>
          </div>
        </div>

        <div class="arch-connector-vert" aria-hidden="true">
          <svg viewBox="0 0 20 40" fill="none">
            <line x1="10" y1="0" x2="10" y2="40" stroke="#00d4d4" stroke-width="1" stroke-dasharray="4,3" opacity="0.5"/>
            <polygon points="5,32 10,40 15,32" fill="#00d4d4" opacity="0.6"/>
          </svg>
        </div>

        <div class="arch-layer" id="arch-api">
          <div class="arch-layer-side">
            <span class="arch-layer-num">L2</span>
            <div class="arch-layer-line" aria-hidden="true"></div>
          </div>
          <div class="arch-layer-card arch-layer-card--backend">
            <div class="arch-layer-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="2" y="3" width="20" height="14" rx="2"/>
                <path d="M8 21h8M12 17v4" stroke-linecap="round"/>
                <path d="M6 8h.01M10 8h8" stroke-linecap="round"/>
                <path d="M6 11h.01M10 11h5" stroke-linecap="round"/>
              </svg>
            </div>
            <div class="arch-layer-body">
              <div class="arch-layer-badge arch-layer-badge--backend">BACKEND LAYER</div>
              <h3>DJANGO REST API</h3>
              <p>Receives scan events · Validates payload · Stores to PostgreSQL · Queues anchor jobs</p>
            </div>
            <div class="arch-layer-status">
              <span class="arch-dot arch-dot--green" aria-hidden="true"></span>
              <span>ONLINE</span>
            </div>
          </div>
        </div>

        <div class="arch-connector-vert" aria-hidden="true">
          <svg viewBox="0 0 20 40" fill="none">
            <line x1="10" y1="0" x2="10" y2="40" stroke="#00d4d4" stroke-width="1" stroke-dasharray="4,3" opacity="0.5"/>
            <polygon points="5,32 10,40 15,32" fill="#00d4d4" opacity="0.6"/>
          </svg>
        </div>

        <div class="arch-layer" id="arch-db">
          <div class="arch-layer-side">
            <span class="arch-layer-num">L3</span>
            <div class="arch-layer-line" aria-hidden="true"></div>
          </div>
          <div class="arch-layer-card arch-layer-card--data">
            <div class="arch-layer-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <ellipse cx="12" cy="5" rx="9" ry="3"/>
                <path d="M21 5v6c0 1.66-4.03 3-9 3S3 12.66 3 11V5"/>
                <path d="M21 11v6c0 1.66-4.03 3-9 3S3 18.66 3 17v-6"/>
              </svg>
            </div>
            <div class="arch-layer-body">
              <div class="arch-layer-badge arch-layer-badge--data">DATA LAYER</div>
              <h3>POSTGRESQL DATABASE</h3>
              <p>Custody records · Hash index · Anchor status · Event metadata · Verification log</p>
            </div>
            <div class="arch-layer-status">
              <span class="arch-dot arch-dot--green" aria-hidden="true"></span>
              <span>SYNCED</span>
            </div>
          </div>
        </div>

        <div class="arch-connector-vert" aria-hidden="true">
          <svg viewBox="0 0 20 40" fill="none">
            <line x1="10" y1="0" x2="10" y2="40" stroke="#00d4d4" stroke-width="1" stroke-dasharray="4,3" opacity="0.5"/>
            <polygon points="5,32 10,40 15,32" fill="#00d4d4" opacity="0.6"/>
          </svg>
        </div>

        <div class="arch-layer" id="arch-anchor">
          <div class="arch-layer-side">
            <span class="arch-layer-num">L4</span>
            <div class="arch-layer-line" aria-hidden="true"></div>
          </div>
          <div class="arch-layer-card arch-layer-card--anchor">
            <div class="arch-layer-icon arch-layer-icon--anchor" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <circle cx="12" cy="12" r="10"/>
                <path d="M9 8h4.5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
                <path d="M9 13h5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
                <line x1="11" y1="6" x2="11" y2="8"/><line x1="13" y1="6" x2="13" y2="8"/>
                <line x1="11" y1="18" x2="11" y2="20"/><line x1="13" y1="18" x2="13" y2="20"/>
              </svg>
            </div>
            <div class="arch-layer-body">
              <div class="arch-layer-badge arch-layer-badge--anchor">BLOCKCHAIN LAYER</div>
              <h3>BITCOIN CASH CHIPNET</h3>
              <p>OP_RETURN anchoring · Transaction hash stored · Publicly auditable · Tamper-proof finality</p>
            </div>
            <div class="arch-layer-status arch-layer-status--bch">
              <span class="arch-dot arch-dot--bch" aria-hidden="true"></span>
              <span>ANCHORED</span>
            </div>
          </div>
        </div>

        <!-- Side branch — Verification Dashboard -->
        <div class="arch-side-branch" aria-hidden="true">
          <svg viewBox="0 0 120 40" fill="none">
            <line x1="0" y1="20" x2="100" y2="20" stroke="#00d4d4" stroke-width="1" stroke-dasharray="4,3" opacity="0.4"/>
            <polygon points="92,15 100,20 92,25" fill="#00d4d4" opacity="0.5"/>
          </svg>
          <div class="arch-layer-card arch-layer-card--verify">
            <div class="arch-layer-body">
              <div class="arch-layer-badge arch-layer-badge--verify">VERIFICATION</div>
              <h3>DASHBOARD</h3>
              <p>Public hash lookup · On-chain proof display · Chain-of-custody timeline</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════
         PROJECT STATUS
    ══════════════════════════════════════════ -->
    <section id="project" class="project-status" aria-labelledby="project-title">
      <div class="section-label-tag" aria-hidden="true">// BUILD PROGRESS</div>
      <h2 class="section-title" id="project-title">PROJECT STATUS</h2>
      <p class="section-subtitle">Current development milestones and build pipeline status.</p>

      <div class="timeline-grid">
        <div class="timeline-card timeline-card--active" id="tl-backend">
          <div class="timeline-card-header">
            <div class="timeline-indicator">
              <span class="tl-dot tl-dot--active" aria-hidden="true"></span>
              <span class="tl-badge tl-badge--active">IN PROGRESS</span>
            </div>
            <span class="tl-num">01</span>
          </div>
          <div class="tl-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="2" y="3" width="20" height="14" rx="2"/>
              <path d="M8 21h8M12 17v4" stroke-linecap="round"/>
            </svg>
          </div>
          <h3 class="tl-title">Backend API</h3>
          <p class="tl-desc">Django REST endpoints, custody model, and anchor queue service.</p>
          <div class="tl-progress-bar" aria-hidden="true">
            <div class="tl-progress-fill" style="width:70%"></div>
          </div>
          <span class="tl-pct">70%</span>
        </div>

        <div class="timeline-card timeline-card--active" id="tl-frontend">
          <div class="timeline-card-header">
            <div class="timeline-indicator">
              <span class="tl-dot tl-dot--active" aria-hidden="true"></span>
              <span class="tl-badge tl-badge--active">IN PROGRESS</span>
            </div>
            <span class="tl-num">02</span>
          </div>
          <div class="tl-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M4 5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5z"/>
              <path d="M14 5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1V5z"/>
              <path d="M14 13a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1v-6z"/>
              <path d="M4 14a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6z"/>
            </svg>
          </div>
          <h3 class="tl-title">Frontend</h3>
          <p class="tl-desc">Vue 3 dashboard, verification UI, and landing page.</p>
          <div class="tl-progress-bar" aria-hidden="true">
            <div class="tl-progress-fill" style="width:65%"></div>
          </div>
          <span class="tl-pct">65%</span>
        </div>

        <div class="timeline-card timeline-card--active" id="tl-hw">
          <div class="timeline-card-header">
            <div class="timeline-indicator">
              <span class="tl-dot tl-dot--active" aria-hidden="true"></span>
              <span class="tl-badge tl-badge--active">IN PROGRESS</span>
            </div>
            <span class="tl-num">03</span>
          </div>
          <div class="tl-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="4" y="4" width="16" height="16" rx="2"/>
              <rect x="9" y="9" width="6" height="6" rx="1"/>
              <path d="M9 2v2M15 2v2M9 20v2M15 20v2M2 9h2M2 15h2M20 9h2M20 15h2"/>
            </svg>
          </div>
          <h3 class="tl-title">Hardware Prototype</h3>
          <p class="tl-desc">ESP32 breadboard prototype with RFID RC522 and DS3231 RTC.</p>
          <div class="tl-progress-bar" aria-hidden="true">
            <div class="tl-progress-fill" style="width:80%"></div>
          </div>
          <span class="tl-pct">80%</span>
        </div>

        <div class="timeline-card timeline-card--pending" id="tl-pcb">
          <div class="timeline-card-header">
            <div class="timeline-indicator">
              <span class="tl-dot tl-dot--pending" aria-hidden="true"></span>
              <span class="tl-badge tl-badge--pending">PENDING</span>
            </div>
            <span class="tl-num">04</span>
          </div>
          <div class="tl-icon tl-icon--dim" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M12 2L2 7l10 5 10-5-10-5z"/>
              <path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>
            </svg>
          </div>
          <h3 class="tl-title">PCB Design Rev 1</h3>
          <p class="tl-desc">Schematic capture, layout routing, and DRC validation in KiCad.</p>
          <div class="tl-progress-bar" aria-hidden="true">
            <div class="tl-progress-fill tl-progress-fill--pending" style="width:0%"></div>
          </div>
          <span class="tl-pct tl-pct--dim">—</span>
        </div>

        <div class="timeline-card timeline-card--pending" id="tl-fab">
          <div class="timeline-card-header">
            <div class="timeline-indicator">
              <span class="tl-dot tl-dot--pending" aria-hidden="true"></span>
              <span class="tl-badge tl-badge--pending">PENDING</span>
            </div>
            <span class="tl-num">05</span>
          </div>
          <div class="tl-icon tl-icon--dim" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
            </svg>
          </div>
          <h3 class="tl-title">PCB Fab &amp; Bring-up</h3>
          <p class="tl-desc">PCB fabrication, component assembly, and hardware bring-up testing.</p>
          <div class="tl-progress-bar" aria-hidden="true">
            <div class="tl-progress-fill tl-progress-fill--pending" style="width:0%"></div>
          </div>
          <span class="tl-pct tl-pct--dim">—</span>
        </div>

        <div class="timeline-card timeline-card--pending" id="tl-eval">
          <div class="timeline-card-header">
            <div class="timeline-indicator">
              <span class="tl-dot tl-dot--pending" aria-hidden="true"></span>
              <span class="tl-badge tl-badge--pending">PENDING</span>
            </div>
            <span class="tl-num">06</span>
          </div>
          <div class="tl-icon tl-icon--dim" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M9 11l3 3L22 4"/>
              <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
            </svg>
          </div>
          <h3 class="tl-title">System Integration &amp; Evaluation</h3>
          <p class="tl-desc">End-to-end integration testing, performance benchmarks, and final evaluation.</p>
          <div class="tl-progress-bar" aria-hidden="true">
            <div class="tl-progress-fill tl-progress-fill--pending" style="width:0%"></div>
          </div>
          <span class="tl-pct tl-pct--dim">—</span>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════
         TECH STACK
    ══════════════════════════════════════════ -->
    <section id="tech" class="tech-stack" aria-labelledby="tech-title">
      <div class="section-label-tag" aria-hidden="true">// TECHNOLOGY</div>
      <h2 class="section-title" id="tech-title">TECH STACK</h2>
      <p class="section-subtitle">Purpose-selected technologies for reliability, security, and scale.</p>

      <div class="tech-grid">
        <div class="tech-card" id="tech-esp32">
          <div class="tech-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="4" y="4" width="16" height="16" rx="2"/>
              <rect x="9" y="9" width="6" height="6" rx="1"/>
              <path d="M9 2v2M15 2v2M9 20v2M15 20v2M2 9h2M2 15h2M20 9h2M20 15h2"/>
            </svg>
          </div>
          <span class="tech-card-name">ESP32</span>
          <span class="tech-card-layer">FIRMWARE</span>
        </div>

        <div class="tech-card" id="tech-rfid">
          <div class="tech-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="3" y="7" width="18" height="14" rx="2"/>
              <path d="M8 7V5a4 4 0 0 1 8 0v2"/>
              <circle cx="12" cy="14" r="2"/>
            </svg>
          </div>
          <span class="tech-card-name">RFID RC522</span>
          <span class="tech-card-layer">HARDWARE</span>
        </div>

        <div class="tech-card" id="tech-django">
          <div class="tech-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M3 3h18v18H3z" rx="2"/>
              <path d="M3 9h18M9 21V9"/>
            </svg>
          </div>
          <span class="tech-card-name">Django</span>
          <span class="tech-card-layer">BACKEND</span>
        </div>

        <div class="tech-card" id="tech-postgres">
          <div class="tech-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <ellipse cx="12" cy="5" rx="9" ry="3"/>
              <path d="M21 5v6c0 1.66-4.03 3-9 3S3 12.66 3 11V5"/>
              <path d="M21 11v6c0 1.66-4.03 3-9 3S3 18.66 3 17v-6"/>
            </svg>
          </div>
          <span class="tech-card-name">PostgreSQL</span>
          <span class="tech-card-layer">DATABASE</span>
        </div>

        <div class="tech-card" id="tech-vue">
          <div class="tech-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M2 3h4l6 10 6-10h4L12 21 2 3z"/>
              <path d="M6 3l6 10 6-10" opacity="0.5"/>
            </svg>
          </div>
          <span class="tech-card-name">Vue 3</span>
          <span class="tech-card-layer">FRONTEND</span>
        </div>

        <div class="tech-card tech-card--accent" id="tech-bch">
          <div class="tech-card-icon tech-card-icon--bch" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <circle cx="12" cy="12" r="10"/>
              <path d="M9 8h4.5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
              <path d="M9 13h5a2.5 2.5 0 0 1 0 5H9v-5z" stroke-linecap="round"/>
              <line x1="11" y1="6" x2="11" y2="8"/><line x1="13" y1="6" x2="13" y2="8"/>
              <line x1="11" y1="18" x2="11" y2="20"/><line x1="13" y1="18" x2="13" y2="20"/>
            </svg>
          </div>
          <span class="tech-card-name">Bitcoin Cash</span>
          <span class="tech-card-layer tech-card-layer--bch">BLOCKCHAIN</span>
        </div>

        <div class="tech-card" id="tech-docker">
          <div class="tech-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M22 12.5c0 .5-.4 1.5-2 2.5-2 1-4 1-6 0"/>
              <rect x="2" y="9" width="3" height="3" rx="0.5"/>
              <rect x="6" y="9" width="3" height="3" rx="0.5"/>
              <rect x="10" y="9" width="3" height="3" rx="0.5"/>
              <rect x="6" y="5" width="3" height="3" rx="0.5"/>
              <rect x="10" y="5" width="3" height="3" rx="0.5"/>
              <path d="M2 13c0 3 2 5 9 5s11-2 11-5" opacity="0.5"/>
            </svg>
          </div>
          <span class="tech-card-name">Docker</span>
          <span class="tech-card-layer">DEVOPS</span>
        </div>

        <div class="tech-card" id="tech-kicad">
          <div class="tech-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M12 2L2 7l10 5 10-5-10-5z"/>
              <path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>
            </svg>
          </div>
          <span class="tech-card-name">KiCad</span>
          <span class="tech-card-layer">PCB DESIGN</span>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════
         CTA SECTION
    ══════════════════════════════════════════ -->
    <section id="contact" class="cta-section" aria-labelledby="cta-title">
      <div class="cta-grid-overlay" aria-hidden="true"></div>
      <div class="cta-glow" aria-hidden="true"></div>

      <div class="cta-inner">
        <div class="cta-tag" aria-hidden="true">
          <span class="tl-dot tl-dot--active" aria-hidden="true"></span>
          SYSTEM LIVE · CHIPNET ACTIVE
        </div>

        <h2 class="cta-title" id="cta-title">
          TRUST THE RECORD.<br>
          <span class="highlight-cyan">VERIFY THE PROOF.</span>
        </h2>
        <p class="cta-desc">
          ChainTrace makes every custody handoff transparent, tamper-evident, and verifiable—forever on the Bitcoin Cash blockchain.
        </p>

        <div class="hero-actions cta-actions">
          <button id="btn-cta-explore" class="btn btn-primary" @click="goTo('/dashboard')">
            EXPLORE THE SYSTEM <span class="btn-arrow">→</span>
          </button>
          <button id="btn-cta-verify" class="btn btn-secondary" @click="goTo('/verify')">
            VERIFY A RECORD <span class="btn-arrow">↗</span>
          </button>
        </div>

        <!-- Mini stats row -->
        <div class="cta-stats" aria-label="System statistics">
          <div class="cta-stat">
            <span class="cta-stat-value">SHA-256</span>
            <span class="cta-stat-label">HASH ALGORITHM</span>
          </div>
          <div class="cta-stat-divider" aria-hidden="true"></div>
          <div class="cta-stat">
            <span class="cta-stat-value">OP_RETURN</span>
            <span class="cta-stat-label">ANCHOR METHOD</span>
          </div>
          <div class="cta-stat-divider" aria-hidden="true"></div>
          <div class="cta-stat">
            <span class="cta-stat-value">BCH CHIPNET</span>
            <span class="cta-stat-label">TARGET NETWORK</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════
         FOOTER
    ══════════════════════════════════════════ -->
    <footer class="landing-footer">
      <div class="footer-top">
        <div class="footer-brand">
          <div class="footer-logo-wrap">
            <div class="logo-icon logo-icon--sm" aria-hidden="true">
              <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <polygon points="20,4 34,12 20,20 6,12" fill="rgba(0,212,212,0.15)" stroke="#00d4d4" stroke-width="1.2"/>
                <polygon points="6,12 20,20 20,36 6,28" fill="rgba(0,212,212,0.08)" stroke="#00d4d4" stroke-width="1.2"/>
                <polygon points="34,12 20,20 20,36 34,28" fill="rgba(0,100,255,0.12)" stroke="#00b4ff" stroke-width="1.2"/>
              </svg>
            </div>
            <span class="footer-wordmark">CHAINTRACE</span>
          </div>
          <p class="footer-tagline">TRACE. VERIFY. TRUST.</p>
          <p class="footer-about">A Bitcoin Cash–anchored chain-of-custody system with custom ESP32 IoT scan-logging hardware.</p>
        </div>

        <div class="footer-links-col">
          <span class="footer-col-title">NAVIGATION</span>
          <a href="#home" class="footer-link">Home</a>
          <a href="#overview" class="footer-link">Overview</a>
          <a href="#architecture" class="footer-link">Architecture</a>
          <a href="#features" class="footer-link">Features</a>
          <a href="#tech" class="footer-link">Tech Stack</a>
          <a href="#project" class="footer-link">Project</a>
        </div>

        <div class="footer-links-col">
          <span class="footer-col-title">SYSTEM</span>
          <a href="/dashboard" class="footer-link" @click.prevent="goTo('/dashboard')">Dashboard</a>
          <a href="/verify" class="footer-link" @click.prevent="goTo('/verify')">Verify Record</a>
          <a href="/login" class="footer-link" @click.prevent="goTo('/login')">Login</a>
        </div>

        <div class="footer-links-col">
          <span class="footer-col-title">BUILT WITH</span>
          <span class="footer-tech-tag">ESP32 · RFID RC522</span>
          <span class="footer-tech-tag">Django · PostgreSQL</span>
          <span class="footer-tech-tag">Vue 3 · Vite</span>
          <span class="footer-tech-tag footer-tech-tag--bch">Bitcoin Cash Chipnet</span>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-bottom-left">
          <span class="footer-status-dot" aria-hidden="true"></span>
          <span class="footer-status-text">BCH CHIPNET · SYSTEM ONLINE</span>
        </div>
        <p class="footer-copy">
          © 2024 ChainTrace Capstone Project &nbsp;·&nbsp; Eastern Samar State University – College of Engineering
        </p>
        <div class="footer-bottom-hash" aria-hidden="true">
          <span class="footer-hash-label">LATEST TX</span>
          <span class="footer-hash-value">0x9d1f...b347</span>
        </div>
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
let resizeHandler = null

const goTo = (path) => {
  router.push(path)
}

function initCanvas() {
  const canvas = bgCanvas.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')

  const resize = () => {
    canvas.width = window.innerWidth
    canvas.height = document.documentElement.scrollHeight
  }
  resize()
  resizeHandler = resize
  window.addEventListener('resize', resize)

  const PARTICLE_COUNT = 70
  const particles = Array.from({ length: PARTICLE_COUNT }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 1.4 + 0.3,
    vx: (Math.random() - 0.5) * 0.22,
    vy: (Math.random() - 0.5) * 0.22,
    alpha: Math.random() * 0.45 + 0.08,
  }))

  const draw = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Technical grid
    ctx.strokeStyle = 'rgba(0, 180, 200, 0.035)'
    ctx.lineWidth = 0.5
    const g = 60
    for (let x = 0; x < canvas.width; x += g) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke()
    }
    for (let y = 0; y < canvas.height; y += g) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke()
    }

    // Particles + connections
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy
      if (p.x < 0) p.x = canvas.width
      if (p.x > canvas.width) p.x = 0
      if (p.y < 0) p.y = canvas.height
      if (p.y > canvas.height) p.y = 0
      ctx.beginPath()
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
      ctx.fillStyle = `rgba(0,212,212,${p.alpha})`
      ctx.fill()
    })

    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x
        const dy = particles[i].y - particles[j].y
        const dist = Math.sqrt(dx * dx + dy * dy)
        if (dist < 110) {
          ctx.beginPath()
          ctx.moveTo(particles[i].x, particles[i].y)
          ctx.lineTo(particles[j].x, particles[j].y)
          ctx.strokeStyle = `rgba(0,180,200,${0.055 * (1 - dist / 110)})`
          ctx.lineWidth = 0.5
          ctx.stroke()
        }
      }
    }

    animFrame = requestAnimationFrame(draw)
  }
  draw()
}

onMounted(() => {
  initCanvas()
})

onBeforeUnmount(() => {
  if (animFrame) cancelAnimationFrame(animFrame)
  if (resizeHandler) window.removeEventListener('resize', resizeHandler)
})
</script>

<style scoped>
/* ═══════════════════════════════════════════════════════
   BASE
═══════════════════════════════════════════════════════ */
.landing-page {
  background-color: #040a18;
  color: #e0e8f0;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  overflow-x: hidden;
  position: relative;
}

.bg-canvas {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  pointer-events: none;
  z-index: 0;
}

/* Shared section scaffold */
.section-label-tag {
  text-align: center;
  font-family: 'Courier New', monospace;
  font-size: 0.72rem;
  letter-spacing: 2px;
  color: #00d4d4;
  margin-bottom: 0.75rem;
  opacity: 0.7;
}

.section-title {
  text-align: center;
  font-size: clamp(1.6rem, 2.8vw, 2.4rem);
  font-weight: 800;
  letter-spacing: 3px;
  margin: 0 0 0.75rem;
  color: #ffffff;
}

.section-subtitle {
  text-align: center;
  font-size: 1rem;
  color: #5a7a98;
  margin: 0 auto 3.5rem;
  max-width: 560px;
  line-height: 1.65;
}

/* Buttons */
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
  font-family: 'Inter', sans-serif;
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
.btn-arrow { font-size: 1rem; }

.highlight-cyan {
  color: #00d4d4;
  text-shadow: 0 0 20px rgba(0,212,212,0.55), 0 0 40px rgba(0,212,212,0.2);
}

/* ═══════════════════════════════════════════════════════
   HEADER
═══════════════════════════════════════════════════════ */
.landing-header {
  position: fixed;
  top: 0; left: 0; right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.9rem 4rem;
  background: rgba(4, 10, 24, 0.85);
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
  width: 40px; height: 40px; flex-shrink: 0;
  filter: drop-shadow(0 0 6px rgba(0,212,212,0.6));
}
.logo-icon--sm { width: 30px; height: 30px; }
.brand-text { display: flex; flex-direction: column; line-height: 1; }
.brand-name { font-size: 1.35rem; font-weight: 800; letter-spacing: 3px; color: #fff; line-height: 1.2; }
.brand-tagline { font-size: 0.6rem; letter-spacing: 2px; color: #00d4d4; margin-top: 2px; font-family: 'Courier New', monospace; }
.landing-nav { display: flex; gap: 1.75rem; }
.nav-link {
  color: #5a7a98;
  text-decoration: none;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 1.5px;
  transition: color 0.25s ease;
  padding-bottom: 3px;
  border-bottom: 2px solid transparent;
}
.nav-link:hover { color: #00d4d4; }
.nav-link.active {
  color: #00d4d4;
  border-bottom-color: #00d4d4;
  text-shadow: 0 0 8px rgba(0,212,212,0.4);
}

/* ═══════════════════════════════════════════════════════
   HERO
═══════════════════════════════════════════════════════ */
.hero-section {
  min-height: 100vh;
  padding: 9rem 4rem 5rem;
  display: flex;
  align-items: center;
  gap: 3rem;
  position: relative;
  z-index: 1;
  background:
    radial-gradient(ellipse 60% 50% at 70% 50%, rgba(0,180,200,0.07) 0%, transparent 70%),
    radial-gradient(ellipse 40% 40% at 15% 60%, rgba(0,100,255,0.05) 0%, transparent 60%);
}
.hero-grid-overlay {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(0,212,212,0.032) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,212,212,0.032) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
}
.hero-left {
  flex: 0 0 45%; max-width: 45%;
  z-index: 2;
  display: flex; flex-direction: column; gap: 0;
}
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.45rem 1rem;
  border: 1px solid rgba(0,212,212,0.38);
  border-radius: 20px;
  background: rgba(0,212,212,0.04);
  backdrop-filter: blur(8px);
  margin-bottom: 2rem;
  width: fit-content;
}
.status-text {
  font-family: 'Courier New', monospace;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 1px;
  color: #5a7a98;
  text-transform: uppercase;
}
.status-text.cyan { color: #00d4d4; }
.status-divider { color: rgba(0,212,212,0.3); font-size: 0.7rem; }
.status-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
.status-green { background: #22c55e; box-shadow: 0 0 6px #22c55e; animation: pulse-green 2s ease-in-out infinite; }

@keyframes pulse-green {
  0%, 100% { opacity: 1; box-shadow: 0 0 6px #22c55e; }
  50%       { opacity: 0.7; box-shadow: 0 0 12px #22c55e; }
}

.hero-title {
  display: flex; flex-direction: column;
  font-size: clamp(2.5rem, 4.5vw, 4.2rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin: 0 0 1.5rem;
  color: #ffffff;
}
.title-line { display: block; }
.hero-subtitle { font-size: 1.1rem; color: #c8d8e8; margin: 0 0 0.75rem; max-width: 520px; line-height: 1.65; }
.hero-desc { font-size: 0.95rem; color: #5a7a98; margin: 0 0 2.25rem; max-width: 520px; line-height: 1.7; }
.hero-actions { display: flex; gap: 1.25rem; margin-bottom: 2.5rem; flex-wrap: wrap; }

.metrics-panel {
  display: flex;
  align-items: stretch;
  background: rgba(8,16,36,0.65);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(0,212,212,0.2);
  border-radius: 10px;
  overflow: hidden;
  max-width: 520px;
}
.metric-item { display: flex; align-items: center; gap: 0.75rem; padding: 1.1rem 1.35rem; flex: 1; }
.metric-icon { width: 32px; height: 32px; color: #00d4d4; flex-shrink: 0; }
.metric-icon-bch { color: #22c55e; }
.metric-text { display: flex; flex-direction: column; gap: 1px; }
.metric-label { font-size: 0.65rem; font-weight: 700; letter-spacing: 1px; color: #fff; text-transform: uppercase; }
.metric-sublabel { font-size: 0.6rem; letter-spacing: 0.8px; color: #00d4d4; font-family: 'Courier New', monospace; text-transform: uppercase; }
.metric-divider { width: 1px; background: rgba(0,212,212,0.18); align-self: stretch; }

/* Hero Right */
.hero-right {
  flex: 0 0 55%; max-width: 55%;
  z-index: 2;
  display: flex; justify-content: center; align-items: center;
}
.visual-panel {
  position: relative;
  width: 100%; max-width: 620px;
  border-radius: 16px;
  border: 1px solid rgba(0,212,212,0.3);
  background: rgba(4,10,24,0.4);
  backdrop-filter: blur(4px);
  overflow: hidden;
  box-shadow: 0 0 40px rgba(0,212,212,0.08), inset 0 0 60px rgba(0,100,200,0.04);
  aspect-ratio: 16/11;
}
.panel-glow-ring { position: absolute; border-radius: 50%; pointer-events: none; z-index: 0; }
.panel-glow-ring--top { width:300px;height:300px;top:-80px;right:-60px; background:radial-gradient(circle,rgba(0,180,255,0.10) 0%,transparent 70%); }
.panel-glow-ring--bot { width:250px;height:250px;bottom:-60px;left:20px; background:radial-gradient(circle,rgba(0,212,212,0.08) 0%,transparent 70%); }
.visual-image-wrap { position:relative; width:100%; height:100%; }
.visual-image { width:100%; height:100%; object-fit:cover; object-position:center; display:block; }
.blockchain-overlay { position:absolute;inset:0; pointer-events:none; }
.blockchain-svg { width:100%; height:100%; }
.svg-cube-center { animation: cube-pulse 3s ease-in-out infinite; }
@keyframes cube-pulse { 0%,100%{opacity:1} 50%{opacity:0.7} }

.float-card {
  position: absolute;
  display: flex; align-items: center; gap: 0.6rem;
  padding: 0.6rem 0.9rem;
  background: rgba(4,10,24,0.9);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0,212,212,0.35);
  border-radius: 8px;
  z-index: 10;
  box-shadow: 0 4px 20px rgba(0,0,0,0.5);
  animation: float-bob 4s ease-in-out infinite;
}
@keyframes float-bob { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-5px)} }
.float-card--top { top:16px; left:16px; animation-delay:0s; }
.float-card--bot { bottom:16px; left:16px; animation-delay:2s; }
.float-dot { width:7px; height:7px; border-radius:50%; flex-shrink:0; }
.float-dot--green { background:#22c55e; box-shadow:0 0 6px #22c55e; animation:pulse-green 2s ease-in-out infinite; }
.float-card-text { display:flex; flex-direction:column; gap:1px; }
.float-card-title { font-size:0.65rem; font-weight:700; letter-spacing:1px; color:#fff; text-transform:uppercase; }
.float-card-sub { font-size:0.58rem; color:#00d4d4; font-family:'Courier New',monospace; letter-spacing:0.5px; }
.float-card-status { display:flex; align-items:center; gap:0.4rem; }
.float-card-shield { width:22px; height:22px; color:#00d4d4; flex-shrink:0; }

/* ═══════════════════════════════════════════════════════
   HOW IT WORKS
═══════════════════════════════════════════════════════ */
.how-it-works {
  padding: 7rem 4rem;
  background: #060d1e;
  border-top: 1px solid rgba(0,212,212,0.1);
  position: relative;
  z-index: 1;
}

.process-flow {
  display: flex;
  flex-direction: column;
  gap: 0;
  max-width: 820px;
  margin: 0 auto;
}

.process-step {
  display: flex;
  gap: 0;
  align-items: stretch;
}

.step-number-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 64px;
  flex-shrink: 0;
}

.step-num {
  width: 44px; height: 44px;
  border-radius: 50%;
  border: 1px solid rgba(0,212,212,0.45);
  background: rgba(0,212,212,0.06);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
  font-weight: 700;
  color: #00d4d4;
  letter-spacing: 1px;
  flex-shrink: 0;
}

.step-num--last { border-color: rgba(0,212,212,0.6); box-shadow: 0 0 12px rgba(0,212,212,0.2); }

.step-connector {
  flex: 1;
  width: 1px;
  background: linear-gradient(to bottom, rgba(0,212,212,0.35), rgba(0,212,212,0.1));
  margin: 6px auto;
  min-height: 28px;
}

.step-card {
  flex: 1;
  display: flex;
  align-items: flex-start;
  gap: 1.25rem;
  margin-left: 1.25rem;
  margin-bottom: 2.25rem;
  padding: 1.5rem 1.75rem;
  background: rgba(8,16,36,0.6);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0,212,212,0.14);
  border-radius: 10px;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.step-card:hover {
  border-color: rgba(0,212,212,0.4);
  box-shadow: 0 8px 28px rgba(0,212,212,0.1);
}

.step-icon-box {
  width: 44px; height: 44px;
  flex-shrink: 0;
  border-radius: 8px;
  border: 1px solid rgba(0,212,212,0.3);
  background: rgba(0,212,212,0.06);
  display: flex; align-items: center; justify-content: center;
  color: #00d4d4;
  padding: 9px;
}
.step-icon-box--green { border-color: rgba(34,197,94,0.4); background: rgba(34,197,94,0.06); color: #22c55e; }

.step-body { flex: 1; }

.step-tag {
  font-family: 'Courier New', monospace;
  font-size: 0.62rem;
  letter-spacing: 1.5px;
  color: #00d4d4;
  opacity: 0.7;
  display: block;
  margin-bottom: 0.3rem;
}
.step-tag--green { color: #22c55e; }

.step-title {
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: 1px;
  margin: 0 0 0.5rem;
}

.step-desc {
  font-size: 0.9rem;
  color: #5a7a98;
  line-height: 1.65;
  margin: 0;
}

/* ═══════════════════════════════════════════════════════
   CORE FEATURES
═══════════════════════════════════════════════════════ */
.features-section {
  padding: 7rem 4rem;
  position: relative;
  z-index: 1;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  max-width: 1100px;
  margin: 0 auto;
}

.feature-card {
  background: rgba(8,16,36,0.6);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(0,212,212,0.14);
  padding: 2rem 1.75rem;
  border-radius: 12px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}
.feature-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(0,212,212,0.4), transparent);
  opacity: 0;
  transition: opacity 0.3s;
}
.feature-card:hover { transform: translateY(-4px); border-color: rgba(0,212,212,0.38); box-shadow: 0 12px 32px rgba(0,212,212,0.1); }
.feature-card:hover::before { opacity: 1; }
.feature-card--accent { border-color: rgba(34,197,94,0.25); }
.feature-card--accent:hover { border-color: rgba(34,197,94,0.55); box-shadow: 0 12px 32px rgba(34,197,94,0.1); }
.feature-card--accent::before { background: linear-gradient(90deg, transparent, rgba(34,197,94,0.4), transparent); }

.feature-icon-wrap {
  width: 46px; height: 46px;
  border-radius: 10px;
  border: 1px solid rgba(0,212,212,0.3);
  background: rgba(0,212,212,0.06);
  display: flex; align-items: center; justify-content: center;
  color: #00d4d4;
  padding: 10px;
  margin-bottom: 1.25rem;
}
.feature-icon-wrap--red { border-color: rgba(239,68,68,0.35); background: rgba(239,68,68,0.06); color: #f87171; }
.feature-icon-wrap--bch { border-color: rgba(34,197,94,0.35); background: rgba(34,197,94,0.06); color: #22c55e; }

.feature-tag {
  font-family: 'Courier New', monospace;
  font-size: 0.62rem;
  letter-spacing: 1.5px;
  color: #00d4d4;
  opacity: 0.7;
  margin-bottom: 0.5rem;
  display: block;
}
.feature-tag--red { color: #f87171; }
.feature-tag--bch { color: #22c55e; }

.feature-card h3 {
  font-size: 0.9rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: 1px;
  margin: 0 0 0.75rem;
}
.feature-card p {
  font-size: 0.88rem;
  color: #5a7a98;
  line-height: 1.65;
  margin: 0;
}

/* ═══════════════════════════════════════════════════════
   ARCHITECTURE
═══════════════════════════════════════════════════════ */
.architecture-section {
  padding: 7rem 4rem;
  background: #060d1e;
  border-top: 1px solid rgba(0,212,212,0.1);
  position: relative;
  z-index: 1;
}

.arch-pipeline {
  max-width: 820px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.arch-layer {
  display: flex;
  gap: 0;
  align-items: stretch;
  width: 100%;
}

.arch-layer-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 56px;
  flex-shrink: 0;
}

.arch-layer-num {
  font-family: 'Courier New', monospace;
  font-size: 0.65rem;
  font-weight: 700;
  color: #00d4d4;
  letter-spacing: 1px;
  background: rgba(0,212,212,0.08);
  border: 1px solid rgba(0,212,212,0.3);
  border-radius: 4px;
  padding: 3px 6px;
  flex-shrink: 0;
}

.arch-layer-line {
  flex: 1;
  width: 1px;
  background: rgba(0,212,212,0.25);
  margin: 4px auto;
}

.arch-layer-card {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-left: 1rem;
  padding: 1.25rem 1.5rem;
  border-radius: 10px;
  border: 1px solid rgba(0,212,212,0.14);
  background: rgba(8,16,36,0.6);
  backdrop-filter: blur(10px);
  transition: border-color 0.3s, box-shadow 0.3s;
}
.arch-layer-card:hover { border-color: rgba(0,212,212,0.35); box-shadow: 0 6px 24px rgba(0,212,212,0.08); }
.arch-layer-card--hardware { border-color: rgba(0,212,212,0.2); }
.arch-layer-card--backend  { border-color: rgba(0,180,255,0.18); }
.arch-layer-card--data     { border-color: rgba(168,85,247,0.18); }
.arch-layer-card--anchor   { border-color: rgba(34,197,94,0.28); background: rgba(34,197,94,0.03); }
.arch-layer-card--verify   {
  border-color: rgba(0,212,212,0.3);
  border-style: dashed;
  background: rgba(0,212,212,0.03);
  padding: 1rem 1.5rem;
}

.arch-layer-icon {
  width: 42px; height: 42px;
  flex-shrink: 0;
  border-radius: 8px;
  border: 1px solid rgba(0,212,212,0.3);
  background: rgba(0,212,212,0.06);
  display: flex; align-items: center; justify-content: center;
  color: #00d4d4;
  padding: 9px;
}
.arch-layer-icon--anchor { border-color: rgba(34,197,94,0.4); background: rgba(34,197,94,0.06); color: #22c55e; }

.arch-layer-body { flex: 1; }
.arch-layer-body h3 {
  font-size: 0.95rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: 1px;
  margin: 0.2rem 0 0.4rem;
}
.arch-layer-body p {
  font-size: 0.82rem;
  color: #5a7a98;
  margin: 0;
  line-height: 1.55;
}

.arch-layer-badge {
  font-family: 'Courier New', monospace;
  font-size: 0.6rem;
  letter-spacing: 1.5px;
  padding: 2px 7px;
  border-radius: 3px;
  display: inline-block;
  margin-bottom: 0.1rem;
}
.arch-layer-badge--hardware { background: rgba(0,212,212,0.1); color: #00d4d4; }
.arch-layer-badge--backend  { background: rgba(0,180,255,0.1); color: #00b4ff; }
.arch-layer-badge--data     { background: rgba(168,85,247,0.1); color: #c084fc; }
.arch-layer-badge--anchor   { background: rgba(34,197,94,0.1); color: #22c55e; }
.arch-layer-badge--verify   { background: rgba(0,212,212,0.08); color: #00d4d4; }

.arch-layer-status {
  display: flex; align-items: center; gap: 0.45rem;
  font-family: 'Courier New', monospace;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: #22c55e;
  flex-shrink: 0;
}
.arch-layer-status--bch { color: #22c55e; }

.arch-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
.arch-dot--green { background: #22c55e; box-shadow: 0 0 6px #22c55e; animation: pulse-green 2s ease-in-out infinite; }
.arch-dot--bch   { background: #22c55e; box-shadow: 0 0 8px #22c55e; animation: pulse-green 2s ease-in-out infinite; }

.arch-connector-vert {
  width: 20px;
  height: 40px;
  margin: 0 auto;
  flex-shrink: 0;
}
.arch-connector-vert svg { width: 100%; height: 100%; }

.arch-side-branch {
  display: flex;
  align-items: center;
  gap: 0;
  width: 100%;
  margin-top: 1.5rem;
  padding-left: 56px;
}
.arch-side-branch svg { width: 120px; flex-shrink: 0; }
.arch-side-branch .arch-layer-card { flex: 1; margin-left: 0; }

/* ═══════════════════════════════════════════════════════
   PROJECT STATUS
═══════════════════════════════════════════════════════ */
.project-status {
  padding: 7rem 4rem;
  position: relative;
  z-index: 1;
}

.timeline-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  max-width: 1100px;
  margin: 0 auto;
}

.timeline-card {
  background: rgba(8,16,36,0.6);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(0,212,212,0.14);
  border-radius: 12px;
  padding: 1.5rem;
  position: relative;
  transition: all 0.3s ease;
}
.timeline-card--active {
  border-color: rgba(0,212,212,0.25);
}
.timeline-card--active:hover {
  border-color: rgba(0,212,212,0.5);
  box-shadow: 0 8px 28px rgba(0,212,212,0.1);
  transform: translateY(-3px);
}
.timeline-card--pending {
  border-color: rgba(255,255,255,0.06);
  opacity: 0.6;
}

.timeline-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}
.timeline-indicator { display: flex; align-items: center; gap: 0.5rem; }

.tl-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
.tl-dot--active  { background: #00d4d4; box-shadow: 0 0 6px #00d4d4; animation: pulse-cyan 2s ease-in-out infinite; }
.tl-dot--pending { background: #1e3a5a; }

@keyframes pulse-cyan {
  0%,100% { box-shadow: 0 0 6px #00d4d4; }
  50%      { box-shadow: 0 0 14px #00d4d4; }
}

.tl-badge {
  font-family: 'Courier New', monospace;
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 1px;
  padding: 2px 7px;
  border-radius: 3px;
}
.tl-badge--active  { background: rgba(0,212,212,0.1); color: #00d4d4; border: 1px solid rgba(0,212,212,0.3); }
.tl-badge--pending { background: rgba(30,58,90,0.2); color: #3a5a78; border: 1px solid rgba(30,58,90,0.4); }

.tl-num {
  font-family: 'Courier New', monospace;
  font-size: 1.4rem;
  font-weight: 700;
  color: rgba(0,212,212,0.18);
  letter-spacing: 1px;
}

.tl-icon {
  width: 38px; height: 38px;
  color: #00d4d4;
  margin-bottom: 1rem;
  border-radius: 8px;
  border: 1px solid rgba(0,212,212,0.25);
  background: rgba(0,212,212,0.05);
  display: flex; align-items: center; justify-content: center;
  padding: 8px;
}
.tl-icon--dim { color: #2a4060; border-color: rgba(42,64,96,0.3); background: rgba(42,64,96,0.1); }

.tl-title { font-size: 0.95rem; font-weight: 700; color: #fff; letter-spacing: 0.5px; margin: 0 0 0.5rem; }
.tl-desc  { font-size: 0.83rem; color: #5a7a98; line-height: 1.6; margin: 0 0 1.25rem; }

.tl-progress-bar {
  height: 3px;
  border-radius: 2px;
  background: rgba(0,212,212,0.12);
  overflow: hidden;
  margin-bottom: 0.4rem;
}
.tl-progress-fill {
  height: 100%;
  border-radius: 2px;
  background: linear-gradient(90deg, #00d4d4, #00b4ff);
  box-shadow: 0 0 6px rgba(0,212,212,0.5);
  transition: width 1s ease;
}
.tl-progress-fill--pending { background: rgba(30,58,90,0.3); box-shadow: none; }

.tl-pct { font-family: 'Courier New', monospace; font-size: 0.65rem; color: #00d4d4; letter-spacing: 1px; }
.tl-pct--dim { color: #2a4060; }

/* ═══════════════════════════════════════════════════════
   TECH STACK
═══════════════════════════════════════════════════════ */
.tech-stack {
  padding: 7rem 4rem;
  background: #060d1e;
  border-top: 1px solid rgba(0,212,212,0.1);
  position: relative;
  z-index: 1;
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
  max-width: 1100px;
  margin: 0 auto;
}

.tech-card {
  background: rgba(8,16,36,0.65);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0,212,212,0.12);
  border-radius: 10px;
  padding: 1.5rem 1.25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  transition: all 0.3s ease;
  cursor: default;
}
.tech-card:hover {
  border-color: rgba(0,212,212,0.45);
  box-shadow: 0 8px 24px rgba(0,212,212,0.1);
  transform: translateY(-3px);
}
.tech-card--accent {
  border-color: rgba(34,197,94,0.28);
  background: rgba(34,197,94,0.03);
}
.tech-card--accent:hover {
  border-color: rgba(34,197,94,0.6);
  box-shadow: 0 8px 24px rgba(34,197,94,0.12);
}

.tech-card-icon {
  width: 44px; height: 44px;
  border-radius: 10px;
  border: 1px solid rgba(0,212,212,0.28);
  background: rgba(0,212,212,0.06);
  display: flex; align-items: center; justify-content: center;
  color: #00d4d4;
  padding: 10px;
}
.tech-card-icon--bch { border-color: rgba(34,197,94,0.4); background: rgba(34,197,94,0.06); color: #22c55e; }

.tech-card-name {
  font-size: 0.9rem;
  font-weight: 700;
  color: #e0e8f0;
  letter-spacing: 0.5px;
  text-align: center;
}
.tech-card-layer {
  font-family: 'Courier New', monospace;
  font-size: 0.6rem;
  letter-spacing: 1.5px;
  color: #00d4d4;
  opacity: 0.6;
  text-transform: uppercase;
}
.tech-card-layer--bch { color: #22c55e; opacity: 0.8; }

/* ═══════════════════════════════════════════════════════
   CTA SECTION
═══════════════════════════════════════════════════════ */
.cta-section {
  padding: 8rem 4rem;
  position: relative;
  z-index: 1;
  overflow: hidden;
  border-top: 1px solid rgba(0,212,212,0.1);
}
.cta-grid-overlay {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(0,212,212,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,212,212,0.03) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
}
.cta-glow {
  position: absolute;
  width: 600px; height: 600px;
  border-radius: 50%;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle, rgba(0,180,200,0.07) 0%, transparent 65%);
  pointer-events: none;
}

.cta-inner {
  max-width: 720px;
  margin: 0 auto;
  text-align: center;
  position: relative;
  z-index: 2;
}

.cta-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  font-family: 'Courier New', monospace;
  font-size: 0.68rem;
  letter-spacing: 2px;
  color: #00d4d4;
  border: 1px solid rgba(0,212,212,0.3);
  border-radius: 20px;
  padding: 0.4rem 1rem;
  margin-bottom: 2rem;
  background: rgba(0,212,212,0.04);
}

.cta-title {
  font-size: clamp(2rem, 4vw, 3.5rem);
  font-weight: 800;
  line-height: 1.1;
  color: #fff;
  margin: 0 0 1.5rem;
  letter-spacing: -0.5px;
}

.cta-desc {
  font-size: 1.05rem;
  color: #5a7a98;
  margin: 0 auto 2.5rem;
  max-width: 560px;
  line-height: 1.7;
}

.cta-actions { justify-content: center; margin-bottom: 3rem; }

.cta-stats {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  border: 1px solid rgba(0,212,212,0.16);
  border-radius: 10px;
  background: rgba(8,16,36,0.6);
  backdrop-filter: blur(10px);
  overflow: hidden;
  max-width: 540px;
  margin: 0 auto;
}
.cta-stat { flex: 1; padding: 1rem 1.25rem; text-align: center; }
.cta-stat-value {
  display: block;
  font-family: 'Courier New', monospace;
  font-size: 0.85rem;
  font-weight: 700;
  color: #00d4d4;
  letter-spacing: 1px;
  margin-bottom: 0.3rem;
}
.cta-stat-label {
  display: block;
  font-size: 0.6rem;
  letter-spacing: 1.5px;
  color: #3a5a78;
  text-transform: uppercase;
  font-family: 'Courier New', monospace;
}
.cta-stat-divider { width: 1px; background: rgba(0,212,212,0.15); align-self: stretch; }

/* ═══════════════════════════════════════════════════════
   FOOTER
═══════════════════════════════════════════════════════ */
.landing-footer {
  background: #030812;
  border-top: 1px solid rgba(0,212,212,0.12);
  position: relative;
  z-index: 1;
}

.footer-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 3rem;
  padding: 4rem 4rem 3rem;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  max-width: 1200px;
  margin: 0 auto;
}

.footer-brand {}

.footer-logo-wrap {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  margin-bottom: 0.4rem;
}
.footer-wordmark {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 3px;
  color: #fff;
}
.footer-tagline {
  font-family: 'Courier New', monospace;
  font-size: 0.62rem;
  letter-spacing: 2px;
  color: #00d4d4;
  margin: 0 0 1rem;
  opacity: 0.7;
}
.footer-about {
  font-size: 0.85rem;
  color: #3a5a78;
  line-height: 1.65;
  margin: 0;
  max-width: 280px;
}

.footer-links-col {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.footer-col-title {
  font-family: 'Courier New', monospace;
  font-size: 0.62rem;
  letter-spacing: 2px;
  color: #00d4d4;
  opacity: 0.6;
  margin-bottom: 0.4rem;
  text-transform: uppercase;
}
.footer-link {
  font-size: 0.85rem;
  color: #3a5a78;
  text-decoration: none;
  transition: color 0.2s;
  cursor: pointer;
}
.footer-link:hover { color: #00d4d4; }

.footer-tech-tag {
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
  color: #3a5a78;
  letter-spacing: 0.5px;
}
.footer-tech-tag--bch { color: #22c55e; opacity: 0.8; }

.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 4rem;
  max-width: 1200px;
  margin: 0 auto;
}
.footer-bottom-left {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.footer-status-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 6px #22c55e;
  animation: pulse-green 2s ease-in-out infinite;
}
.footer-status-text {
  font-family: 'Courier New', monospace;
  font-size: 0.62rem;
  letter-spacing: 1.5px;
  color: #22c55e;
  opacity: 0.7;
}
.footer-copy {
  font-size: 0.78rem;
  color: #2a3f55;
  text-align: center;
  margin: 0;
}
.footer-bottom-hash {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.footer-hash-label {
  font-family: 'Courier New', monospace;
  font-size: 0.58rem;
  letter-spacing: 1px;
  color: #2a3f55;
}
.footer-hash-value {
  font-family: 'Courier New', monospace;
  font-size: 0.65rem;
  color: #00d4d4;
  opacity: 0.5;
  letter-spacing: 0.5px;
}

/* ═══════════════════════════════════════════════════════
   RESPONSIVE
═══════════════════════════════════════════════════════ */
@media (max-width: 1100px) {
  .hero-section { flex-direction: column; padding: 10rem 2.5rem 4rem; gap: 3rem; }
  .hero-left, .hero-right { flex: unset; max-width: 100%; width: 100%; }
  .metrics-panel { max-width: 100%; }
  .features-grid { grid-template-columns: repeat(2, 1fr); }
  .timeline-grid  { grid-template-columns: repeat(2, 1fr); }
  .tech-grid       { grid-template-columns: repeat(3, 1fr); }
  .footer-top      { grid-template-columns: 1fr 1fr; }
  .landing-header  { padding: 0.9rem 2rem; }
  .arch-side-branch { padding-left: 0; flex-direction: column; }
  .arch-side-branch svg { display: none; }
}

@media (max-width: 768px) {
  .landing-nav { display: none; }
  .features-grid { grid-template-columns: 1fr; }
  .timeline-grid  { grid-template-columns: 1fr; }
  .tech-grid       { grid-template-columns: repeat(2, 1fr); }
  .footer-top      { grid-template-columns: 1fr; gap: 2rem; padding: 2.5rem 1.5rem; }
  .footer-bottom   { flex-direction: column; gap: 0.75rem; padding: 1.25rem 1.5rem; text-align: center; }
  .hero-title { font-size: 2.4rem; }
  .cta-title  { font-size: 2rem; }
  .metrics-panel { flex-direction: column; }
  .metric-divider { width: auto; height: 1px; align-self: stretch; }
  .hero-section, .how-it-works, .features-section,
  .architecture-section, .project-status,
  .tech-stack, .cta-section { padding: 4rem 1.5rem; }
  .cta-stats { flex-direction: column; }
  .cta-stat-divider { width: auto; height: 1px; align-self: stretch; }
  .process-step { flex-direction: column; }
  .step-number-wrap { flex-direction: row; width: auto; }
  .step-connector { flex: none; height: 1px; width: 24px; margin: auto 0; background: rgba(0,212,212,0.3); }
  .step-card { margin-left: 0; }
  .arch-layer { flex-direction: column; }
  .arch-layer-side { flex-direction: row; width: auto; }
  .arch-layer-line { flex: none; width: 24px; height: 1px; }
  .arch-layer-card { margin-left: 0; }
}
</style>
