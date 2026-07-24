<template>
  <div class="landing-page">
    <!-- 1. HEADER / NAVIGATION -->
    <header class="landing-header">
      <div class="brand">
        <div class="logo-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
            <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
            <line x1="12" y1="22.08" x2="12" y2="12"></line>
          </svg>
        </div>
        <div class="brand-text">
          <span class="brand-name">CHAINTRACE</span>
          <span class="brand-tagline">TRACE. VERIFY. TRUST.</span>
        </div>
      </div>
      <nav class="landing-nav">
        <a href="#home" class="active">HOME</a>
        <a href="#overview">OVERVIEW</a>
        <a href="#architecture">ARCHITECTURE</a>
        <a href="#features">FEATURES</a>
        <a href="#tech">TECH STACK</a>
        <a href="#project">PROJECT</a>
        <a href="#contact">CONTACT</a>
      </nav>
    </header>

    <!-- 2. HERO SECTION -->
    <section id="home" class="hero-section">
      <div class="hero-content">
        <h1 class="hero-title">
          EVERY HANDOFF.<br>
          CRYPTOGRAPHICALLY<br>
          <span class="highlight">TRACEABLE.</span>
        </h1>
        <p class="hero-subtitle">
          ChainTrace is a Bitcoin Cash–anchored chain-of-custody system with custom IoT-based scan-logging hardware.
        </p>
        <p class="hero-desc">
          Every scan is hashed, stored, and anchored on the Bitcoin Cash blockchain—making tampering detectable and trust verifiable by anyone.
        </p>
        <div class="hero-actions">
          <button class="btn btn-primary" @click="goTo('/dashboard')">EXPLORE THE SYSTEM</button>
          <button class="btn btn-secondary" @click="goTo('/verify')">VERIFY A RECORD</button>
        </div>
        
        <div class="university-info">
          <p>EASTERN SAMAR STATE UNIVERSITY</p>
          <p class="college">COLLEGE OF ENGINEERING</p>
        </div>
      </div>
      <div class="hero-visual">
        <img src="/img/scan_node_hero.png" alt="Scan Node and Blockchain" class="hero-image" />
      </div>
    </section>

    <!-- 3. HOW IT WORKS SECTION -->
    <section id="overview" class="how-it-works">
      <h2 class="section-title">HOW IT WORKS</h2>
      <div class="process-steps">
        <div class="step">
          <div class="step-icon">1</div>
          <h3>RFID SCAN</h3>
          <p>Handler scans the asset tag using the ESP32 scan node.</p>
        </div>
        <div class="step-arrow">→</div>
        <div class="step">
          <div class="step-icon">2</div>
          <h3>HASH & LOG</h3>
          <p>UID, timestamp, and sensor data are hashed using SHA-256 and stored off-chain.</p>
        </div>
        <div class="step-arrow">→</div>
        <div class="step">
          <div class="step-icon">3</div>
          <h3>BACKEND API</h3>
          <p>The event is sent to the Django backend and stored in PostgreSQL.</p>
        </div>
        <div class="step-arrow">→</div>
        <div class="step">
          <div class="step-icon">4</div>
          <h3>ANCHOR</h3>
          <p>The hash is anchored to Bitcoin Cash via an OP_RETURN transaction.</p>
        </div>
        <div class="step-arrow">→</div>
        <div class="step">
          <div class="step-icon">5</div>
          <h3>VERIFY ANYTIME</h3>
          <p>Anyone can verify the record by comparing the stored hash with the on-chain data.</p>
        </div>
      </div>
    </section>

    <!-- 4. CORE FEATURES SECTION -->
    <section id="features" class="features-section">
      <h2 class="section-title">CORE FEATURES</h2>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">📡</div>
          <h3>HARDWARE-BASED SCAN LOGGING</h3>
          <p>Custom ESP32 node captures every custody handoff.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">⏱️</div>
          <h3>OFFLINE-READY TIMESTAMPING</h3>
          <p>DS3231 RTC ensures accurate timestamps even when offline.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🚨</div>
          <h3>TAMPER DETECTION</h3>
          <p>Reed switch and motion sensors detect tampering or shocks.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🔐</div>
          <h3>CRYPTOGRAPHIC INTEGRITY</h3>
          <p>Every event is hashed using SHA-256.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🔗</div>
          <h3>BITCOIN CASH ANCHORING</h3>
          <p>Hashes are anchored on-chain via OP_RETURN outputs.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">✅</div>
          <h3>INDEPENDENT VERIFICATION</h3>
          <p>Anyone can verify records without trusting the system operator.</p>
        </div>
      </div>
    </section>

    <!-- 5. SYSTEM ARCHITECTURE SECTION -->
    <section id="architecture" class="architecture-section">
      <h2 class="section-title">SYSTEM ARCHITECTURE</h2>
      <div class="architecture-diagram">
        <div class="arch-node">ESP32 SCAN NODE</div>
        <div class="arch-arrow">↓</div>
        <div class="arch-node">DJANGO REST API</div>
        <div class="arch-arrow">↓</div>
        <div class="arch-node">POSTGRESQL DATABASE</div>
        <div class="arch-arrow">↓</div>
        <div class="arch-node">ANCHOR QUEUE</div>
        <div class="arch-arrow">↓</div>
        <div class="arch-node highlight-node">BITCOIN CASH CHIPNET</div>
        <div class="arch-connector"></div>
        <div class="arch-node verification-node">VERIFICATION DASHBOARD</div>
      </div>
    </section>

    <!-- 6. PROJECT STATUS SECTION -->
    <section id="project" class="project-status">
      <h2 class="section-title">PROJECT STATUS</h2>
      <div class="timeline-container">
        <div class="timeline-item active-status">
          <span class="status-dot"></span>
          <span class="status-label">Backend API</span>
          <span class="status-badge in-progress">IN PROGRESS</span>
        </div>
        <div class="timeline-item active-status">
          <span class="status-dot"></span>
          <span class="status-label">Frontend</span>
          <span class="status-badge in-progress">IN PROGRESS</span>
        </div>
        <div class="timeline-item active-status">
          <span class="status-dot"></span>
          <span class="status-label">Hardware Prototype</span>
          <span class="status-badge in-progress">IN PROGRESS</span>
        </div>
        <div class="timeline-item pending-status">
          <span class="status-dot"></span>
          <span class="status-label">PCB Design Rev 1</span>
          <span class="status-badge pending">PENDING</span>
        </div>
        <div class="timeline-item pending-status">
          <span class="status-dot"></span>
          <span class="status-label">PCB Fab & Bring-up</span>
          <span class="status-badge pending">PENDING</span>
        </div>
        <div class="timeline-item pending-status">
          <span class="status-dot"></span>
          <span class="status-label">System Integration</span>
          <span class="status-badge pending">PENDING</span>
        </div>
        <div class="timeline-item pending-status">
          <span class="status-dot"></span>
          <span class="status-label">Evaluation & Testing</span>
          <span class="status-badge pending">PENDING</span>
        </div>
      </div>
    </section>

    <!-- 7. TECH STACK SECTION -->
    <section id="tech" class="tech-stack">
      <h2 class="section-title">TECH STACK</h2>
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

    <!-- 8. FINAL CTA SECTION -->
    <section id="contact" class="cta-section">
      <div class="cta-visual">
        <img src="/img/cyber_shield.png" alt="Cyber Shield" class="cta-image" />
      </div>
      <div class="cta-content">
        <h2 class="cta-title">TRUST THE RECORD.<br>VERIFY THE PROOF.</h2>
        <p class="cta-desc">ChainTrace makes every custody handoff transparent, tamper-evident, and verifiable—forever.</p>
        <div class="hero-actions">
          <button class="btn btn-primary" @click="goTo('/dashboard')">EXPLORE THE SYSTEM</button>
          <button class="btn btn-secondary" @click="goTo('/verify')">VERIFY A RECORD</button>
        </div>
      </div>
    </section>

    <!-- 9. FOOTER -->
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

