<template>
  <div class="landing-page">

    <!-- ═══════════════════════════════════════════════
         NAVIGATION
    ═══════════════════════════════════════════════ -->
    <nav id="landing-nav" :class="['landing-nav', { 'nav-scrolled': isScrolled }]" aria-label="Main navigation">
      <div class="nav-inner">
        <a href="#" class="nav-logo" aria-label="ChainTrace home">
          <svg class="logo-icon" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <polygon points="18,2 33,9.5 33,26.5 18,34 3,26.5 3,9.5" fill="none" stroke="#3B82F6" stroke-width="1.2"/>
            <polygon points="18,7 28,12.5 28,23.5 18,29 8,23.5 8,12.5" fill="none" stroke="rgba(59,130,246,0.3)" stroke-width="0.8"/>
            <circle cx="13" cy="16" r="2.5" fill="none" stroke="#06B6D4" stroke-width="1.2"/>
            <circle cx="23" cy="16" r="2.5" fill="none" stroke="#06B6D4" stroke-width="1.2"/>
            <line x1="15.5" y1="16" x2="20.5" y2="16" stroke="#06B6D4" stroke-width="1.2"/>
            <circle cx="18" cy="21" r="2" fill="none" stroke="#3B82F6" stroke-width="1"/>
            <line x1="13" y1="18.5" x2="16.6" y2="19.6" stroke="#3B82F6" stroke-width="0.8"/>
            <line x1="23" y1="18.5" x2="19.4" y2="19.6" stroke="#3B82F6" stroke-width="0.8"/>
          </svg>
          <span class="nav-wordmark">CHAINTRACE</span>
        </a>

        <ul class="nav-links">
          <li><a href="#architecture">Research</a></li>
          <li><a href="#architecture">Architecture</a></li>
          <li><a href="#verification">Verification</a></li>
          <li><a href="#features">Hardware</a></li>
          <li><a href="#timeline">Documentation</a></li>
          <li><a href="#footer">Contact</a></li>
        </ul>

        <div class="nav-cta">
          <router-link to="/dashboard" class="btn-primary-nav">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/>
              <rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>
            </svg>
            Open Dashboard
          </router-link>
        </div>
      </div>
    </nav>

    <!-- ═══════════════════════════════════════════════
         HERO
    ═══════════════════════════════════════════════ -->
    <section id="home" class="hero-section" aria-label="Hero">
      <div class="blueprint-bg" aria-hidden="true"></div>
      <div class="hero-glow-l" aria-hidden="true"></div>
      <div class="hero-glow-r" aria-hidden="true"></div>

      <div class="container">
        <div class="hero-inner">

          <!-- Left -->
          <div class="hero-left">
            <span class="label">Blockchain-Backed Chain-of-Custody Research</span>
            <h1 class="hero-headline">
              Proving custody with <span class="gradient-text">cryptographic evidence.</span>
            </h1>
            <p class="hero-para">
              ChainTrace combines custom ESP32 IoT hardware, SHA-256 hashing, and Bitcoin Cash blockchain anchoring to create tamper-evident custody records that can be independently verified by anyone.
            </p>
            <div class="hero-btns">
              <a href="#architecture" class="btn btn-primary">
                <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12,8 16,12 12,16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
                View Architecture
              </a>
              <router-link to="/verify" class="btn btn-ghost">
                <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                Verify Record
              </router-link>
            </div>
          </div>

          <!-- Right — ESP32 Hardware Diagram -->
          <div class="hero-right" aria-label="ESP32 scan node hardware diagram">
            <div class="hw-diagram">
              <!-- Floating component callouts -->
              <div class="hw-comp hw-comp-1"><div class="comp-name">Microcontroller</div><div class="comp-val">ESP32-WROOM-32</div></div>
              <div class="hw-comp hw-comp-2"><div class="comp-name">RFID Reader</div><div class="comp-val">RC522 / 13.56 MHz</div></div>
              <div class="hw-comp hw-comp-3"><div class="comp-name">Real-Time Clock</div><div class="comp-val">DS3231 ±2ppm</div></div>
              <div class="hw-comp hw-comp-4"><div class="comp-name">IMU Sensor</div><div class="comp-val">MPU6050 6-DOF</div></div>
              <div class="hw-comp hw-comp-5"><div class="comp-name">Tamper Switch</div><div class="comp-val">SPDT / Active Low</div></div>
              <div class="hw-comp hw-comp-6"><div class="comp-name">Battery</div><div class="comp-val">Li-Ion 3.7V 2000mAh</div></div>

              <!-- PCB SVG -->
              <svg class="pcb-svg" viewBox="0 0 280 240" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <rect x="20" y="20" width="240" height="200" rx="12" fill="#061810" stroke="rgba(0,200,80,0.3)" stroke-width="1.5"/>
                <circle cx="36" cy="36" r="4" fill="none" stroke="rgba(0,200,80,0.2)" stroke-width="1"/>
                <circle cx="244" cy="36" r="4" fill="none" stroke="rgba(0,200,80,0.2)" stroke-width="1"/>
                <circle cx="36" cy="204" r="4" fill="none" stroke="rgba(0,200,80,0.2)" stroke-width="1"/>
                <circle cx="244" cy="204" r="4" fill="none" stroke="rgba(0,200,80,0.2)" stroke-width="1"/>
                <path d="M85 120 L110 120 L110 95 L140 95" stroke="rgba(0,200,80,0.18)" stroke-width="1" fill="none"/>
                <path d="M85 130 L110 130 L110 155 L140 155" stroke="rgba(0,200,80,0.13)" stroke-width="1" fill="none"/>
                <path d="M195 120 L170 120 L170 95 L140 95" stroke="rgba(0,200,80,0.18)" stroke-width="1" fill="none"/>
                <path d="M195 130 L170 130 L170 155 L140 155" stroke="rgba(0,200,80,0.13)" stroke-width="1" fill="none"/>
                <circle cx="110" cy="95" r="2.5" fill="rgba(0,200,80,0.3)" stroke="rgba(0,200,80,0.6)" stroke-width="0.8"/>
                <circle cx="110" cy="155" r="2.5" fill="rgba(0,200,80,0.3)" stroke="rgba(0,200,80,0.6)" stroke-width="0.8"/>
                <circle cx="170" cy="95" r="2.5" fill="rgba(0,200,80,0.3)" stroke="rgba(0,200,80,0.6)" stroke-width="0.8"/>
                <circle cx="170" cy="155" r="2.5" fill="rgba(0,200,80,0.3)" stroke="rgba(0,200,80,0.6)" stroke-width="0.8"/>
                <rect x="115" y="95" width="50" height="50" rx="3" fill="#1a1a2e" stroke="rgba(100,100,150,0.6)" stroke-width="1"/>
                <rect x="120" y="100" width="40" height="40" rx="2" fill="#0d0d1a" stroke="rgba(80,80,120,0.4)" stroke-width="0.5"/>
                <text x="140" y="124" text-anchor="middle" font-family="monospace" font-size="7" fill="rgba(150,150,200,0.7)">ESP32</text>
                <line x1="160" y1="100" x2="165" y2="100" stroke="rgba(100,100,150,0.4)" stroke-width="0.8"/>
                <line x1="160" y1="108" x2="167" y2="108" stroke="rgba(100,100,150,0.4)" stroke-width="0.8"/>
                <line x1="160" y1="116" x2="165" y2="116" stroke="rgba(100,100,150,0.4)" stroke-width="0.8"/>
                <rect x="20" y="88" width="4" height="64" fill="none" stroke="rgba(0,200,80,0.15)" stroke-width="0.8"/>
                <line x1="22" y1="96" x2="22" y2="100" stroke="rgba(200,160,0,0.35)" stroke-width="1.5"/>
                <line x1="22" y1="110" x2="22" y2="114" stroke="rgba(200,160,0,0.35)" stroke-width="1.5"/>
                <line x1="22" y1="124" x2="22" y2="128" stroke="rgba(200,160,0,0.35)" stroke-width="1.5"/>
                <line x1="22" y1="138" x2="22" y2="142" stroke="rgba(200,160,0,0.35)" stroke-width="1.5"/>
                <rect x="256" y="88" width="4" height="64" fill="none" stroke="rgba(0,200,80,0.15)" stroke-width="0.8"/>
                <line x1="258" y1="96" x2="258" y2="100" stroke="rgba(200,160,0,0.35)" stroke-width="1.5"/>
                <line x1="258" y1="110" x2="258" y2="114" stroke="rgba(200,160,0,0.35)" stroke-width="1.5"/>
                <line x1="258" y1="124" x2="258" y2="128" stroke="rgba(200,160,0,0.35)" stroke-width="1.5"/>
                <text x="36" y="78" text-anchor="middle" font-family="monospace" font-size="5.5" fill="rgba(6,182,212,0.6)">RC522</text>
                <text x="244" y="78" text-anchor="middle" font-family="monospace" font-size="5.5" fill="rgba(6,182,212,0.6)">DS3231</text>
                <text x="36" y="200" text-anchor="middle" font-family="monospace" font-size="5.5" fill="rgba(6,182,212,0.6)">MPU6050</text>
                <text x="244" y="200" text-anchor="middle" font-family="monospace" font-size="5.5" fill="rgba(6,182,212,0.6)">LiPo PWR</text>
                <rect x="26" y="26" width="228" height="188" rx="6" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="0.8" stroke-dasharray="4 4"/>
                <text x="140" y="16" text-anchor="middle" font-family="monospace" font-size="6.5" fill="rgba(0,200,80,0.35)" letter-spacing="2">CHAINTRACE-NODE-v1.0</text>
              </svg>

              <div class="hw-badge">Custom ESP32 Scan Node — KiCad Design</div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         METRICS
    ═══════════════════════════════════════════════ -->
    <section id="metrics" class="metrics-section" aria-label="Key statistics">
      <div class="container">
        <div class="metrics-grid">
          <div class="metric-card">
            <svg class="metric-icon" viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><rect x="8" y="12" width="24" height="18" rx="2"/><path d="M14 12V9a6 6 0 0112 0v3"/><circle cx="20" cy="22" r="2.5" fill="currentColor" stroke="none"/><line x1="20" y1="24.5" x2="20" y2="27"/></svg>
            <div class="metric-value">256-bit</div>
            <div class="metric-label">SHA-256 Integrity Hashing</div>
          </div>
          <div class="metric-card">
            <svg class="metric-icon" viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><rect x="4" y="10" width="14" height="10" rx="2"/><rect x="22" y="10" width="14" height="10" rx="2"/><rect x="4" y="24" width="14" height="10" rx="2"/><rect x="22" y="24" width="14" height="10" rx="2"/><line x1="18" y1="15" x2="22" y2="15"/><line x1="11" y1="20" x2="11" y2="24"/><line x1="29" y1="20" x2="29" y2="24"/><line x1="18" y1="29" x2="22" y2="29"/></svg>
            <div class="metric-value">BCH</div>
            <div class="metric-label">OP_RETURN Blockchain Anchoring</div>
          </div>
          <div class="metric-card">
            <svg class="metric-icon" viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><circle cx="20" cy="20" r="14"/><polyline points="20,10 20,20 26,26"/><line x1="6" y1="20" x2="9" y2="20"/><line x1="31" y1="20" x2="34" y2="20"/><line x1="20" y1="6" x2="20" y2="9"/></svg>
            <div class="metric-value">RTC</div>
            <div class="metric-label">Offline Timestamp Support</div>
          </div>
          <div class="metric-card">
            <svg class="metric-icon" viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><path d="M20 6l2.5 7.5H30l-6 4.5 2.5 7.5L20 21l-6.5 4.5 2.5-7.5-6-4.5h7.5z"/><circle cx="20" cy="20" r="16" stroke-dasharray="3 3"/></svg>
            <div class="metric-value">Public</div>
            <div class="metric-label">Independent Verification</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         ARCHITECTURE
    ═══════════════════════════════════════════════ -->
    <section id="architecture" class="arch-section" aria-label="System architecture">
      <div class="blueprint-bg" aria-hidden="true" style="opacity:0.4;"></div>
      <div class="container" style="position:relative;z-index:2;">
        <div class="section-header">
          <span class="label">System Architecture</span>
          <h2 class="section-title" style="margin-top:20px;">End-to-end data flow</h2>
          <p class="section-sub" style="margin-top:16px;">From physical RFID scan to immutable blockchain record — every step is cryptographically linked.</p>
        </div>

        <!-- Primary flow -->
        <div class="arch-flow" role="list" aria-label="Primary data flow">
          <div class="arch-node" role="listitem" v-for="(node, i) in archNodes" :key="i">
            <div class="arch-node-icon" v-html="node.icon"></div>
            <div class="arch-node-title">{{ node.title }}</div>
            <div class="arch-node-sub">{{ node.sub }}</div>
          </div>
          <!-- Arrows are rendered between nodes via CSS/flex pseudo -->
        </div>

        <!-- Arrows row (separate for clean layout) -->
        <div class="arch-arrows-row" aria-hidden="true">
          <div class="arch-arrow-line" v-for="i in 5" :key="i">
            <div class="arch-pulse" :style="{ animationDelay: (i * 0.35) + 's' }"></div>
          </div>
        </div>

        <!-- Verification path -->
        <div class="arch-verify" aria-label="Verification data flow">
          <div class="arch-node arch-node-cyan" v-for="(node, i) in verifyNodes" :key="i">
            <div class="arch-node-icon" v-html="node.icon"></div>
            <div class="arch-node-title">{{ node.title }}</div>
            <div class="arch-node-sub">{{ node.sub }}</div>
          </div>
        </div>
        <div class="arch-verify-label">INDEPENDENT VERIFICATION PATH</div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         FEATURES / RESEARCH HIGHLIGHTS
    ═══════════════════════════════════════════════ -->
    <section id="features" class="features-section" aria-label="Research highlights">
      <div class="container">
        <div class="section-header">
          <span class="label">Research Highlights</span>
          <h2 class="section-title" style="margin-top:20px;">Three pillars of custody integrity</h2>
        </div>
        <div class="features-grid">

          <!-- Hardware Integrity -->
          <div class="feature-card fade-up">
            <div class="feature-illustration" aria-label="Hardware schematic diagram">
              <svg viewBox="0 0 320 160" fill="none" style="width:100%;height:100%;" aria-hidden="true">
                <rect x="60" y="20" width="200" height="120" rx="8" fill="none" stroke="rgba(59,130,246,0.2)" stroke-width="1" stroke-dasharray="3 3"/>
                <rect x="120" y="55" width="80" height="50" rx="3" fill="rgba(59,130,246,0.05)" stroke="rgba(59,130,246,0.28)" stroke-width="1"/>
                <text x="160" y="83" text-anchor="middle" font-family="monospace" font-size="8" fill="rgba(59,130,246,0.55)">ESP32</text>
                <rect x="68" y="35" width="40" height="25" rx="2" fill="rgba(6,182,212,0.04)" stroke="rgba(6,182,212,0.22)" stroke-width="0.8"/>
                <text x="88" y="51" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(6,182,212,0.45)">RC522</text>
                <rect x="212" y="35" width="40" height="25" rx="2" fill="rgba(6,182,212,0.04)" stroke="rgba(6,182,212,0.22)" stroke-width="0.8"/>
                <text x="232" y="51" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(6,182,212,0.45)">DS3231</text>
                <rect x="68" y="100" width="40" height="25" rx="2" fill="rgba(6,182,212,0.04)" stroke="rgba(6,182,212,0.22)" stroke-width="0.8"/>
                <text x="88" y="116" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(6,182,212,0.45)">MPU6050</text>
                <rect x="212" y="100" width="40" height="25" rx="2" fill="rgba(6,182,212,0.04)" stroke="rgba(6,182,212,0.22)" stroke-width="0.8"/>
                <text x="232" y="116" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(6,182,212,0.45)">TAMPER</text>
                <line x1="108" y1="47" x2="120" y2="72" stroke="rgba(59,130,246,0.18)" stroke-width="0.8"/>
                <line x1="212" y1="47" x2="200" y2="72" stroke="rgba(59,130,246,0.18)" stroke-width="0.8"/>
                <line x1="108" y1="112" x2="120" y2="95" stroke="rgba(59,130,246,0.18)" stroke-width="0.8"/>
                <line x1="212" y1="112" x2="200" y2="95" stroke="rgba(59,130,246,0.18)" stroke-width="0.8"/>
              </svg>
            </div>
            <h3 class="feature-title">Hardware Integrity</h3>
            <p class="feature-desc">Custom PCB designed in KiCad integrates RFID scanning, real-time tamper detection via hardware switches, 6-DOF motion sensing, and offline RTC timestamps.</p>
            <div class="feature-tags">
              <span class="feature-tag">Custom PCB</span>
              <span class="feature-tag">RFID</span>
              <span class="feature-tag">Tamper Detection</span>
              <span class="feature-tag">MPU6050</span>
              <span class="feature-tag">DS3231</span>
            </div>
          </div>

          <!-- Blockchain Anchoring -->
          <div class="feature-card fade-up">
            <div class="feature-illustration" aria-label="Blockchain anchoring diagram">
              <svg viewBox="0 0 320 160" fill="none" style="width:100%;height:100%;" aria-hidden="true">
                <rect x="20" y="60" width="60" height="40" rx="4" fill="rgba(59,130,246,0.05)" stroke="rgba(59,130,246,0.28)" stroke-width="1"/>
                <text x="50" y="77" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(59,130,246,0.45)">BLOCK</text>
                <text x="50" y="88" text-anchor="middle" font-family="monospace" font-size="5" fill="rgba(59,130,246,0.3)">#849120</text>
                <line x1="80" y1="80" x2="100" y2="80" stroke="rgba(59,130,246,0.25)" stroke-width="1"/>
                <polygon points="98,76 106,80 98,84" fill="rgba(59,130,246,0.25)"/>
                <rect x="110" y="60" width="60" height="40" rx="4" fill="rgba(59,130,246,0.05)" stroke="rgba(59,130,246,0.28)" stroke-width="1"/>
                <text x="140" y="77" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(59,130,246,0.45)">BLOCK</text>
                <text x="140" y="88" text-anchor="middle" font-family="monospace" font-size="5" fill="rgba(59,130,246,0.3)">#849121</text>
                <line x1="170" y1="80" x2="190" y2="80" stroke="rgba(59,130,246,0.25)" stroke-width="1"/>
                <polygon points="188,76 196,80 188,84" fill="rgba(59,130,246,0.25)"/>
                <rect x="200" y="55" width="70" height="50" rx="4" fill="rgba(59,130,246,0.1)" stroke="rgba(59,130,246,0.45)" stroke-width="1.2"/>
                <text x="235" y="72" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(59,130,246,0.7)">BLOCK</text>
                <text x="235" y="82" text-anchor="middle" font-family="monospace" font-size="5" fill="rgba(59,130,246,0.55)">#849122</text>
                <text x="235" y="96" text-anchor="middle" font-family="monospace" font-size="5.5" fill="rgba(6,182,212,0.75)">OP_RETURN</text>
                <text x="235" y="120" text-anchor="middle" font-family="monospace" font-size="5" fill="rgba(6,182,212,0.45)">sha256:a3f9...</text>
                <rect x="90" y="25" width="140" height="22" rx="3" fill="rgba(6,182,212,0.03)" stroke="rgba(6,182,212,0.13)" stroke-width="0.8"/>
                <text x="160" y="40" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(6,182,212,0.45)">SHA-256(payload) → anchor tx</text>
                <line x1="235" y1="47" x2="235" y2="55" stroke="rgba(6,182,212,0.18)" stroke-width="0.8" stroke-dasharray="2 2"/>
              </svg>
            </div>
            <h3 class="feature-title">Blockchain Anchoring</h3>
            <p class="feature-desc">Each custody event is SHA-256 hashed and permanently embedded into the Bitcoin Cash blockchain via OP_RETURN transactions — creating immutable, censorship-resistant audit trails.</p>
            <div class="feature-tags">
              <span class="feature-tag">SHA-256</span>
              <span class="feature-tag">OP_RETURN</span>
              <span class="feature-tag">Bitcoin Cash</span>
              <span class="feature-tag">Immutable</span>
            </div>
          </div>

          <!-- Independent Verification -->
          <div class="feature-card fade-up">
            <div class="feature-illustration" aria-label="Independent verification flow">
              <svg viewBox="0 0 320 160" fill="none" style="width:100%;height:100%;" aria-hidden="true">
                <circle cx="60" cy="80" r="20" fill="rgba(59,130,246,0.05)" stroke="rgba(59,130,246,0.22)" stroke-width="1"/>
                <text x="60" y="84" text-anchor="middle" font-family="monospace" font-size="8" fill="rgba(59,130,246,0.45)">USR</text>
                <line x1="80" y1="80" x2="120" y2="80" stroke="rgba(59,130,246,0.2)" stroke-width="0.8" stroke-dasharray="3 3"/>
                <rect x="120" y="60" width="80" height="40" rx="4" fill="rgba(59,130,246,0.07)" stroke="rgba(59,130,246,0.32)" stroke-width="1"/>
                <text x="160" y="77" text-anchor="middle" font-family="monospace" font-size="7" fill="rgba(59,130,246,0.65)">VERIFY</text>
                <text x="160" y="89" text-anchor="middle" font-family="monospace" font-size="5.5" fill="rgba(59,130,246,0.4)">Hash Compare</text>
                <line x1="200" y1="80" x2="240" y2="80" stroke="rgba(59,130,246,0.2)" stroke-width="0.8" stroke-dasharray="3 3"/>
                <circle cx="265" cy="80" r="22" fill="rgba(59,130,246,0.05)" stroke="rgba(59,130,246,0.22)" stroke-width="1"/>
                <text x="265" y="77" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(59,130,246,0.45)">BCH</text>
                <text x="265" y="87" text-anchor="middle" font-family="monospace" font-size="5.5" fill="rgba(6,182,212,0.4)">CHAIN</text>
                <circle cx="160" cy="130" r="12" fill="rgba(34,197,94,0.08)" stroke="rgba(34,197,94,0.3)" stroke-width="1"/>
                <polyline points="154,130 158,134 167,124" stroke="rgba(34,197,94,0.7)" stroke-width="1.5" fill="none"/>
                <text x="160" y="152" text-anchor="middle" font-family="monospace" font-size="6" fill="rgba(34,197,94,0.55)">VERIFIED</text>
                <line x1="160" y1="100" x2="160" y2="118" stroke="rgba(34,197,94,0.18)" stroke-width="0.8" stroke-dasharray="2 2"/>
              </svg>
            </div>
            <h3 class="feature-title">Independent Verification</h3>
            <p class="feature-desc">Any party can cryptographically verify a custody record using the public verification portal — comparing SHA-256 payload hashes against OP_RETURN data on the Bitcoin Cash blockchain.</p>
            <div class="feature-tags">
              <span class="feature-tag">Public Portal</span>
              <span class="feature-tag">Hash Comparison</span>
              <span class="feature-tag">Audit-Ready</span>
              <span class="feature-tag">Zero Trust</span>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         VERIFICATION CONSOLE
    ═══════════════════════════════════════════════ -->
    <section id="verification" class="verify-section" aria-label="Verification console">
      <div class="blueprint-bg" style="opacity:0.3;" aria-hidden="true"></div>
      <div class="container" style="position:relative;z-index:2;">
        <div class="section-header">
          <span class="label">Verification Console</span>
          <h2 class="section-title" style="margin-top:20px;">Verify any custody record</h2>
          <p class="section-sub" style="margin-top:16px;">Enter a transaction ID and payload hash to cryptographically verify a custody event against the Bitcoin Cash blockchain.</p>
        </div>

        <div class="verify-inner">

          <!-- Input Panel -->
          <div class="verify-panel">
            <div class="verify-panel-title">Query Parameters</div>

            <div class="form-group">
              <label class="form-label" for="txid-input">Transaction ID</label>
              <input id="txid-input" v-model="txid" class="form-input" type="text" placeholder="a3f9c82e1b4d7f0e..." />
            </div>

            <div class="form-group">
              <label class="form-label" for="hash-input">Payload Hash (SHA-256)</label>
              <input id="hash-input" v-model="payloadHash" class="form-input" type="text" placeholder="sha256:..." />
            </div>

            <div class="form-group">
              <label class="form-label" for="network-select">Network</label>
              <select id="network-select" v-model="network" class="form-input">
                <option value="chipnet">BCH Chipnet (Testnet)</option>
                <option value="mainnet">BCH Mainnet</option>
              </select>
            </div>

            <button id="verify-btn" class="btn-verify" @click="runVerification" :disabled="verifying">
              <svg v-if="!verifying" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
              <svg v-else class="spin" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" opacity="0.25"/><path d="M21 12a9 9 0 00-9-9"/></svg>
              {{ verifying ? 'Verifying...' : 'Verify Record' }}
            </button>

            <!-- Terminal output -->
            <div v-if="terminalLines.length > 0" class="terminal-output">
              <div class="terminal-header">$ chaintrace verify --txid ...</div>
              <div v-for="(line, i) in terminalLines" :key="i" class="terminal-line" v-html="'&#8250; ' + line"></div>
            </div>
          </div>

          <!-- Result Card -->
          <div class="verify-result">
            <div class="verify-panel-title">Verification Result</div>
            <div class="verify-status">
              <div class="status-badge">
                <div class="status-dot"></div>
                VERIFIED
              </div>
              <span class="status-confirm">Blockchain Confirmed</span>
            </div>
            <div class="verify-field"><span class="vf-key">Block Height</span><span class="vf-val accent">849,122</span></div>
            <div class="verify-field"><span class="vf-key">Timestamp</span><span class="vf-val">2025-08-01 14:23:07 UTC</span></div>
            <div class="verify-field"><span class="vf-key">OP_RETURN Hash</span><span class="vf-val" style="font-size:10px;">7f83b165...9069</span></div>
            <div class="verify-field"><span class="vf-key">Payload Match</span><span class="vf-val green">✓ Exact Match</span></div>
            <div class="verify-field"><span class="vf-key">Network</span><span class="vf-val accent">BCH Chipnet</span></div>
            <div class="verify-field"><span class="vf-key">Confirmations</span><span class="vf-val">1,847</span></div>
            <div class="verify-field"><span class="vf-key">Scan Node</span><span class="vf-val" style="font-size:10px;">NODE-A3:4F:2E</span></div>
            <div class="verify-note">
              The custody record at block #849,122 matches the submitted SHA-256 payload hash exactly. This record has been independently confirmed by 1,847 Bitcoin Cash network nodes.
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         TIMELINE
    ═══════════════════════════════════════════════ -->
    <section id="timeline" class="timeline-section" aria-label="Development timeline">
      <div class="container">
        <div class="timeline-inner">

          <div class="timeline-left">
            <span class="label">Project Timeline</span>
            <h2 class="section-title" style="margin-top:20px;">Research &amp; development phases</h2>
            <p class="section-sub" style="margin-top:16px;font-size:15px;">A structured capstone thesis progression from literature review through evaluation and final defense.</p>
            <div class="progress-card">
              <div class="progress-header">
                <span>Overall Completion</span>
                <span class="progress-pct">71%</span>
              </div>
              <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width:71%"></div>
              </div>
            </div>
          </div>

          <div class="timeline-track">
            <div class="timeline-item" v-for="(phase, i) in phases" :key="i">
              <div :class="['tl-dot', phase.status]"></div>
              <div class="tl-phase">Phase 0{{ i + 1 }}</div>
              <div class="tl-title">{{ phase.title }}</div>
              <span :class="['tl-status', phase.status]">{{ phase.label }}</span>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         TECH STACK
    ═══════════════════════════════════════════════ -->
    <section id="tech" class="tech-section" aria-label="Technology stack">
      <div class="container">
        <span class="label">Technology Stack</span>
        <h2 class="section-title" style="margin-top:20px;">Built on proven foundations</h2>
        <div class="tech-grid">
          <div class="tech-card" v-for="tech in techStack" :key="tech.name">
            <div class="tech-icon" v-html="tech.icon" aria-hidden="true"></div>
            <div class="tech-name">{{ tech.name }}</div>
            <div class="tech-sub">{{ tech.sub }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         CTA
    ═══════════════════════════════════════════════ -->
    <section id="cta" class="cta-section" aria-label="Call to action">
      <div class="blueprint-bg" style="opacity:0.2;" aria-hidden="true"></div>
      <div class="cta-glow" aria-hidden="true"></div>
      <div class="container" style="position:relative;z-index:2;text-align:center;">
        <span class="label">Capstone Thesis — Eastern Samar State University</span>
        <h2 class="cta-headline">
          Trust the evidence.<br/>
          <span class="gradient-text">Verify the chain.</span>
        </h2>
        <p class="cta-sub">Built for forensic accountability, academic research, and secure asset custody.</p>
        <div class="cta-btns">
          <a href="#architecture" class="btn btn-primary">Explore the Research</a>
          <router-link to="/verify" class="btn btn-outline">Open Verification Portal</router-link>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         FOOTER
    ═══════════════════════════════════════════════ -->
    <footer id="footer" class="landing-footer" role="contentinfo">
      <div class="footer-inner">
        <div class="footer-brand">
          <div class="footer-logo-row">
            <svg width="28" height="28" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
              <polygon points="18,2 33,9.5 33,26.5 18,34 3,26.5 3,9.5" fill="none" stroke="#3B82F6" stroke-width="1.2"/>
              <circle cx="13" cy="16" r="2.5" fill="none" stroke="#06B6D4" stroke-width="1.2"/>
              <circle cx="23" cy="16" r="2.5" fill="none" stroke="#06B6D4" stroke-width="1.2"/>
              <line x1="15.5" y1="16" x2="20.5" y2="16" stroke="#06B6D4" stroke-width="1.2"/>
            </svg>
            <span class="footer-wordmark">CHAINTRACE</span>
          </div>
          <div class="footer-inst">
            Eastern Samar State University<br/>
            College of Engineering — Capstone Project
          </div>
        </div>
        <ul class="footer-links">
          <li><a href="https://github.com/" target="_blank" rel="noopener noreferrer">GitHub</a></li>
          <li><a href="#timeline">Documentation</a></li>
          <li><a href="mailto:chaintrace@essu.edu.ph">Email</a></li>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
        </ul>
        <div class="footer-copy">
          © 2025 ChainTrace. Capstone Thesis.<br/>All rights reserved.
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// ── Nav scroll ──────────────────────────────────────────────────────────────
const isScrolled = ref(false)
const handleScroll = () => { isScrolled.value = window.scrollY > 20 }
onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  setupFadeObserver()
})
onUnmounted(() => window.removeEventListener('scroll', handleScroll))

