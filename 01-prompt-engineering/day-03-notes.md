# Day 3 - Prompt Engineering (Applied)

## Focus
Shifted from learning individual concepts to combining them into reusable,
testable prompt templates - the last practical step before wrapping up the
Prompt Engineering module on Day 4.

## Reusable Prompt Templates
Built a small set of parameterized templates meant to be reused directly in
DocuMind and BISINDO AI, instead of one-off prompt strings.

```python
# experiments/prompt_templates.py

QUERY_REWRITE_TEMPLATE = """Rewrite the following user question into a
clear, standalone search query. Do not answer it, only rewrite it.

Question: {user_input}"""

RAG_ANSWER_TEMPLATE = """Given this context:
{context}

Answer the question using only the information in the context above.
If the answer is not in the context, say you don't know.

Question: {question}"""

BISINDO_GESTURE_TEMPLATE = """System: You are a translation assistant for
BISINDO gesture detection output. Convert the gesture sequence into a
natural Indonesian sentence. Do not add information not present in the
sequence.

Return ONLY valid JSON with this schema:
{{
  "sentence": string,
  "confidence": "high" | "medium" | "low",
  "ambiguous_words": string[]
}}

Gesture sequence: {gesture_sequence}"""
```

Key design decision: templates take named variables (`{context}`,
`{question}`, `{gesture_sequence}`) instead of hardcoded text, so they can
be called as functions later once the codebase for DocuMind/BISINDO AI
exists.

## Mini Evaluation Exercise
Took the query rewriting template and tested 3 variants manually:

1. **Direct instruction** - "Rewrite into a standalone search query."
2. **With example (few-shot)** - added one input/output example before the
   instruction.
3. **With constraint** - added "Keep it under 15 words" to the instruction.

Tested each variant against 4 inputs: a clear question, a vague/ambiguous
question, an empty input, and a very long rambling input.

**Observations:**
- Direct instruction alone was inconsistent on the ambiguous input - the
  rewritten query sometimes kept the ambiguity instead of resolving it.
- Few-shot variant produced the most consistent format across all 4 cases.
- The length constraint helped on the long/rambling input but had no effect
  on the other three - not worth adding as a default, better used
  conditionally.
- Empty input was not handled well by any variant - needs explicit
  input validation in code before it reaches the prompt at all, not
  something to solve with prompt wording.

## Takeaway
A prompt that works on a clear example doesn't necessarily work on messy or
ambiguous input - inconsistency shows up specifically at the edges. Few-shot
examples helped more than extra instructions for keeping output format
consistent. Also confirmed that some problems (like empty input) belong in
code-level validation, not in the prompt itself. Ready to close out Prompt
Engineering on Day 4 and move into Pre-trained Models & 3rd Party Platforms.
