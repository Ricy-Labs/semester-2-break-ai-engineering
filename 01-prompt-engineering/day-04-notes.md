# Day 4 - Prompt Engineering Wrap-up
 
## Focus
Closed out Module 1 by finalizing the prompt templates drafted on Day 3 and
reviewing the module as a whole before moving into Module 2 (Pre-trained
Models & 3rd Party Platforms).

## Finalized Templates
Promoted the Day 3 draft templates to production-ready versions based on
the mini-evaluation results. See `prompt_templates.py` (v1.0).

Changes from draft to final:
- **Query rewrite (DocuMind):** switched to the few-shot variant, since it
  was the most consistent across clear, ambiguous, and long input in the
  Day 3 eval. Direct instruction was dropped as the default.
- **RAG answer (DocuMind):** kept the original structure, made the
  "don't guess" instruction more explicit to reduce hallucination risk.
- **Gesture-to-sentence (BISINDO AI):** kept the JSON schema, added explicit
  instruction to route unclear gestures into `ambiguous_words` instead of
  silently guessing.
- **Input validation:** confirmed this stays out of the prompt entirely.
  Added a `validate_input()` stub as a placeholder for when the actual
  DocuMind/BISINDO AI codebases are built - empty input never reaches
  these templates.

## Module 1 Retrospective

**What worked:**
- Few-shot examples were consistently more reliable than adding more
  instructions - this was the single most useful finding of the module,
  and it will carry into template design for later modules too (e.g.
  RAG prompt design in Module 5).
- Treating prompts as parameterized templates from Day 3 onward, instead
  of one-off strings, made the Day 4 finalization step straightforward -
  there was a clear "draft vs final" version to compare instead of
  starting from scratch.

**Gaps / things to watch:**
- Evaluation in Day 3 was manual and small-scale (4 inputs, 3 variants).
  Good enough to catch obvious inconsistencies, but not rigorous. A more
  structured evaluation approach will matter more once RAG and Agents
  modules introduce multi-step outputs.
- Haven't yet tested these templates against a real LLM API with real
  BISINDO gesture data or real DocuMind documents - all evaluation so far
  has been manual/conceptual. Real testing starts once Module 2 covers
  working with pre-trained models and APIs directly.

**In three sentences - what is prompt engineering (for future reference):**
Prompt engineering is designing the input to a language model so its output
is consistent, correct, and usable in a larger system. It relies more on
structure (few-shot examples, clear constraints, defined output format)
than on adding more instructions. Some problems - like empty or malformed
input - are not prompt problems at all and belong in code.

## Module 1 Summary
| Day | Focus |
|-----|-------|
| 1 | Git/GitHub setup, repo structure |
| 2 | Prompt chaining, system vs user prompt, structured output, eval basics |
| 3 | Reusable parameterized templates, manual mini-evaluation |
| 4 | Finalized templates (v1.0), module retrospective |

## Next
Module 2 - Pre-trained Models & 3rd Party Platforms starts Day 5.
