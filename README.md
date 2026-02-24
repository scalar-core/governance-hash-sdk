# `governance-hash-sdk`

[![ISO/IEC 42001 - Ready](badges/iso-42001-ready.png)](https://scalar-os.com)
[![Secured By - SCALAR Core](badges/secured-by-scalar-core.png)](https://github.com/scalar-os/governance-hash-sdk)
[![EBITDA Assurance - Eligible](badges/ebitda-assurance-eligible.png)](https://scalar-os.com/index)

> **Hosted badge images:** [ISO 42001](https://scalar-os.lovable.app/badges/iso-42001-ready.png) · [SCALAR Core](https://scalar-os.lovable.app/badges/secured-by-scalar-core.png) · [EBITDA Assurance](https://scalar-os.lovable.app/badges/ebitda-assurance-eligible.png)

---

**A lightweight, zero-dependency SDK for cryptographically signing AI agent workflows.**

`governance-hash-sdk` provides drop-in integrations for LangChain, LangGraph, and CrewAI to seal every agentic action with a **Governance Hash**. By generating an immutable SHA-256 audit trail, this SDK transforms opaque LLM executions into tamper-evident, enterprise-ready logs.

---

## ⚡ Why Use This SDK?

- **Cryptographic Accountability:** Seals each agent action with a Governance Hash (SHA-256).
- **ISO/IEC 42001 Readiness:** Satisfies clauses for AI Traceability and Risk Management.
- **Zero Data Retention:** Hashes generated *locally*. Raw prompts and PII never leave your servers.
- **Policy-as-Code Enforcement:** Validates agent decisions against predefined risk boundaries.

---

## 📦 Installation

**Python (LangChain, CrewAI)**

```bash
pip install governance-hash-sdk
```

**TypeScript (LangChain.js)**

```bash
npm install @scalar-os/governance-hash-sdk
```

---

## 🚀 Quick Start (LangChain)

```python
from governance_hash_sdk.langchain import ScalarCallbackHandler

handler = ScalarCallbackHandler(agent_id="my_agent", policy_ref="ops-policy")
response = agent.run("Process refund $50", callbacks=[handler])
print(f"Hash: {handler.latest_hash}")
```

See full docs at https://github.com/scalar-os/governance-hash-sdk

## 📄 License

Apache License 2.0 — Copyright 2025 SCALAR OS Inc.
