# L5 — Adaptive Follow-Up Logic

**Assignee:** Pawni Gupta  
**Captain:** Nikhil Patil  
**Module:** AI / LLM Interview Engine  
**Deadline:** 28 June 2026 (Saturday)

---

## Problem Statement

In a real interview, good interviewers don't just read from a fixed list — they listen to the candidate's answers and ask targeted follow-up questions that probe gaps, vague claims, or interesting points. This task replicates that behaviour using an LLM (OpenRouter API).

The system takes:
- The **job role** being interviewed for
- The **previous question** that was asked
- The **candidate's answer** to that question
- Optional **conversation history** for multi-turn sessions

…and returns a dynamically generated follow-up question, along with the competency it probes and the reasoning behind it.

---

## Installation Guide

```bash
# 1. Clone / navigate to this folder
cd L5_adaptive_followup

# 2. No external dependencies required — uses Python built-in libraries only

# 3. Get your free API key from https://openrouter.ai
#    Sign up with Google → API Keys → Create Key → copy it

# 4. Paste your API key in line 21 of adaptive_followup.py
#    API_KEY = "sk-or-v1-your-key-here"

# 5. Run the demo
python adaptive_followup.py
```

---

## How It Works

```
┌─────────────────────────────────────────────────┐
│          generate_followup_question()            │
│                                                  │
│  Input:                                          │
│    job_role           → "Backend Engineer"       │
│    previous_question  → "Tell me about REST APIs"│
│    candidate_answer   → "I used FastAPI and JWT…"│
│    conversation_history (optional) → [...]       │
│                                                  │
│  OpenRouter API Call:                            │
│    Prompt → expert interviewer, return JSON only │
│                                                  │
│  Output:                                         │
│    followup_question  → adaptive follow-up       │
│    focus_area         → competency being probed  │
│    reasoning          → why this was chosen      │
└─────────────────────────────────────────────────┘
```

---

## Sample JSON Output

```json
{
  "followup_question": "You mentioned storing JWT tokens in localStorage — what are the security trade-offs of that approach, and would you consider an alternative?",
  "focus_area": "Security awareness",
  "reasoning": "The candidate described a pattern (localStorage for JWTs) that is widely considered a security risk due to XSS vulnerabilities. The follow-up probes whether they are aware of this trade-off and can reason about alternatives like httpOnly cookies."
}
```

---

## Function Signature

```python
generate_followup_question(
    job_role,
    previous_question,
    candidate_answer,
    conversation_history=None,
)
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `job_role` | Position being interviewed for |
| `previous_question` | The question just asked |
| `candidate_answer` | Candidate's response |
| `conversation_history` | Optional list of prior `{question, answer}` pairs |

### Returns

| Key | Description |
|-----|-------------|
| `followup_question` | The dynamically generated follow-up |
| `focus_area` | Competency being probed |
| `reasoning` | Why this follow-up was chosen |

---

## Edge Cases Handled

| Edge Case | Handling |
|-----------|----------|
| Vague / one-word answers | LLM asks candidate to elaborate |
| No conversation history | Works with single Q&A pair only |
| LLM returns markdown fences | Stripped before JSON parsing |
| Multi-turn sessions | Full history passed for context continuity |

---

## Acceptance Criteria

- Follow-up question is contextually relevant to the candidate's answer
- JSON output matches the expected structure
- Works without conversation history (single-turn)
- Works with full multi-turn history
- Edge cases handled (vague answers, markdown in LLM output)
