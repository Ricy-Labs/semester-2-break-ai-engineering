# Day 2 - Prompt Engineering (Advanced)

## Topics Covered
- Prompt chaining
- System prompt vs user prompt
- Structured output (JSON mode)
- Prompt evaluation and iteration

## Prompt Chaining
Breaking a complex task into multiple sequential prompts, where the output of
one step becomes the input of the next, instead of trying to solve everything
in a single prompt.

Example use case relevant to DocuMind (RAG pipeline):
1. Step 1: Rewrite/clarify the user's raw query
2. Step 2: Use the rewritten query for retrieval
3. Step 3: Generate the final answer using retrieved context

```
Step 1 prompt:
"Rewrite the following user question into a clear, standalone search query.
Question: {user_input}"

Step 2 prompt:
"Given this context: {retrieved_chunks}
Answer the question: {rewritten_query}"
```

Chaining makes each step easier to debug and evaluate individually, compared
to one large prompt trying to do retrieval reasoning and answer generation at
once.

## System Prompt vs User Prompt
- **System prompt**: defines the model's role, constraints, and behavior for
  the whole conversation. Set once, rarely changes per request.
- **User prompt**: the actual task/question for that specific turn.

Example system prompt for BISINDO AI (gesture-to-text assistant):
```
System: You are a translation assistant for BISINDO (Indonesian Sign
Language) gesture detection output. You receive a sequence of detected
gesture labels and must convert them into a natural, grammatically correct
Indonesian sentence. Do not add information that wasn't in the gesture
sequence. If the sequence is ambiguous, output the most literal
interpretation.
```

Separating role/constraints (system) from the actual input (user) keeps
behavior consistent even when the input changes every request.

## Structured Output (JSON Mode)
Asking the model to return output in a strict, parseable format instead of
free text - necessary for anything that feeds into code (API responses,
function calling, agent tool inputs).

Example for BISINDO AI's gesture translation step:
```
Prompt:
"Convert the following gesture sequence into a sentence.
Return ONLY valid JSON with this schema:
{
  "sentence": string,
  "confidence": "high" | "medium" | "low",
  "ambiguous_words": string[]
}

Gesture sequence: {input}"
```

Key point: always validate the returned JSON in code (try/except or schema
validation) - the model can still occasionally return malformed output even
when instructed.

## Prompt Evaluation & Iteration
A prompt isn't "done" after it works once. Basic evaluation approach:
1. Write 3-5 variants of the same prompt (different phrasing, different
   instruction order, with/without examples)
2. Run each variant against the same set of test inputs, including edge
   cases (empty input, ambiguous input, very long input)
3. Compare outputs for consistency, not just "looks correct once"

This matters directly for DocuMind and BISINDO AI, where prompts will run on
inputs the model hasn't seen during manual testing.

## Takeaway
Today's focus shifted from "how to phrase one prompt" to "how to structure
multiple prompts as a reliable pipeline" - chaining, strict output format,
and testing across variants. This is the direction needed before moving into
pre-trained models and 3rd party platforms, where prompts stop being
one-off experiments and start being pipeline components.
