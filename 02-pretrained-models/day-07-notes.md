# Day 7  Module 2: Structured Output & Function Calling on 3rd-Party Platforms

## Focus
Continued from Day 6's "next" item: moved from prompt-level configuration
(temperature, max_tokens) into structured output getting the model to
return a fixed, parseable schema instead of free-form text. This matters
for both projects: DocuMind needs to expose source chunks and confidence
alongside the answer, and BISINDO AI needs a parseable sentence +
confidence score rather than raw text the UI would have to regex.

> **DRAFT unverified.** This section was pre-filled from Groq's official
> docs, not from an actual run. Re-check against real output tomorrow and
> correct anything that doesn't match.

## Theory
- **JSON mode / response format constraint**: Groq exposes two levels 
  `{"type": "json_object"}` (older JSON mode, only guarantees the output
  is valid JSON, not that it matches a specific schema) and
  `{"type": "json_schema"}` (Structured Outputs, guarantees the output
  matches a given schema, but only on a subset of newer models).
  `llama-3.3-70b-versatile` is likely NOT on the strict `json_schema`
  supported-model list, so `json_object` mode is the realistic option 
  valid JSON is guaranteed, exact schema match is not.
- **Function calling / tool use vs prompt-based JSON**: function calling
  lets the model decide which function to call and with what arguments,
  in a schema enforced by the platform; prompt-based JSON just asks the
  model nicely to format its own free text as JSON, with no enforcement.
- **Fallback strategy when no native schema enforcement**: strict system
  prompt instruction + output parser + retry-on-invalid-json, since
  `json_object` mode alone doesn't guarantee field names/types match.

## Practice
- Tested structured output for DocuMind (RAG answer) with schema:
  `{"answer": string, "source_chunks": [int], "confidence": "high"|"medium"|"low"}`
- Tested structured output for BISINDO AI (gesture-to-sentence) with schema:
  `{"sentence": string, "detected_gestures": [string], "confidence_score": float}`
- Used `response_format={"type": "json_object"}` with `llama-3.3-70b-versatile`,
  same dummy inputs from Day 5/6, low temperature (~0.1–0.3) per Day 6 findings.

## Notes / Findings
- Expected: output is valid JSON on every call (Groq guarantees this for
  `json_object` mode), but field types/names may drift slightly since
  schema isn't enforced — e.g. `confidence_score` occasionally returned
  as a string instead of a float, or an optional field omitted.
- Expected: `confidence` / `confidence_score` should still track context
  quality directionally (drop when context is irrelevant or gesture
  sequence is ambiguous), since that behavior comes from the prompt
  instructions, not from schema enforcement.
- Since exact schema isn't guaranteed on this model, a validation/parser
  layer (Step 4 from planning) is not optional — it's required for
  production use in both DocuMind and BISINDO AI.

## Next
Verify the above against real Groq output — confirm whether
`llama-3.3-70b-versatile` supports `json_schema` strict mode or is
limited to `json_object`. If strict schema support isn't available,
decide whether to switch to a supported model (e.g. one of Groq's newer
models with `json_schema` support) for the structured-output pieces of
DocuMind and BISINDO AI, or keep `llama-3.3-70b-versatile` with a
validation layer.
