"""Core cryptographic signing logic for governance-hash-sdk."""

import hashlib
import hmac
import json
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class SignaturePolicy:
    """Defines the required fields and entropy threshold for a valid signature."""

    def __init__(self, min_entropy: float = 0.95, required_fields: Optional[List[str]] = None):
        self.min_entropy = min_entropy
        self.required_fields = required_fields or ["action", "timestamp"]


class Signature:
    """Immutable record of a signed decision."""

    def __init__(self, hash_value: str, payload: Dict[str, Any], timestamp: str, nonce: str):
        self.hash = hash_value
        self.payload = payload
        self.timestamp = timestamp
        self.nonce = nonce

    def to_dict(self) -> Dict[str, Any]:
        return {
            "hash": self.hash,
            "payload": self.payload,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
        }


def sign(
    data: Dict[str, Any],
    policy: SignaturePolicy,
    private_key: Optional[str] = None,
    previous_hash: str = "genesis",
) -> Signature:
    """
    Generate a SHA-256 cryptographic hash of a decision payload.

    Args:
        data: The decision payload to sign.
        policy: A SignaturePolicy defining required fields.
        private_key: Optional HMAC key. Uses plain SHA-256 if omitted.
        previous_hash: The hash of the previous entry in the chain.

    Returns:
        A Signature object containing the hash, payload, timestamp, and nonce.

    Raises:
        ValueError: If a required field from the policy is missing.
    """
    for field in policy.required_fields:
        if field not in data:
            raise ValueError(f"Policy Violation: Missing required field '{field}'")

    timestamp = datetime.now(timezone.utc).isoformat()
    nonce = str(uuid.uuid4())

    payload = {
        **data,
        "_meta": {
            "timestamp": timestamp,
            "nonce": nonce,
            "previous_hash": previous_hash,
        },
    }

    encoded = json.dumps(payload, sort_keys=True).encode("utf-8")

    if private_key:
        hash_value = hmac.new(private_key.encode("utf-8"), encoded, hashlib.sha256).hexdigest()
    else:
        hash_value = hashlib.sha256(encoded).hexdigest()

    return Signature(
        hash_value=f"0x{hash_value}",
        payload=payload,
        timestamp=timestamp,
        nonce=nonce,
    )
