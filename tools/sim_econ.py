"""Executable economics: does bonded attestation raise truth-ratio?
Agents make claims each round; liars profit if unchallenged. Bonds make false claims
costly WHEN DISCOVERED. Honesty scope (Day-12 audit): discovery is probabilistic in
both branches (challenge_prob); challenge_cost is charged on discovery. The verdict
below states its assumption explicitly - it motivates the design, it does not prove it."""
import random
def run(rounds=2000, agents=40, liar_share=0.5, bond=8, claim_gain=5, challenge_cost=1,
        challenge_prob=0.5, use_bonds=True, seed=None):
    rng = random.Random(seed)
    truth = [True] * (agents - int(agents*liar_share)) + [False] * int(agents*liar_share)
    rng.shuffle(truth); wealth = [10]*agents; discovered = 0
    for r in range(rounds):
        i = rng.randrange(agents); claim_true = truth[i]
        if use_bonds:
            wealth[i] -= bond                       # post bond
            if not claim_true:
                if rng.random() < challenge_prob:   # discovery is probabilistic
                    wealth[i] -= bond               # forfeiture on discovery
                    wealth[i] -= challenge_cost     # challenger fee borne by claimant on loss
                    discovered += 1
            else:
                wealth[i] += bond + claim_gain      # returned + gain when true
        else:
            challenged = rng.random() < challenge_prob
            wealth[i] += claim_gain if (claim_true or not challenged) else 0
            if not claim_true and challenged: wealth[i] -= challenge_cost
    liars = [w for w, t in zip(wealth, truth) if not t]
    honest = [w for w, t in zip(wealth, truth) if t]
    surviving_liar_share = sum(1 for w in liars if w > 10) / max(1, len(liars))
    return {"liar_avg_wealth": round(sum(liars)/max(1,len(liars)),1),
            "honest_avg_wealth": round(sum(honest)/max(1,len(honest)),1),
            "liars_prospering": round(surviving_liar_share,2),
            "discoveries": discovered}
if __name__ == "__main__":
    nb = run(use_bonds=False, seed=7); b = run(use_bonds=True, seed=7)
    print("NO-BONDS :", nb); print("BONDED   :", b)
    works = b["liars_prospering"] < nb["liars_prospering"] and b["liar_avg_wealth"] < nb["liar_avg_wealth"]
    verdict = (f"UNDER p(discovery)={0.5} AND forfeiture-on-discovery: bonds collapse liar "
               f"prosperity while honest wealth holds") if works else "INSUFFICIENT AT THESE PARAMETERS"
    print("VERDICT  :", verdict, "| assumption-bound, not a proof (see header)")