const router = useRouter()

const goTo = (path) => {
  router.push(path)
}
</script>

<style scoped>
/* Base Theme & Utilities */
.landing-page {
  background-color: #050a1a;
  color: #e0e6ed;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  overflow-x: hidden;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  letter-spacing: 2px;
  margin-bottom: 3rem;
  color: #ffffff;
  text-transform: uppercase;
}

.highlight {
  color: #00d2d3;
  text-shadow: 0 0 15px rgba(0, 210, 211, 0.6);
}

.btn {
  padding: 1rem 2rem;
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.btn-primary {
  background: #00d2d3;
  color: #050a1a;
  box-shadow: 0 0 20px rgba(0, 210, 211, 0.4);
}
.btn-primary:hover {
  background: #00f0f0;
  box-shadow: 0 0 30px rgba(0, 210, 211, 0.7);
}

.btn-secondary {
  background: transparent;
  color: #00d2d3;
  border: 1px solid #00d2d3;
}
.btn-secondary:hover {
  background: rgba(0, 210, 211, 0.1);
  box-shadow: inset 0 0 10px rgba(0, 210, 211, 0.2);
}

/* 1. Header */
.landing-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 4rem;
  background: rgba(5, 10, 26, 0.7);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0, 210, 211, 0.2);
  z-index: 100;
}

