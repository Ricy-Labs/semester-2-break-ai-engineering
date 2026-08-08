"""
Finalized prompt templates - v1.0
Module: Prompt Engineering (Day 1-4)

These are the production-ready versions of the templates drafted in
experiments/prompt_templates.py on Day 3. Selection was based on the
mini-evaluation results:
- Few-shot beat direct instruction for output consistency, especially on
  ambiguous input.
- Length constraints only help on long/rambling input - not included as a
  default, apply conditionally if needed later.
- Empty input is NOT handled here. It must be validated in code before
  these templates are called (see validate_input() usage note at the
  bottom of this file).
"""

# ---------------------------------------------------------------------------
# DocuMind - Query Rewriting
# Winner from Day 3 eval: few-shot variant (most consistent format across
# clear, ambiguous, and long/rambling inputs).
# ---------------------------------------------------------------------------

QUERY_REWRITE_TEMPLATE = """Rewrite the user's question into a clear,
standalone search query. Do not answer it, only rewrite it. If the question
is ambiguous, resolve the ambiguity using the most likely intent.

Example:
Question: "what about the pricing thing they mentioned earlier"
Rewritten: "product pricing details"

Question: {user_input}
Rewritten:"""


# ---------------------------------------------------------------------------
# DocuMind - RAG Answer Generation
# ---------------------------------------------------------------------------

RAG_ANSWER_TEMPLATE = """Given this context:
{context}

Answer the question using only the information in the context above.
If the answer is not in the context, say you don't know - do not guess or
use outside knowledge.

Question: {question}
Answer:"""


# ---------------------------------------------------------------------------
# BISINDO AI - Gesture Sequence to Sentence
# ---------------------------------------------------------------------------

BISINDO_GESTURE_TEMPLATE = """System: You are a translation assistant for
BISINDO gesture detection output. Convert the gesture sequence into a
natural Indonesian sentence. Do not add information not present in the
sequence.

If a gesture in the sequence is unclear or could map to more than one word,
list it in "ambiguous_words" instead of guessing silently.

Return ONLY valid JSON with this schema:
{{
  "sentence": string,
  "confidence": "high" | "medium" | "low",
  "ambiguous_words": string[]
}}

Gesture sequence: {gesture_sequence}"""


# ---------------------------------------------------------------------------
# Code-level validation (NOT a prompt concern - confirmed Day 3)
# Call this before passing user_input / gesture_sequence into the templates
# above. Keeping it here as a reference stub for when the actual DocuMind
# and BISINDO AI codebases are built in later modules.
# ---------------------------------------------------------------------------

def validate_input(value: str) -> bool:
    """Return False for empty/whitespace-only input.
    Templates above assume this check already passed."""
    return bool(value and value.strip())
