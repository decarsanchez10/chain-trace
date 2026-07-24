# API Reference

## Endpoints

### 1. Custody Scan Event
- `POST /api/custody/scan/`
- Request body: `{ asset_id, handler_id, timestamp, hash, signature }`

### 2. List Custody Events
- `GET /api/custody/events/`

### 3. Verify Event
- `GET /api/verification/verify/:event_id/`
