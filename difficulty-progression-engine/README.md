# B11 — Difficulty Progression Engine

A Python module that determines the next question's difficulty level based on a predefined progression rule.

## Progression Rule

Question 1 → Easy
Question 2 → Easy
Question 3 → Medium
Question 4 → Medium
Question 5+ → Hard

## Output Format

```json
{
  "next_question_level": "Medium"
}
```

## How to Run

### Run the Engine Demo
```bash
python engine.py
```

### Run Tests
```bash
python test_engine.py
```

## Edge Cases Handled

| Scenario | Behaviour |
|---|---|
| None or negative index | Defaults to Easy |
| Skipped question | Does not advance; repeats the same level |
| Missing or empty answer | Does not advance; repeats the same level |
| Index beyond progression | Returns Hard (final level) |

## Tech Stack
- Language: Python 3
- No external dependencies

