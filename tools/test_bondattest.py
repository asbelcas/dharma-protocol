import time, unittest, sys
sys.path.insert(0, '.')
from bondattest import Attestation, certify, forfeit_split
def mk(**kw):
    d = {"claim_hash":"c1","statement_hash":h("s"),"statement_text_actual":h("s"),
         "artifact_hash":h("a"),"artifact_actual":h("a"),"producer":"p1",
         "bond_amount":1000,"currency":"USD","issued_at":time.time()-40*86400,
         "challenge_window_s":7*86400,"rule_ref":"dap-v0.1","signature":"sig:p1",
         "evidence_ref":"evid:run-42"}
    d.update(kw); return d
h = lambda s: __import__('hashlib').sha256(s.encode()).hexdigest()
class T(unittest.TestCase):
    def test_valid_certifies_full(self):
        ok,why = Attestation(mk()).validate(); self.assertTrue(ok, why)
        self.assertEqual(Attestation(mk()).status()[0], "certified-full")
    def test_missing_field_fails(self):
        d = mk(); del d["bond_amount"]
        self.assertFalse(Attestation(d).validate()[0])
    def test_zero_bond_fails(self):
        self.assertFalse(Attestation(mk(bond_amount=0)).validate()[0])
    def test_statement_mismatch_forfeits(self):
        self.assertIn("FORFEIT", Attestation(mk(statement_text_actual=h("evil"))).validate()[1])
    def test_artifact_mismatch_forfeits(self):
        self.assertIn("FORFEIT", Attestation(mk(artifact_actual=h("evil"))).validate()[1])
    def test_within_window_challengable(self):
        self.assertEqual(Attestation(mk(issued_at=time.time())).status()[0], "challengable")
    def test_partial_release(self):
        self.assertEqual(Attestation(mk(issued_at=time.time()-20*86400)).status()[0], "certified-partial")
    def test_forfeit_split_math(self):
        p = forfeit_split(1000, 50)
        self.assertEqual(p["challenger"], 300.0); self.assertEqual(p["jury_each"], 80.0)
    def test_ledger_records(self):
        L = []; ok, why = certify(L, mk(statement_text_actual="x"))
        self.assertFalse(ok); self.assertEqual(len(L), 1); self.assertFalse(L[0]["valid"])
    def test_certify_requires_outcome_check(self):
        L = []; ok, why = certify(L, mk())  # valid format, no outcome_check bound
        self.assertFalse(ok); self.assertIn("OUTCOME", why)
    def test_certify_passes_with_outcome_check(self):
        L = []; d = mk(outcome_check={"condition":"c","verifier_ref":"v","deadline":30})
        ok, why = certify(L, d); self.assertTrue(ok, why)
if __name__ == "__main__": unittest.main(verbosity=0)

class T2(unittest.TestCase):
    def test_paperwork_only_flagged(self):
        from bondattest import outcome_check, full_validate
        self.assertFalse(outcome_check(Attestation(mk()))[0])
    def test_outcome_linked_passes(self):
        from bondattest import full_validate
        d = mk(outcome_check={"condition":"emitted PNGs match spec table",
                              "verifier_ref":"tests/integration","deadline":30})
        self.assertTrue(full_validate(Attestation(d))[0])
    def test_incomplete_outcome_check_fails(self):
        from bondattest import full_validate
        d = mk(outcome_check={"condition":"x"})
        self.assertFalse(full_validate(Attestation(d))[0])
if __name__ == "__main__": unittest.main(verbosity=0)
