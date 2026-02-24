/**
 * LangChain.js callback handler for automatic governance hashing.
 */
import { sign, type Signature, type SignaturePolicy } from './core';

export class ScalarCallbackHandler {
  agentId: string;
  policyRef: string;
  privateKey?: string;
  policy: SignaturePolicy;
  latestHash: string | null = null;
  hashChain: Signature[] = [];

  constructor(opts: { agentId: string; policyRef: string; privateKey?: string }) {
    this.agentId = opts.agentId;
    this.policyRef = opts.policyRef;
    this.privateKey = opts.privateKey;
    this.policy = { requiredFields: ['action', 'agent_id'] };
  }

  async handleToolEnd(output: string): Promise<void> {
    const sig = await sign(
      { action: 'tool_execution', agent_id: this.agentId, output },
      this.policy,
      { privateKey: this.privateKey, previousHash: this.latestHash ?? 'genesis' }
    );
    this.latestHash = sig.hash;
    this.hashChain.push(sig);
  }

  async handleChainEnd(outputs: Record<string, unknown>): Promise<void> {
    const sig = await sign(
      { action: 'chain_completion', agent_id: this.agentId, output: JSON.stringify(outputs) },
      this.policy,
      { privateKey: this.privateKey, previousHash: this.latestHash ?? 'genesis' }
    );
    this.latestHash = sig.hash;
    this.hashChain.push(sig);
  }
}
