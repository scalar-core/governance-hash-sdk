# SCALAR Core: Governance Hash SDK

[![ISO/IEC 42001 - Ready](https://img.shields.io/badge/ISO%2FIEC_42001-Ready-10b981?style=for-the-badge&logo=shield&logoColor=white)](https://scalar-os.com)
[![Secured By - SCALAR Core](https://img.shields.io/badge/Secured_By-SCALAR_Core-0f172a?style=for-the-badge&logo=lock&logoColor=white)](https://github.com/scalar-core/governance-hash-sdk)
[![EBITDA Assurance - Eligible](https://img.shields.io/badge/EBITDA_Assurance-Eligible-f59e0b?style=for-the-badge&logo=check&logoColor=white)](https://scalar-os.com)

**A lightweight, zero-dependency SDK for cryptographically signing AI agent workflows.**

`governance-hash-sdk` provides drop-in integrations to seal every agentic action with a **Governance Hash**. By generating an immutable SHA-256 audit trail, this SDK transforms opaque LLM executions into tamper-evident, enterprise-ready logs.

---

## ⚡ Why Use This SDK?

* **Cryptographic Accountability:** Seals each agent action with a unique Governance Hash (SHA-256) linked to the previous action, creating an unbreakable chain.
* **ISO/IEC 42001 Readiness:** Automatically satisfies strict enterprise clauses for AI Traceability and Risk Management.
* **Zero Data Retention:** Hashes are generated **locally**. Raw prompts, proprietary data, and PII never leave your servers.
* **Policy-as-Code Enforcement:** Validates agent decisions against predefined operational and financial risk boundaries before execution.

---



## 🌍 Ecosystem & Roadmap

We are building the universal standard for AI operational integrity. Our architecture is designed to support any autonomous system, from open-source orchestrators to proprietary enterprise platforms.

**Currently Supported (v0.1.x):**
* LangChain & LangChain.js
* LangGraph
* CrewAI

**Upcoming Integrations (Roadmap):**
* **OpenAI:** Native wrappers for OpenAI Swarm and Assistants API.
* **Microsoft Ecosystem:** Telemetry hooks for Microsoft Copilot Studio and Semantic Kernel agents.
* **Google Cloud:** Integration for Google Gemini, Vertex AI, and Antigravity AI agents.
* **Universal REST API:** A language-agnostic sidecar proxy to hash outgoing LLM network requests for any custom-built agent.

---

## 📦 Installation

**Python (LangChain, CrewAI)**
```bash
pip install governance-hash-sdk
--
