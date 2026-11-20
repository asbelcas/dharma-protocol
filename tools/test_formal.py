import unittest, sys, os
sys.path.insert(0, '.')
from hashchain import Chain
from sim_econ import run
class F(unittest.TestCase):
    def test_chain_tamper_detected(self):
        c = Chain(); c.add("claim A"); c.add("claim B")
        self.assertTrue(c.verify())                 # intact chain verifies
        h0, raw0 = c.entries[0]
        c.entries[0] = (h0, "forged raw")           # tamper with stored content
        self.assertFalse(c.verify())                # ... and verification fails
    def test_chain_order_matters(self):
        a = Chain(); a.add("X"); a.add("Y")
        b = Chain(); b.add("Y"); b.add("X")
        self.assertNotEqual(a.prev, b.prev)
    def test_sim_bonds_punish_liars(self):
        nb = run(use_bonds=False, rounds=800, agents=30, seed=7)
        b = run(use_bonds=True, rounds=800, agents=30, seed=7)
        self.assertLess(b["liar_avg_wealth"], nb["liar_avg_wealth"])
        self.assertLess(b["liars_prospering"], nb["liars_prospering"])
    def test_bonded_honest_outearn_liars(self):
        b = run(use_bonds=True, rounds=500, agents=20, seed=7)
        self.assertGreater(b["honest_avg_wealth"], b["liar_avg_wealth"])
    def test_chain_recompute_ok(self):
        c = Chain(); c.add("A"); c.add("B")
        self.assertTrue(c.recompute_ok(list(c.entries)))   # stored raws recompute
        h1, raw1 = c.entries[1]
        self.assertFalse(c.recompute_ok([(h1, "EVIL")]))  # tampered pair rejected
    def test_chain_full_replacement_rejected_by_anchor(self):
        c = Chain(); c.add("claim A"); c.add("claim B")
        tip, n = c.prev, len(c.entries)
        forged = Chain(); forged.add("forged A"); forged.add("forged B")
        self.assertTrue(forged.verify())                        # forged chain self-consistent...
        self.assertFalse(forged.verify(expected_tip=tip, expected_len=n))  # ...anchor rejects it
        self.assertFalse(forged.verify(expected_tip=tip))       # tip alone suffices
        self.assertTrue(c.verify(expected_tip=tip, expected_len=n))        # genuine chain passes
    def test_chain_truncation_rejected_by_anchor(self):
        c = Chain(); c.add("A"); c.add("B"); c.add("C")
        tip, n = c.prev, len(c.entries)
        t = Chain(); t.entries = list(c.entries[:2]); t.prev = t.entries[-1][0]
        self.assertTrue(t.verify())                             # truncated prefix self-consistent...
        self.assertFalse(t.verify(expected_tip=tip, expected_len=n))       # ...count catches it
        self.assertFalse(t.verify(expected_tip=tip))            # tip alone catches it
if __name__ == "__main__": unittest.main(verbosity=0)
