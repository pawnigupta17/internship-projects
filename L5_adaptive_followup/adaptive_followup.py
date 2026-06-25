"""
L5 — Adaptive Follow-Up Logic
Assignee : Pawni Gupta
Captain  : Nikhil Patil
Deadline : 28 June 2026

Objective:
    Build AI-driven interview flow that adapts based on previous candidate responses.
    The AI generates a contextually relevant follow-up question from the candidate's
    previous answer.

Expected Output:
    Follow-up question string generated dynamically from prior answer context.
"""

import json
import urllib.request

# ── Configuration ──────────────────────────────────────────────────────────────

API_KEY = "paste-your-openrouter-key-here"
MODEL   = "openrouter/free"

# ── Core Logic ─────────────────────────────────────────────────────────────────

def generate_followup_question(
    job_role,
    previous_question,
    candidate_answer,
    conversation_history=None,
):
    history_block = ""
    if conversation_history:
        lines = []
        for i, turn in enumerate(conversation_history, 1):
            lines.append(f"Turn {i}:")
            lines.append(f"  Q: {turn['question']}")
            lines.append(f"  A: {turn['answer']}")
        history_block = "\n\nPrior conversation:\n" + "\n".join(lines)

    prompt = f"""You are an expert technical interviewer conducting a structured interview.
Your job is to generate ONE adaptive follow-up question that digs deeper into the candidate's previous answer.

The follow-up should:
- Probe gaps, vague claims, or interesting points the candidate raised
- Stay relevant to the job role
- Be open-ended and encourage elaboration
- NOT repeat what was already asked

Job Role: {job_role}{history_block}

Last Question Asked: {previous_question}
Candidate's Answer : {candidate_answer}

Respond ONLY with a JSON object, no markdown, no extra text:
{{"followup_question": "...", "reasoning": "...", "focus_area": "..."}}"""

    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST"
    )

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    raw_text = data["choices"][0]["message"]["content"].strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
        raw_text = raw_text.strip()

    result = json.loads(raw_text)
    return result


# ── Demo Runner ────────────────────────────────────────────────────────────────

def run_demo():
    job_role = "Backend Software Engineer"

    turns = [
        {
            "question": "Can you describe your experience with designing REST APIs?",
            "answer": (
                "I've designed several REST APIs at my previous company. "
                "We used FastAPI and followed standard HTTP conventions. "
                "I mostly worked on the authentication endpoints."
            ),
        },
        {
            "question": None,
            "answer": (
                "For authentication I implemented JWT tokens. "
                "We stored them in localStorage on the frontend. "
                "Refresh tokens were handled server-side with a 7-day expiry."
            ),
        },
    ]

    print("=" * 60)
    print("  L5 — Adaptive Follow-Up Logic  |  Assignee: Pawni Gupta")
    print("=" * 60)
    print(f"  Job Role : {job_role}\n")

    history = []

    for i, turn in enumerate(turns):
        q = turn["question"] if turn["question"] else "(follow-up from previous turn)"
        print(f"  [Turn {i+1}] Question : {q}")
        print(f"  [Turn {i+1}] Candidate: {turn['answer']}\n")

        result = generate_followup_question(
            job_role=job_role,
            previous_question=q,
            candidate_answer=turn["answer"],
            conversation_history=history if history else None,
        )

        print(f"  Follow-Up Question : {result['followup_question']}")
        print(f"  Focus Area         : {result['focus_area']}")
        print(f"  Reasoning          : {result['reasoning']}")
        print("-" * 60)

        history.append({"question": q, "answer": turn["answer"]})

        if i + 1 < len(turns) and turns[i + 1]["question"] is None:
            turns[i + 1]["question"] = result["followup_question"]

    print("\n  Done! Follow-up questions generated successfully.")


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_demo()