// ── Fade-up observer ────────────────────────────────────────────────────────
function setupFadeObserver() {
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target) } })
  }, { threshold: 0.15 })
  document.querySelectorAll('.fade-up').forEach(el => obs.observe(el))
}

// ── Architecture data ───────────────────────────────────────────────────────
const archNodes = [
  { icon: `<svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="rgba(59,130,246,0.8)" stroke-width="1.5"><rect x="2" y="6" width="20" height="14" rx="2"/><path d="M8 6V4a2 2 0 014 0v2"/><circle cx="12" cy="13" r="2"/></svg>`, title: 'ESP32 Scan Node', sub: 'RFID + RTC + IMU' },
  { icon: `<svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="rgba(59,130,246,0.8)" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`, title: 'Secure API Gateway', sub: 'HMAC Auth / TLS 1.3' },
  { icon: `<svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="rgba(59,130,246,0.8)" stroke-width="1.5"><polyline points="16,18 22,12 16,6"/><polyline points="8,6 2,12 8,18"/></svg>`, title: 'Django REST Backend', sub: 'Python / DRF' },
  { icon: `<svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="rgba(59,130,246,0.8)" stroke-width="1.5"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>`, title: 'PostgreSQL Ledger', sub: 'Immutable Records' },
  { icon: `<svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="rgba(59,130,246,0.8)" stroke-width="1.5"><path d="M4 12V4l4 4M4 4h4M20 12v8l-4-4M20 20h-4"/><line x1="4" y1="12" x2="20" y2="12"/></svg>`, title: 'Anchor Queue', sub: 'Batch + Retry' },
  { icon: `<svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="rgba(59,130,246,0.9)" stroke-width="1.5"><rect x="4" y="8" width="16" height="8" rx="1"/><line x1="8" y1="8" x2="8" y2="4"/><line x1="12" y1="8" x2="12" y2="4"/><line x1="16" y1="8" x2="16" y2="4"/><line x1="4" y1="16" x2="4" y2="20"/><line x1="20" y1="16" x2="20" y2="20"/></svg>`, title: 'Bitcoin Cash', sub: 'OP_RETURN / Chipnet' },
]
const verifyNodes = [
  { icon: `<svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="rgba(6,182,212,0.8)" stroke-width="1.5"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>`, title: 'Verification Dashboard', sub: 'Vue 3 SPA' },
  { icon: `<svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="rgba(6,182,212,0.8)" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>`, title: 'Blockchain Explorer', sub: 'BCH Explorer API' },
  { icon: `<svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="rgba(6,182,212,0.8)" stroke-width="1.5"><path d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>`, title: 'On-chain Proof', sub: 'OP_RETURN Hash' },
]

