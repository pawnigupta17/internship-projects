"""
Unit Tests for Difficulty Progression Engine
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import get_next_question_level, get_level_for_position

# Simple test runner (no external libraries needed)
passed = 0
failed = 0


def test(name, result, expected):
    global passed, failed
    if result == expected:
        print(f"  ✅ PASS: {name}")
        passed += 1
    else:
        print(f"  ❌ FAIL: {name}")
        print(f"         Expected: {expected}")
        print(f"         Got:      {result}")
        failed += 1


print("=" * 55)
print("  RUNNING UNIT TESTS")
print("=" * 55)

# ── Normal Progression Tests ──────────────────────────────
print("\n📋 Normal Progression:")
test("Position 1 → Easy",   get_level_for_position(1), {"next_question_level": "Easy"})
test("Position 2 → Easy",   get_level_for_position(2), {"next_question_level": "Easy"})
test("Position 3 → Medium", get_level_for_position(3), {"next_question_level": "Medium"})
test("Position 4 → Medium", get_level_for_position(4), {"next_question_level": "Medium"})
test("Position 5 → Hard",   get_level_for_position(5), {"next_question_level": "Hard"})

# ── Advancing via get_next_question_level ─────────────────
print("\n🔁 Advancing through progression:")
test("Index 0 + answer → Easy",   get_next_question_level(0, answer="Paris"), {"next_question_level": "Easy"})
test("Index 1 + answer → Medium", get_next_question_level(1, answer="Berlin"), {"next_question_level": "Medium"})
test("Index 2 + answer → Medium", get_next_question_level(2, answer="Tokyo"), {"next_question_level": "Medium"})
test("Index 3 + answer → Hard",   get_next_question_level(3, answer="Rome"), {"next_question_level": "Hard"})

# ── Edge Cases ────────────────────────────────────────────
print("\n⚠️  Edge Cases:")
test("None index → Easy",          get_next_question_level(None), {"next_question_level": "Easy"})
test("Negative index → Easy",      get_next_question_level(-1),   {"next_question_level": "Easy"})
test("Skipped question",           get_next_question_level(1, skipped=True), {"next_question_level": "Easy"})
test("Empty string answer",        get_next_question_level(1, answer=""),    {"next_question_level": "Easy"})
test("None answer",                get_next_question_level(1, answer=None),  {"next_question_level": "Easy"})
test("Beyond range → Hard",        get_next_question_level(10, answer="x"),  {"next_question_level": "Hard"})
test("Position 0 (invalid) → Easy",get_level_for_position(0),               {"next_question_level": "Easy"})
test("Position 99 → Hard",         get_level_for_position(99),              {"next_question_level": "Hard"})

# ── Summary ───────────────────────────────────────────────
print("\n" + "=" * 55)
print(f"  Results: {passed} passed, {failed} failed out of {passed+failed} tests")
print("=" * 55)

if failed == 0:
    print("  🎉 All tests passed!")
else:
    print("  ⚠️  Some tests failed. Please review the engine.")
    sys.exit(1)
