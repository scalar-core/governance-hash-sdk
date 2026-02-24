"""LangChain callback handler for automatic governance hashing."""

import json
from typing import Any, Dict

from langchain_core.callbacks import BaseCallbackHandler

from .core import Signature, SignaturePolicy, sign


class ScalarCallbackHandler(BaseCallbackHandler):
    """Signs LangChain tool invocations and chain completions automatically."""

    def __init__(self, agent_id: str, policy_ref: str, private_key: str = None):
        self.agent_id = agent_id
        self.policy_ref = policy_ref
        self.private_key = private_key
        self.policy = SignaturePolicy(required_fields=["action", "agent_id"])
        self.latest_hash: str | None = None
        self.hash_chain: list[Signature] = []

    def on_tool_end(self, output: str, **kwargs) -> None:
        previous = self.latest_hash or "genesis"
        sig = sign(
            data={"action": "tool_execution", "agent_id": self.agent_id, "output": output},
            policy=self.policy,
            private_key=self.private_key,
            previous_hash=previous,
        )
        self.latest_hash = sig.hash
        self.hash_chain.append(sig)

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs) -> None:
        previous = self.latest_hash or "genesis"
        sig = sign(
            data={
                "action": "chain_completion",
                "agent_id": self.agent_id,
                "output": json.dumps(outputs, default=str),
            },
            policy=self.policy,
            private_key=self.private_key,
            previous_hash=previous,
        )
        self.latest_hash = sig.hash
        self.hash_chain.append(sig)