// ── Verification console ────────────────────────────────────────────────────
const txid = ref('a3f9c82e1b4d7f0e9c3a5b8d2e6f1a4c7890abcdef1234567890abcdef123456')
const payloadHash = ref('sha256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069')
const network = ref('chipnet')
const verifying = ref(false)
const terminalLines = ref([])

async function runVerification() {
  verifying.value = true
  terminalLines.value = []
  const steps = [
    { text: 'Connecting to BCH Chipnet node...', delay: 200 },
    { text: 'Fetching transaction a3f9c82e...', delay: 700 },
    { text: 'Parsing OP_RETURN output...', delay: 1200 },
    { text: 'Computing SHA-256 of local payload...', delay: 1700 },
    { text: 'Comparing hashes: 7f83b165...9069 ✓', delay: 2200 },
    { text: '<span style="color:#22C55E">✓ VERIFICATION PASSED — Block #849122</span>', delay: 2700 },
  ]
  for (const step of steps) {
    await new Promise(r => setTimeout(r, step.delay - (steps.indexOf(step) > 0 ? steps[steps.indexOf(step)-1].delay : 0)))
    terminalLines.value.push(step.text)
  }
  verifying.value = false
}

// ── Timeline ────────────────────────────────────────────────────────────────
const phases = [
  { title: 'Research & Proposal',          status: 'done',   label: 'Complete'    },
  { title: 'Hardware Prototyping',          status: 'done',   label: 'Complete'    },
  { title: 'PCB Design',                    status: 'done',   label: 'Complete'    },
  { title: 'Backend Development',           status: 'done',   label: 'Complete'    },
  { title: 'Frontend Verification Portal',  status: 'active', label: 'In Progress' },
  { title: 'Blockchain Integration',        status: 'pending',label: 'Pending'     },
  { title: 'Evaluation & Testing',          status: 'pending',label: 'Pending'     },
]

