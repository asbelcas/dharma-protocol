# Charter v0.1+rev2 → rev3 — Amendment DRAFT (awaits operator review)
Status: DRAFT 2026-11-27. Not applied to the charter of record. Source: ChatGPT
advisory 2026-11-12 (revision set P1/P2 items not yet landed) + ENGINE-14 build-queue.
Merge = one click by the operator; until then rev2 governs.

## Amendment 1 — A3 becomes operational (P1)
Replace the A3 paragraph with:
> **A3 — Human ends, named signers.** Every automated action belongs to exactly one
> approved **action class**, and each action class has exactly one named accountable
> human signer with (a) informed assent to that class's risk profile, (b) live
> authority to halt, and (c) real causal control. Signer authority is **bounded**
> (named classes only), **expires** (reaffirmation at a stated interval, default 90
> days), and carries **escalation rules** (who acts when the signer is unreachable).
> A **halt drill** is executed and logged at least annually per deployment — an
> untested stop is a claimed stop, not a real one. The signer must be shown the
> strongest declined alternative with each single recommended approval. Multi-party
> systems use role-based signing. "The agent did it" is void.
Acceptance test: a revoked or expired authorization provably prevents further
consequential actions; a halt drill succeeds on record.

## Amendment 2 — A4 discloses knowledge limits (P1)
Add to A4 after the disclosure list:
> Disclosure uses four states — **known, unknown, not applicable, withheld (with
> reason)**. Model-training provenance upstream of the operator is declared
> *unknown* (it is unknowable in general); knowledge contributed directly to the
> operator's system is declared with owner and compensation status. An entry of
> *unknown* is never restated as identified, and withheld entries name the
> withholding rationale.
Acceptance test: unknown upstream contributors cannot be reported as identified or
compensated; every withheld entry carries a stated reason.

## Amendment 3 — A1 risk-tiering (P2)
Add to A1:
> Claims are tiered by consequence. **Material external claims** (payment, health,
> safety, legal standing, published output) require full evidence binding and the
> bound outcome check. **Low-risk communications** require the lightweight status
> label only. Where an outcome has matured, the outcome check executes on its
> stated deadline — a missing or overdue check is reported as unresolved, never
> treated as success.
Acceptance test: an overdue outcome check surfaces as unresolved in the audit log.

## Conformance section update
L1 bullet A3 gains: "signer authority bounded, expiring, halt-drilled." L1 bullet A4
gains: "disclosure uses known/unknown/n-a/withheld." L1 bullet A1 gains: "material
claims fully bound; matured checks execute on deadline." L2 unchanged.
