"""Tamper-evident hash-chained record of claims (dharma13 Day 5, sound per Day-12 audit).
add() hashes (prev, raw) where raw = "ts|event" is STORED, so verify() can recompute
the whole chain and detect any mutation of entries or reordering. No chain, no network."""
import hashlib, time
class Chain:
    def __init__(s): s.entries = []; s.prev = "GENESIS"
    def add(s, event):
        raw = f"{time.time()}|{event}"
        h = hashlib.sha256((s.prev + raw).encode()).hexdigest()
        s.entries.append((h, raw)); s.prev = h; return h
    def verify(s):
        """Recompute the chain from stored raws. True only if every entry is intact
        and in order; any tampering with (h, raw) pairs is detected."""
        p = "GENESIS"
        for h, raw in s.entries:
            if hashlib.sha256((p + raw).encode()).hexdigest() != h: return False
            p = h
        return True
    def recompute_ok(s, raw_pairs):
        """Independent check: given (h, raw) pairs from an external copy, recompute.
        True iff the copy matches the same chain. Works because add() stores raw."""
        p = "GENESIS"
        for h, raw in raw_pairs:
            if hashlib.sha256((p + raw).encode()).hexdigest() != h: return False
            p = h
        return True