// ── Tech stack ──────────────────────────────────────────────────────────────
const techStack = [
  { name: 'ESP32', sub: 'Microcontroller', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="8" y="8" width="24" height="24" rx="2"/><line x1="4" y1="14" x2="8" y2="14"/><line x1="4" y1="20" x2="8" y2="20"/><line x1="4" y1="26" x2="8" y2="26"/><line x1="32" y1="14" x2="36" y2="14"/><line x1="32" y1="20" x2="36" y2="20"/><line x1="32" y1="26" x2="36" y2="26"/><rect x="14" y="14" width="12" height="12" rx="1" fill="rgba(59,130,246,0.1)" stroke="rgba(59,130,246,0.4)"/></svg>` },
  { name: 'RC522 RFID', sub: '13.56 MHz Reader', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="12" y="14" width="16" height="12" rx="2"/><path d="M8 20 Q8 10 20 10 Q32 10 32 20"/><path d="M5 20 Q5 7 20 7 Q35 7 35 20"/><circle cx="20" cy="20" r="2" fill="currentColor"/></svg>` },
  { name: 'DS3231 RTC', sub: '±2ppm Accuracy', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="20" cy="20" r="14"/><polyline points="20,10 20,20 26,26"/><circle cx="20" cy="20" r="1.5" fill="currentColor"/></svg>` },
  { name: 'MPU6050', sub: '6-DOF IMU', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="10" y="10" width="20" height="20" rx="2"/><line x1="20" y1="10" x2="20" y2="4"/><line x1="20" y1="30" x2="20" y2="36"/><line x1="10" y1="20" x2="4" y2="20"/><line x1="30" y1="20" x2="36" y2="20"/><circle cx="20" cy="20" r="4" fill="rgba(59,130,246,0.1)" stroke="rgba(59,130,246,0.4)"/></svg>` },
  { name: 'Django', sub: 'REST Framework', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><polyline points="8,18 2,12 8,6"/><polyline points="32,18 38,12 32,6"/><line x1="24" y1="4" x2="16" y2="36"/><rect x="10" y="24" width="20" height="12" rx="2"/></svg>` },
  { name: 'PostgreSQL', sub: 'Custody Ledger', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><ellipse cx="20" cy="12" rx="12" ry="4"/><path d="M8 12v8c0 2.2 5.4 4 12 4s12-1.8 12-4v-8"/><path d="M8 20v8c0 2.2 5.4 4 12 4s12-1.8 12-4v-8"/></svg>` },
  { name: 'Vue 3', sub: 'Verify Portal', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><polygon points="20,6 36,34 4,34"/><polygon points="20,14 30,30 10,30" fill="rgba(59,130,246,0.1)" stroke="rgba(59,130,246,0.4)"/></svg>` },
  { name: 'Docker', sub: 'Containerized Deploy', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="4" y="18" width="32" height="12" rx="2"/><rect x="8" y="14" width="7" height="5" rx="1"/><rect x="17" y="14" width="7" height="5" rx="1"/><rect x="26" y="14" width="7" height="5" rx="1"/><rect x="12" y="10" width="7" height="5" rx="1"/><rect x="21" y="10" width="7" height="5" rx="1"/></svg>` },
  { name: 'Bitcoin Cash', sub: 'BCH / Chipnet', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="20" cy="20" r="14"/><path d="M16 14h7c2 0 4 1 4 3s-2 3-4 3h-7M16 20h8c2.5 0 4 1 4 3.5S26.5 27 24 27H16"/><line x1="18" y1="12" x2="18" y2="30"/><line x1="22" y1="12" x2="22" y2="30"/></svg>` },
  { name: 'KiCad', sub: 'PCB Design', icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="6" y="6" width="28" height="28" rx="3"/><line x1="12" y1="6" x2="12" y2="34"/><line x1="20" y1="6" x2="20" y2="34"/><line x1="28" y1="6" x2="28" y2="34"/><line x1="6" y1="12" x2="34" y2="12"/><line x1="6" y1="20" x2="34" y2="20"/><line x1="6" y1="28" x2="34" y2="28"/><circle cx="20" cy="20" r="4" fill="rgba(59,130,246,0.15)" stroke="rgba(59,130,246,0.5)"/></svg>` },
]
</script>

