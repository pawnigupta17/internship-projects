"""
Difficulty Progression Engine
==============================
Determines the next question's difficulty level based on a
predefined progression: Easy → Easy → Medium → Medium → Hard
"""

# Predefined difficulty progression (0-indexed)
DIFFICULTY_PROGRESSION = ["Easy", "Easy", "Medium", "Medium", "Hard"]


def get_next_question_level(current_index, answer=None, skipped=False):
    """
    Returns the next question's difficulty level.

    Parameters:
        current_index (int or None): The index of the NEXT question (0-based).
                                     Pass None or negative to start from beginning.
        answer (str or None):        The user's answer to the previous question.
                                     None means answer is missing.
        skipped (bool):              True if the previous question was skipped.

    Returns:
        dict: {"next_question_level": "<Easy|Medium|Hard>"}
    """

    # Edge Case 1: Missing or invalid index → start from beginning
    if current_index is None or not isinstance(current_index, int) or current_index < 0:
        return {"next_question_level": DIFFICULTY_PROGRESSION[0]}

    # Edge Case 2: Skipped question → don't advance, repeat same level
    if skipped:
        # Clamp to valid range
        safe_index = min(current_index, len(DIFFICULTY_PROGRESSION) - 1)
        return {"next_question_level": DIFFICULTY_PROGRESSION[safe_index]}

    # Edge Case 3: Missing answer → don't advance, repeat same level
    if answer is None or str(answer).strip() == "":
        safe_index = min(current_index, len(DIFFICULTY_PROGRESSION) - 1)
        return {"next_question_level": DIFFICULTY_PROGRESSION[safe_index]}

    # Normal flow: advance to the next position
    next_index = current_index + 1

    # Edge Case 4: Beyond the progression → stay at the last level (Hard)
    if next_index >= len(DIFFICULTY_PROGRESSION):
        return {"next_question_level": DIFFICULTY_PROGRESSION[-1]}

    return {"next_question_level": DIFFICULTY_PROGRESSION[next_index]}


def get_level_for_position(position):
    """
    Directly returns the difficulty level for a given question position (1-based).

    Parameters:
        position (int): Question number (1, 2, 3, 4, 5, ...)

    Returns:
        dict: {"next_question_level": "<Easy|Medium|Hard>"}
    """
    if position is None or not isinstance(position, int) or position < 1:
        return {"next_question_level": "Easy"}

    index = position - 1  # Convert to 0-based

    if index >= len(DIFFICULTY_PROGRESSION):
        return {"next_question_level": "Hard"}

    return {"next_question_level": DIFFICULTY_PROGRESSION[index]}


# ─────────────────────────────────────────────
# Demo / Manual Testing
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  DIFFICULTY PROGRESSION ENGINE - DEMO")
    print("=" * 50)

    print("\n📋 Full Progression (positions 1–5):")
    for i in range(1, 6):
        result = get_level_for_position(i)
        print(f"  Question {i} → {result['next_question_level']}")

    print("\n⚠️  Edge Cases:")

    result = get_next_question_level(None, answer=None)
    print(f"  Missing index, no answer     → {result}")

    result = get_next_question_level(1, skipped=True)
    print(f"  Question skipped             → {result}")

    result = get_next_question_level(1, answer="")
    print(f"  Empty answer                 → {result}")

    result = get_next_question_level(1, answer="Paris")
    print(f"  Valid answer at index 1      → {result}")

    result = get_next_question_level(10, answer="anything")
    print(f"  Beyond progression (index 10)→ {result}")

    print("\n✅ Engine working correctly!")
