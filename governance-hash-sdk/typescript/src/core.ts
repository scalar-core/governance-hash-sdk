/**
 * Core cryptographic signing for governance-hash-sdk (TypeScript).
 * Uses the Web Crypto API — works in Node 18+, Deno, and modern browsers.
 */

export interface SignaturePolicy {
  minEntropy?: number;
  requiredFields: string[];
}

export interface Signature {
  hash: string;
  payload: Record<string, unknown>;
  timestamp: string;
  nonce: string;
}

export async function sign(
  data: Record<string, unknown>,
  policy: SignaturePolicy,
  options: { privateKey?: string; previousHash?: string } = {}
): Promise<Signature> {
  const { privateKey, previousHash = 'genesis' } = options;

  for (const field of policy.requiredFields) {
    if (!(field in data)) {
      throw new Error(`Policy Violation: Missing required field '${field}'`);
    }
  }

  const timestamp = new Date().toISOString();
  const nonce = crypto.randomUUID();

  const payload: Record<string, unknown> = {
    ...data,
    _meta: { timestamp, nonce, previous_hash: previousHash },
  };

  const encoded = new TextEncoder().encode(JSON.stringify(payload, Object.keys(payload).sort()));

  let hashHex: string;

  if (privateKey) {
    const key = await crypto.subtle.importKey(
      'raw',
      new TextEncoder().encode(privateKey),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['sign']
    );
    const sig = await crypto.subtle.sign('HMAC', key, encoded);
    hashHex = Array.from(new Uint8Array(sig)).map(b => b.toString(16).padStart(2, '0')).join('');
  } else {
    const digest = await crypto.subtle.digest('SHA-256', encoded);
    hashHex = Array.from(new Uint8Array(digest)).map(b => b.toString(16).padStart(2, '0')).join('');
  }

  return { hash: `0x${hashHex}`, payload, timestamp, nonce };
}