<style scoped>
/* ─── DESIGN TOKENS ──────────────────────────────────────────────────────── */
.landing-page {
  --bg-0: #050816;
  --bg-1: #0B1220;
  --surface: rgba(255,255,255,0.03);
  --surface-2: rgba(255,255,255,0.06);
  --border: rgba(255,255,255,0.07);
  --border-2: rgba(96,165,250,0.18);
  --accent: #3B82F6;
  --accent-2: #06B6D4;
  --text-0: #F8FAFC;
  --text-1: #CBD5E1;
  --text-2: #64748B;
  --text-3: #334155;
  --mono: 'JetBrains Mono', monospace;
  --sans: 'Inter', sans-serif;
  --radius: 20px;
  --radius-sm: 10px;
  --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);

  font-family: var(--sans);
  background: var(--bg-0);
  color: var(--text-0);
  overflow-x: hidden;
}

/* ─── UTILITY ────────────────────────────────────────────────────────────── */
.container { max-width: 1280px; margin: 0 auto; padding: 0 40px; }

.label {
  display: inline-flex; align-items: center; gap: 8px;
  font-family: var(--mono); font-size: 11px; font-weight: 500;
  letter-spacing: 0.12em; text-transform: uppercase; color: var(--accent-2);
  padding: 5px 12px; border: 1px solid rgba(6,182,212,0.25); border-radius: 4px;
  background: rgba(6,182,212,0.06);
}
.label::before { content:''; width:6px; height:6px; border-radius:50%; background:var(--accent-2); box-shadow:0 0 6px var(--accent-2); }

