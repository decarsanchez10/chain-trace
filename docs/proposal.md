# ChainTrace

**A Bitcoin Cash-Anchored Chain-of-Custody System with Custom IoT-Based Scan-Logging Hardware**

Eastern Samar State University — College of Engineering
Capstone Project

---

## Overview

ChainTrace is a chain-of-custody tracking system that combines a custom-built ESP32-based hardware scan node with a Django/Vue web application. Every custody handoff — a scan of an asset's RFID tag — is captured on the hardware node, hashed, stored off-chain, and anchored to the Bitcoin Cash blockchain via an `OP_RETURN` transaction. This produces a custody trail that can be independently verified by any party without needing to trust the system operator.

The problem this solves: conventional custody logs (spreadsheets, internal databases) can be edited, backdated, or selectively altered without leaving a trace. ChainTrace makes tampering **detectable** by anchoring a cryptographic fingerprint of every custody event to a public, immutable blockchain.

## How it works

1. A handler scans an asset's RFID tag using the custom ESP32 scan node.
2. The node reads the tag UID, timestamps it (DS3231 RTC, works offline), checks for tamper/motion signals (reed switch + MPU6050), and computes a SHA-256 hash of the event.
3. The event is sent to the Django backend, where the full record is stored in PostgreSQL and the hash is queued for anchoring.
4. The hash is written to the Bitcoin Cash chipnet blockchain as an `OP_RETURN` transaction.
5. Anyone can later use the Vue verification dashboard to recompute the hash of a stored record and compare it against what's on-chain — a match confirms the record hasn't been altered since it was anchored.

## Repository structure

```
chaintrace/
├── backend/       # Django + DRF API, custody + anchoring + verification apps
├── frontend/       # Vue 3 dashboards and verification interface
├── firmware/       # ESP32 firmware (RFID, RTC, motion, tamper, hashing, upload)
├── hardware/        # KiCad schematic and PCB design files
├── docs/         # Proposal, architecture notes, diagrams
└── docker-compose.yml
```

See each subfolder's own README (once added) for setup specific to that layer.

## Tech stack

| Layer | Tools |
|---|---|
| Hardware | ESP32-WROOM-32E (custom PCB), RC522 RFID, DS3231 RTC, MPU6050, tamper switch |
| Firmware | ESP-IDF / Arduino (C/C++) |
| Backend | Django, Django REST Framework, PostgreSQL |
| Blockchain | Bitcoin Cash (chipnet testnet), OP_RETURN anchoring, mainnet-js |
| Frontend | Vue 3, Pinia, WalletConnect (wc2-bch-bcr) |
| Infra | Docker, Docker Compose |
| PCB design | KiCad, fabrication via JLCPCB/PCBWay |

## Project status

- [ ] Backend API (custody events, anchoring, verification)
- [ ] Frontend dashboards
- [ ] Breadboard hardware prototype
- [ ] Custom PCB design (Rev 1)
- [ ] PCB fabrication and bring-up
- [ ] Full system integration
- [ ] Evaluation (scan-to-anchor latency, hash accuracy, hardware reliability)

## Getting started

```bash
git clone <repo-url>
cd chaintrace
docker-compose up --build
```

Backend API: `http://localhost:8000`
Frontend: `http://localhost:5173`

Firmware setup and PCB fabrication instructions live in `/firmware` and `/hardware` respectively once those folders are populated.

