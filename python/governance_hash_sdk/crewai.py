"""CrewAI integration for multi-agent hash chain tracking."""

from .core import Signature, SignaturePolicy, sign


class ScalarCrewTracker:
    """Maintains a continuous hash chain across CrewAI agent steps."""

    def __init__(self, crew_id: str, private_key: str = None):
        self.crew_id = crew_id
        self.private_key = private_key
        self.policy = SignaturePolicy(required_fields=["action", "crew_id"])
        self.current_hash = "genesis"

    def sign_step(self, step_output) -> Signature:
        sig = sign(
            data={
                "action": "crew_agent_step",
                "crew_id": self.crew_id,
                "output": str(step_output),
            },
            policy=self.policy,
            private_key=self.private_key,
            previous_hash=self.current_hash,
        )
        self.current_hash = sig.hash
        return sig

    def get_root_hash(self) -> str:
        return self.current_hash