.section-title { font-size: clamp(32px,4vw,52px); font-weight: 800; letter-spacing: -0.03em; line-height: 1.1; color: var(--text-0); }
.section-sub { font-size: 17px; color: var(--text-1); line-height: 1.7; max-width: 560px; }
.section-header { margin-bottom: 64px; }

.gradient-text { background: linear-gradient(135deg, #60A5FA, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }

.btn {
  display: inline-flex; align-items: center; gap: 8px; padding: 13px 26px;
  border-radius: 8px; font-size: 14px; font-weight: 600; letter-spacing: 0.01em;
  cursor: pointer; border: none; transition: var(--transition); text-decoration: none;
}
.btn-primary { background: var(--accent); color: #fff; box-shadow: 0 0 24px rgba(59,130,246,0.25); }
.btn-primary:hover { background: #2563EB; box-shadow: 0 0 36px rgba(59,130,246,0.4); transform: translateY(-1px); }
.btn-ghost { background: transparent; color: var(--text-1); border: 1px solid var(--border); }
.btn-ghost:hover { border-color: var(--border-2); color: var(--text-0); background: var(--surface); }
.btn-outline { display: inline-flex; align-items: center; gap: 8px; padding: 13px 26px; border-radius: 8px; font-size: 14px; font-weight: 600; background: transparent; color: var(--text-1); border: 1px solid var(--border); transition: var(--transition); text-decoration: none; }
.btn-outline:hover { border-color: var(--border-2); color: var(--text-0); }

.blueprint-bg { position: absolute; inset: 0; pointer-events: none; overflow: hidden; }
.blueprint-bg::before { content:''; position:absolute; inset:0; background-image:linear-gradient(rgba(59,130,246,0.035) 1px,transparent 1px),linear-gradient(90deg,rgba(59,130,246,0.035) 1px,transparent 1px); background-size:60px 60px; }
.blueprint-bg::after { content:''; position:absolute; inset:0; background-image:linear-gradient(rgba(59,130,246,0.015) 1px,transparent 1px),linear-gradient(90deg,rgba(59,130,246,0.015) 1px,transparent 1px); background-size:12px 12px; }

.fade-up { opacity: 0; transform: translateY(30px); transition: opacity 0.7s ease, transform 0.7s ease; }
.fade-up.visible { opacity: 1; transform: translateY(0); }

/* ─── NAVIGATION ─────────────────────────────────────────────────────────── */
.landing-nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  padding: 0 40px; height: 64px; display: flex; align-items: center;
  border-bottom: 1px solid transparent; transition: var(--transition);
}
.nav-scrolled { background: rgba(5,8,22,0.88); backdrop-filter: blur(20px); border-bottom-color: var(--border); }
.nav-inner { display: flex; align-items: center; width: 100%; }
.nav-logo { display: flex; align-items: center; gap: 10px; flex-shrink: 0; text-decoration: none; }
.logo-icon { width: 36px; height: 36px; }
.nav-wordmark { font-family: var(--mono); font-size: 15px; font-weight: 600; letter-spacing: 0.15em; color: var(--text-0); }
.nav-links { display: flex; align-items: center; gap: 2px; list-style: none; margin-left: 56px; padding: 0; }
.nav-links a { font-size: 13px; font-weight: 500; color: var(--text-2); padding: 6px 14px; border-radius: 6px; letter-spacing: 0.01em; transition: var(--transition); text-decoration: none; }
.nav-links a:hover { color: var(--text-0); background: var(--surface); }
.nav-cta { margin-left: auto; }
.btn-primary-nav {
  display: inline-flex; align-items: center; gap: 8px; padding: 10px 20px;
  background: var(--accent); color: #fff; border-radius: 8px; font-size: 13px; font-weight: 600;
  text-decoration: none; transition: var(--transition); box-shadow: 0 0 24px rgba(59,130,246,0.25);
}
.btn-primary-nav:hover { background: #2563EB; transform: translateY(-1px); }

/* ─── HERO ───────────────────────────────────────────────────────────────── */
.hero-section { position: relative; min-height: 100vh; display: flex; align-items: center; overflow: hidden; padding-top: 64px; }
.hero-glow-l { position: absolute; width: 600px; height: 600px; border-radius: 50%; background: radial-gradient(circle,rgba(59,130,246,0.08) 0%,transparent 70%); top: -100px; left: -200px; pointer-events: none; }
.hero-glow-r { position: absolute; width: 700px; height: 700px; border-radius: 50%; background: radial-gradient(circle,rgba(6,182,212,0.05) 0%,transparent 70%); bottom: -200px; right: -100px; pointer-events: none; }
.hero-inner { position: relative; z-index: 2; display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; padding: 80px 0; }
.hero-left { max-width: 600px; }
.hero-headline { font-size: clamp(40px,5.5vw,72px); font-weight: 900; letter-spacing: -0.04em; line-height: 1.05; margin: 20px 0 24px; }
.hero-para { font-size: 17px; line-height: 1.75; color: var(--text-1); margin-bottom: 36px; }
.hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }
.hero-right { position: relative; display: flex; align-items: center; justify-content: center; }

/* ESP32 diagram */
.hw-diagram { position: relative; width: 520px; height: 520px; }
.pcb-svg { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 280px; height: 240px; }
.hw-comp {
  position: absolute; padding: 8px 12px; border-radius: 8px;
  background: rgba(11,18,32,0.92); border: 1px solid var(--border-2); backdrop-filter: blur(12px);
  font-family: var(--mono); font-size: 10px; color: var(--text-1); white-space: nowrap;
  box-shadow: 0 4px 20px rgba(0,0,0,0.4); animation: float-comp 4s ease-in-out infinite;
}
.comp-name { font-size: 9px; color: var(--accent-2); letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 2px; }
.comp-val { font-size: 11px; color: var(--text-0); font-weight: 500; }
@keyframes float-comp { 0%,100%{transform:translateY(0px)} 50%{transform:translateY(-6px)} }
.hw-comp-1 { top:20px; left:40px; animation-delay:0s; }
.hw-comp-2 { top:40px; right:20px; animation-delay:0.5s; }
.hw-comp-3 { bottom:80px; left:10px; animation-delay:1s; }
.hw-comp-4 { bottom:40px; right:30px; animation-delay:1.5s; }
.hw-comp-5 { top:130px; left:0px; animation-delay:2s; }
.hw-comp-6 { top:140px; right:0px; animation-delay:2.5s; }
.hw-badge { position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.25); border-radius: 6px; padding: 6px 14px; font-family: var(--mono); font-size: 10px; color: var(--accent); letter-spacing: 0.08em; white-space: nowrap; }

/* ─── METRICS ────────────────────────────────────────────────────────────── */
.metrics-section { padding: 60px 0; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.metrics-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; }
.metric-card { background: var(--bg-0); padding: 36px 32px; transition: var(--transition); position: relative; }
.metric-card::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg,var(--accent),var(--accent-2)); opacity:0; transition:var(--transition); }
.metric-card:hover { background: var(--bg-1); }
.metric-card:hover::before { opacity: 1; }
.metric-icon { width: 40px; height: 40px; margin-bottom: 16px; color: var(--accent); }
.metric-value { font-family: var(--mono); font-size: 28px; font-weight: 700; color: var(--text-0); letter-spacing: -0.02em; margin-bottom: 6px; }
.metric-label { font-size: 13px; color: var(--text-2); font-weight: 500; line-height: 1.4; }

