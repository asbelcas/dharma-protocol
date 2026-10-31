"""Bonded Attestation Protocol v0.1 - minimal offline prototype (dharma13 Day 5).
Ledger = signed append-only log abstraction (list of dicts). No chain, no network.
Honesty scope (Day-12 audit): this module enforces an ATTESTATION FORMAT - it checks
fields, hashes as supplied by the caller, and arithmetic. It does not escrow value,
execute transfers, fetch artifacts, or verify outcomes; certify() requires an
outcome-check BINDING (condition + verifier_ref + deadline) per charter A1(c)."""
import json, hashlib, time
REQUIRED = {"claim_hash","statement_hash","artifact_hash","producer","bond_amount",
            "currency","issued_at","challenge_window_s","rule_ref","signature",
            "evidence_ref"}
def h(s): return hashlib.sha256(s.encode()).hexdigest()
class Attestation:
    def __init__(s, d):
        s.d = d
    def validate(s):
        missing = REQUIRED - set(s.d)
        if missing: return False, f"missing:{sorted(missing)}"
        if s.d["bond_amount"] <= 0: return False, "bond<=0"
        if s.d["statement_hash"] != s.d.get("statement_text_actual"):
            return False, "FORFEIT:statement-mismatch"
        if s.d["artifact_hash"] != s.d.get("artifact_actual"):
            return False, "FORFEIT:artifact-mismatch"
        if not s.d["signature"].startswith("sig:"):
            return False, "bad-signature"
        return True, "ok"
    def status(s, now=None):
        now = now or time.time()
        t0 = s.d["issued_at"]; W = s.d["challenge_window_s"]
        ok, why = s.validate()
        if not ok: return "forfeited", why
        # Time-based labels only: no challenge record, adjudication, or release event
        # exists in this prototype. "certified" = "window elapsed, no challenge
        # recorded in this log"; it moves no value.
        if now < t0 + W: return "challengable", "within window"
        if now < t0 + W + 30*86400: return "certified-partial", "window elapsed; no challenge recorded (time-based label; 50% release schedule not executed)"
        return "certified-full", "window elapsed; no challenge recorded (time-based label; no bond moved)"

# Anti gaming-by-documentation (added Day 5 from GPT-Nano adversary pass, 10-15; scope
# pinned by Day-12 audit): an attestation must bind an OUTCOME CHECK (a falsifiable
# condition to be verified post-hoc), not merely paperwork presence. This validates the
# binding's completeness; EXECUTING the check is the operator's duty.
def outcome_check(att):
    """Returns (bool, reason): True if attestation binds a verifiable outcome check."""
    oc = att.d.get("outcome_check")
    if not oc:
        return False, "NO-OUTCOME-LINK:paperwork-only attestation"
    if not oc.get("condition") or not oc.get("verifier_ref") or not oc.get("deadline"):
        return False, "OUTCOME-CHECK-INCOMPLETE:need condition+verifier_ref+deadline"
    return True, "outcome-linked"
def full_validate(s):
    ok, why = s.validate()
    if not ok: return False, why
    return outcome_check(s)
def certify(ledger, d):
    """Record an attestation in the ledger. Certification requires full_validate:
    format checks PLUS a bound outcome check (charter A1(c) - not optional)."""
    a = Attestation(d); ok, why = full_validate(a)
    ledger.append({"entry": "attest", "claim": d["claim_hash"], "valid": ok, "why": why,
                   "ts": time.time()})
    return ok, why

def forfeit_split(bond, challenger_bond, n_jurors=5):
    """Allocation ARITHMETIC for a forfeited bond: 30% challenger, 40% jury (split),
    30% consumers pool. No value moves; execution is out of scope for this prototype.
    challenger_bond is reserved for a future challenger-slashing rule (spec §5)."""
    jury = round(bond * 0.4 / n_jurors, 2)
    challenger = round(bond * 0.3, 2)
    return {"challenger": challenger, "jury_each": jury, "consumers_pool": round(bond*0.3,2)}
