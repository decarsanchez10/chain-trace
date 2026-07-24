import hashlib
import json

def calculate_payload_hash(data_dict: dict) -> str:
    """Calculates SHA-256 hash of a deterministic JSON string."""
    encoded = json.dumps(data_dict, sort_keys=True).encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()