/* ─── ARCHITECTURE ───────────────────────────────────────────────────────── */
.arch-section { padding: 120px 0; position: relative; overflow: hidden; }
.arch-flow {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 8px;
  margin-bottom: 0;
  position: relative;
}
.arch-flow::after {
  content:'';
  position: absolute;
  top: 50%; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, var(--border-2), rgba(6,182,212,0.4));
  z-index: 0;
}
.arch-node {
  padding: 20px 16px; background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius-sm); text-align: center; position: relative; z-index: 1;
  transition: var(--transition); cursor: default;
}
.arch-node:hover { border-color: var(--border-2); background: var(--surface-2); transform: translateY(-3px); box-shadow: 0 12px 40px rgba(59,130,246,0.1); }
.arch-node-icon { font-size: 20px; margin-bottom: 10px; display: flex; justify-content: center; }
.arch-node-title { font-size: 11px; font-weight: 700; color: var(--text-0); letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 4px; }
.arch-node-sub { font-family: var(--mono); font-size: 9px; color: var(--text-2); }

.arch-arrows-row { display: flex; justify-content: space-around; padding: 0; margin-bottom: 40px; }
.arch-arrow-line { width: 80px; height: 1px; background: linear-gradient(90deg, var(--border-2), rgba(6,182,212,0.4)); position: relative; overflow: hidden; }
.arch-pulse { position: absolute; top: -2px; left: 0; width: 6px; height: 6px; border-radius: 50%; background: var(--accent-2); animation: pulse-flow 2s linear infinite; }
@keyframes pulse-flow { 0%{left:0;opacity:1} 100%{left:100%;opacity:0} }

.arch-verify { display: flex; align-items: center; justify-content: center; gap: 40px; margin-top: 20px; }
.arch-node-cyan { border-color: rgba(6,182,212,0.2); background: rgba(6,182,212,0.04); min-width: 160px; }
.arch-verify-label { text-align: center; margin-top: 16px; font-family: var(--mono); font-size: 10px; color: var(--text-2); letter-spacing: 0.08em; }

/* ─── FEATURES ───────────────────────────────────────────────────────────── */
.features-section { padding: 120px 0; background: var(--bg-1); }
.features-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; }
.feature-card { padding: 48px 40px; border-radius: var(--radius); border: 1px solid var(--border); background: var(--bg-0); position: relative; overflow: hidden; transition: var(--transition); }
.feature-card::after { content:''; position:absolute; inset:0; background:radial-gradient(circle at 70% 120%,rgba(59,130,246,0.05) 0%,transparent 60%); pointer-events:none; }
.feature-card:hover { border-color: rgba(59,130,246,0.25); transform: translateY(-4px); box-shadow: 0 20px 60px rgba(0,0,0,0.4); }
.feature-illustration { width:100%; height:160px; margin-bottom:32px; border-radius:10px; overflow:hidden; background:var(--bg-1); border:1px solid var(--border); display:flex; align-items:center; justify-content:center; }
.feature-title { font-size: 22px; font-weight: 700; color: var(--text-0); letter-spacing: -0.01em; margin-bottom: 12px; }
.feature-desc { font-size: 14px; line-height: 1.75; color: var(--text-2); }
.feature-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 24px; }
.feature-tag { font-family: var(--mono); font-size: 10px; color: var(--accent); padding: 4px 10px; border: 1px solid rgba(59,130,246,0.2); border-radius: 4px; background: rgba(59,130,246,0.06); }