.brand {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo-icon {
  width: 40px;
  height: 40px;
  color: #00d2d3;
  filter: drop-shadow(0 0 5px rgba(0, 210, 211, 0.5));
}

.brand-text {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: 2px;
  color: #fff;
}

.brand-tagline {
  font-size: 0.7rem;
  letter-spacing: 1px;
  color: #00d2d3;
}

.landing-nav {
  display: flex;
  gap: 2rem;
}

.landing-nav a {
  color: #a0a0b0;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.landing-nav a:hover,
.landing-nav a.active {
  color: #00d2d3;
  text-shadow: 0 0 10px rgba(0, 210, 211, 0.5);
}

/* 2. Hero Section */
.hero-section {
  min-height: 100vh;
  padding: 8rem 4rem 4rem;
  display: flex;
  align-items: center;
  position: relative;
  background-image: 
    linear-gradient(to bottom, rgba(5, 10, 26, 0.9), rgba(5, 10, 26, 1)),
    radial-gradient(circle at 70% 50%, rgba(0, 210, 211, 0.15) 0%, transparent 50%);
}

.hero-content {
  flex: 1;
  z-index: 2;
}

.hero-title {
  font-size: 4.5rem;
  line-height: 1.1;
  font-weight: 800;
  margin-bottom: 1.5rem;
  color: #fff;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: #e0e6ed;
  margin-bottom: 1rem;
  max-width: 600px;
  line-height: 1.6;
}

.hero-desc {
  font-size: 1.1rem;
  color: #a0a0b0;
  margin-bottom: 3rem;
  max-width: 600px;
  line-height: 1.6;
}

.hero-actions {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 4rem;
}

.university-info {
  font-size: 0.85rem;
  letter-spacing: 2px;
  color: #5a6b8c;
}

.university-info .college {
  color: #00d2d3;
  margin-top: 0.25rem;
}

.hero-visual {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.hero-image {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 0 50px rgba(0, 210, 211, 0.2);
  border: 1px solid rgba(0, 210, 211, 0.1);
  mask-image: linear-gradient(to bottom, black 80%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 80%, transparent 100%);
}

/* 3. How It Works */
.how-it-works {
  padding: 6rem 4rem;
  background-color: #070e20;
  border-top: 1px solid rgba(0, 210, 211, 0.1);
  border-bottom: 1px solid rgba(0, 210, 211, 0.1);
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
  background: rgba(0, 210, 211, 0.1);
  border: 2px solid #00d2d3;
  color: #00d2d3;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5rem;
  font-weight: 800;
  box-shadow: 0 0 15px rgba(0, 210, 211, 0.3);
}

.step h3 {
  font-size: 1.1rem;
  color: #fff;
  margin-bottom: 0.75rem;
}

.step p {
  font-size: 0.9rem;
  color: #a0a0b0;
  line-height: 1.5;
}

.step-arrow {
  color: #00d2d3;
  font-size: 2rem;
  margin-top: 1.5rem;
  opacity: 0.5;
}

/* 4. Features */
.features-section {
  padding: 8rem 4rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background: rgba(10, 15, 35, 0.5);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0, 210, 211, 0.2);
  padding: 2.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  border-color: #00d2d3;
  box-shadow: 0 10px 30px rgba(0, 210, 211, 0.15);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
}

.feature-card h3 {
  font-size: 1.2rem;
  color: #fff;
  margin-bottom: 1rem;
}

.feature-card p {
  color: #a0a0b0;
  line-height: 1.6;
}

/* 5. Architecture */
.architecture-section {
  padding: 6rem 4rem;
  background: #070e20;
}

.architecture-diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
  margin: 0 auto;
}

.arch-node {
  background: rgba(10, 15, 35, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1rem 2rem;
  border-radius: 4px;
  font-weight: 600;
  letter-spacing: 1px;
  min-width: 250px;
  text-align: center;
  z-index: 2;
}

.arch-arrow {
  color: #00d2d3;
  font-size: 1.5rem;
  margin: 0.5rem 0;
}

.highlight-node {
  border-color: #00d2d3;
  color: #00d2d3;
  box-shadow: 0 0 15px rgba(0, 210, 211, 0.2);
}

.arch-connector {
  height: 40px;
  width: 2px;
  background: linear-gradient(to bottom, rgba(0, 210, 211, 0.5), transparent);
  margin: 1rem 0;
}

.verification-node {
  background: rgba(0, 210, 211, 0.1);
  border-color: #00d2d3;
  border-style: dashed;
}

/* 6. Project Status */
.project-status {
  padding: 8rem 4rem;
}

.timeline-container {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.timeline-item {
  display: flex;
  align-items: center;
  background: rgba(10, 15, 35, 0.5);
  padding: 1rem 2rem;
  border-radius: 4px;
  border-left: 2px solid;
}

.active-status {
  border-left-color: #00d2d3;
}
.pending-status {
  border-left-color: #334155;
  opacity: 0.6;
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 1.5rem;
}
.active-status .status-dot {
  background: #00d2d3;
  box-shadow: 0 0 10px #00d2d3;
}
.pending-status .status-dot {
  background: #334155;
}

.status-label {
  flex: 1;
  font-size: 1.1rem;
  font-weight: 500;
}

.status-badge {
  font-size: 0.75rem;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-weight: 600;
  letter-spacing: 1px;
}
.in-progress {
  background: rgba(0, 210, 211, 0.1);
  color: #00d2d3;
  border: 1px solid rgba(0, 210, 211, 0.3);
}
.pending {
  background: rgba(51, 65, 85, 0.2);
  color: #94a3b8;
  border: 1px solid rgba(51, 65, 85, 0.5);
}

/* 7. Tech Stack */
.tech-stack {
  padding: 6rem 4rem;
  background: #070e20;
}

.tech-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  max-width: 900px;
  margin: 0 auto;
}

.tech-item {
  background: rgba(10, 15, 35, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1rem 2rem;
  border-radius: 4px;
  font-weight: 600;
  color: #a0a0b0;
  transition: all 0.3s ease;
}

.tech-item:hover {
  color: #fff;
  border-color: rgba(255, 255, 255, 0.3);
}

.highlight-tech {
  color: #00d2d3;
  border-color: rgba(0, 210, 211, 0.3);
}
.highlight-tech:hover {
  color: #00d2d3;
  border-color: #00d2d3;
  box-shadow: 0 0 15px rgba(0, 210, 211, 0.2);
}

/* 8. CTA Section */
.cta-section {
  padding: 8rem 4rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4rem;
  position: relative;
}

.cta-visual {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

.cta-image {
  max-width: 500px;
  border-radius: 12px;
  box-shadow: 0 0 60px rgba(0, 210, 211, 0.3);
  border: 1px solid rgba(0, 210, 211, 0.2);
}

.cta-content {
  flex: 1;
}

.cta-title {
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  color: #fff;
}

.cta-desc {
  font-size: 1.2rem;
  color: #a0a0b0;
  margin-bottom: 3rem;
  max-width: 500px;
  line-height: 1.6;
}

/* 9. Footer */
.landing-footer {
  background: #030612;
  padding: 3rem 4rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  text-align: center;
}

.footer-logo {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: 2px;
  color: #fff;
  margin-bottom: 1rem;
}

.footer-copy {
  color: #5a6b8c;
  font-size: 0.85rem;
}

/* Responsive */
@media (max-width: 1024px) {
  .hero-section {
    flex-direction: column;
    text-align: center;
    padding-top: 10rem;
  }
  .hero-desc {
    margin: 0 auto 3rem;
  }
  .hero-actions {
    justify-content: center;
  }
  .process-steps {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
  .step-arrow {
    transform: rotate(90deg);
    margin: 0;
  }
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .cta-section {
    flex-direction: column;
    text-align: center;
  }
  .cta-visual {
    justify-content: center;
  }
  .cta-desc {
    margin: 0 auto 3rem;
  }
}

@media (max-width: 768px) {
  .landing-nav {
    display: none;
  }
  .features-grid {
    grid-template-columns: 1fr;
  }
  .hero-title {
    font-size: 3rem;
  }
  .cta-title {
    font-size: 2.5rem;
  }
  .cta-image {
    max-width: 100%;
  }
}
</style>