/* ─── VERIFICATION ───────────────────────────────────────────────────────── */
.verify-section { padding: 120px 0; position: relative; overflow: hidden; }
.verify-inner { display: grid; grid-template-columns: 1fr 1.1fr; gap: 48px; align-items: start; }
.verify-panel { padding: 40px; border-radius: var(--radius); border: 1px solid var(--border); background: var(--bg-1); }
.verify-panel-title { font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-2); margin-bottom: 28px; display: flex; align-items: center; gap: 10px; }
.verify-panel-title::before { content:''; display:inline-block; width:8px; height:8px; border:1px solid var(--accent); border-radius:2px; transform:rotate(45deg); }
.form-group { margin-bottom: 20px; }
.form-label { display: block; font-family: var(--mono); font-size: 10px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-2); margin-bottom: 8px; }
.form-input { width: 100%; padding: 12px 16px; background: var(--bg-0); border: 1px solid var(--border); border-radius: 8px; color: var(--text-0); font-family: var(--mono); font-size: 12px; outline: none; transition: var(--transition); }
.form-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(59,130,246,0.1); }
.btn-verify { width: 100%; padding: 14px; background: var(--accent); color: #fff; border: none; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; transition: var(--transition); display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 8px; font-family: var(--sans); }
.btn-verify:hover:not(:disabled) { background: #2563EB; box-shadow: 0 0 30px rgba(59,130,246,0.3); }
.btn-verify:disabled { opacity: 0.7; cursor: not-allowed; }
.spin { animation: _spin 0.8s linear infinite; }
@keyframes _spin { 100%{ transform: rotate(360deg); } }
.terminal-output { margin-top: 20px; padding: 16px; background: var(--bg-0); border: 1px solid var(--border); border-radius: 8px; font-family: var(--mono); font-size: 11px; color: var(--text-2); min-height: 80px; }
.terminal-header { color: var(--accent-2); margin-bottom: 8px; }
.terminal-line { margin-bottom: 4px; }
.verify-result { padding: 40px; border-radius: var(--radius); border: 1px solid rgba(34,197,94,0.25); background: rgba(0,20,10,0.6); }
.verify-status { display: flex; align-items: center; gap: 12px; margin-bottom: 28px; }
.status-badge { display: flex; align-items: center; gap: 8px; padding: 8px 16px; background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.3); border-radius: 6px; font-family: var(--mono); font-size: 13px; font-weight: 600; color: #22C55E; }
.status-dot { width: 8px; height: 8px; border-radius: 50%; background: #22C55E; box-shadow: 0 0 10px #22C55E; animation: status-pulse 1.5s ease-in-out infinite; }
@keyframes status-pulse { 0%,100%{box-shadow:0 0 8px #22C55E} 50%{box-shadow:0 0 16px #22C55E} }
.status-confirm { font-family: var(--mono); font-size: 10px; color: var(--text-2); }
.verify-field { border-bottom: 1px solid var(--border); padding: 14px 0; display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; }
.verify-field:last-of-type { border-bottom: none; }
.vf-key { font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-2); flex-shrink: 0; }
.vf-val { font-family: var(--mono); font-size: 12px; color: var(--text-0); text-align: right; word-break: break-all; }
.vf-val.accent { color: var(--accent-2); }
.vf-val.green { color: #22C55E; }
.verify-note { margin-top: 20px; padding: 12px; background: rgba(34,197,94,0.05); border: 1px solid rgba(34,197,94,0.15); border-radius: 8px; font-family: var(--mono); font-size: 10px; color: rgba(34,197,94,0.7); line-height: 1.6; }

/* ─── TIMELINE ───────────────────────────────────────────────────────────── */
.timeline-section { padding: 120px 0; background: var(--bg-1); }
.timeline-inner { display: grid; grid-template-columns: 360px 1fr; gap: 80px; align-items: start; }
.timeline-left { }
.progress-card { margin-top: 40px; padding: 24px; border: 1px solid var(--border); border-radius: var(--radius-sm); background: var(--surface); }
.progress-header { display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 12px; color: var(--text-1); }
.progress-pct { font-family: var(--mono); color: var(--accent); }
.progress-bar-bg { height: 4px; background: var(--border); border-radius: 2px; overflow: hidden; }
.progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent-2)); border-radius: 2px; transition: width 1s ease; }
.timeline-track { position: relative; padding-left: 32px; }
.timeline-track::before { content:''; position:absolute; left:8px; top:8px; bottom:8px; width:1px; background:linear-gradient(180deg,var(--accent),transparent); }
.timeline-item { position: relative; margin-bottom: 32px; }
.timeline-item:last-child { margin-bottom: 0; }
.tl-dot { position: absolute; left: -32px; top: 3px; width: 18px; height: 18px; border-radius: 50%; border: 2px solid var(--border); background: var(--bg-1); display: flex; align-items: center; justify-content: center; transition: var(--transition); }
.tl-dot.done { border-color: var(--accent); background: rgba(59,130,246,0.15); }
.tl-dot.done::after { content:''; width:6px; height:6px; border-radius:50%; background:var(--accent); }
.tl-dot.active { border-color: var(--accent-2); background: rgba(6,182,212,0.15); animation: tl-pulse 2s infinite; }
.tl-dot.active::after { content:''; width:6px; height:6px; border-radius:50%; background:var(--accent-2); }
@keyframes tl-pulse { 0%,100%{box-shadow:0 0 0 0 rgba(6,182,212,0.3)} 50%{box-shadow:0 0 0 6px rgba(6,182,212,0)} }
.tl-phase { font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-2); margin-bottom: 4px; }
.tl-title { font-size: 16px; font-weight: 600; color: var(--text-0); }
.tl-status { display: inline-block; margin-top: 4px; font-family: var(--mono); font-size: 10px; padding: 2px 8px; border-radius: 3px; }
.tl-status.done { background: rgba(34,197,94,0.1); color: #22C55E; border: 1px solid rgba(34,197,94,0.2); }
.tl-status.active { background: rgba(6,182,212,0.1); color: var(--accent-2); border: 1px solid rgba(6,182,212,0.2); }
.tl-status.pending { background: var(--surface); color: var(--text-2); border: 1px solid var(--border); }

/* ─── TECH STACK ─────────────────────────────────────────────────────────── */
.tech-section { padding: 120px 0; }
.tech-grid { display: grid; grid-template-columns: repeat(5,1fr); gap: 16px; margin-top: 56px; }
.tech-card { padding: 28px 20px; border-radius: var(--radius-sm); border: 1px solid var(--border); background: var(--surface); text-align: center; transition: var(--transition); cursor: default; }
.tech-card:hover { border-color: var(--border-2); background: var(--surface-2); transform: translateY(-3px); box-shadow: 0 12px 40px rgba(0,0,0,0.3); }
.tech-icon { width: 40px; height: 40px; margin: 0 auto 12px; display: flex; align-items: center; justify-content: center; color: var(--text-2); }
.tech-name { font-size: 13px; font-weight: 600; color: var(--text-1); margin-bottom: 4px; }
.tech-sub { font-family: var(--mono); font-size: 10px; color: var(--text-3); }

/* ─── CTA ────────────────────────────────────────────────────────────────── */
.cta-section { padding: 140px 0; position: relative; overflow: hidden; }
.cta-glow { position: absolute; width: 800px; height: 400px; border-radius: 50%; background: radial-gradient(circle,rgba(59,130,246,0.06) 0%,transparent 70%); top: 50%; left: 50%; transform: translate(-50%,-50%); pointer-events: none; }
.cta-headline { font-size: clamp(40px,5vw,64px); font-weight: 900; letter-spacing: -0.04em; line-height: 1.1; margin: 20px 0 20px; }
.cta-sub { font-size: 17px; color: var(--text-1); max-width: 500px; margin: 0 auto 40px; line-height: 1.7; }
.cta-btns { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }

/* ─── FOOTER ─────────────────────────────────────────────────────────────── */
.landing-footer { border-top: 1px solid var(--border); padding: 48px 40px; }
.footer-inner { display: flex; align-items: center; justify-content: space-between; gap: 40px; flex-wrap: wrap; }
.footer-logo-row { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
.footer-wordmark { font-family: var(--mono); font-size: 13px; font-weight: 600; letter-spacing: 0.12em; }
.footer-inst { font-size: 13px; color: var(--text-2); line-height: 1.5; }
.footer-links { display: flex; align-items: center; gap: 32px; list-style: none; padding: 0; }
.footer-links a { font-size: 13px; color: var(--text-2); transition: var(--transition); text-decoration: none; }
.footer-links a:hover { color: var(--text-0); }
.footer-copy { font-family: var(--mono); font-size: 11px; color: var(--text-3); line-height: 1.6; }
</style>
