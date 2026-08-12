# Day 8 — Module 2: Verifying Structured Output on Groq

## Focus
Followed up on Day 7's open item: verify against real Groq output whether
`llama-3.3-70b-versatile` supports strict `json_schema` mode, or is limited
to `json_object` mode as suspected.

> **DRAFT — Result section is theory-based, not from an actual saved run.**
> The real test was run earlier today but output wasn't kept/logged.
> Re-run and paste actual output next session to replace the Result
> section below with observed data.

## What was tested
- Called Groq API with `llama-3.3-70b-versatile`
- Tried `response_format={"type": "json_schema", ...}` with the DocuMind
  and/or BISINDO AI schemas from Day 7
- Compared against `response_format={"type": "json_object"}`

## Result
> Note: actual run output wasn't saved/retained. The below is a
> theory-based expectation, not an observed result — replace with real
> output next time the test is re-run.

- `json_schema` strict mode: expected to either be rejected by the API
  (unsupported parameter combo for this model) or accepted but silently
  ignored/not strictly enforced — i.e. it behaves like `json_object`
  under the hood rather than guaranteeing schema conformance.
- `json_object` mode: expected to always return valid JSON, but with
  occasional field-level drift consistent with Day 7's prediction — e.g.
  `confidence_score` returned as a string instead of a float, or fields
  reordered/renamed slightly across calls.
- Deviation from Day 7 predictions: none expected; this run is treated
  as confirming Day 7's theory rather than revealing new behavior.

## Decision
Keep `llama-3.3-70b-versatile` and treat `json_object` mode + a
validation/parser layer as required, not optional, for both DocuMind and
BISINDO AI.

Reasoning: Groq's own structured-outputs documentation demonstrates
`llama-3.3-70b-versatile` using prompt-based JSON formatting (schema
described in the system prompt), not strict `json_schema` enforcement.
Independent sources checked while writing this confirm the model has no
JSON-schema enforcement and can require retry loops when strict structure
is needed. This matches Day 7's prediction exactly, so the fallback
strategy already planned — strict system prompt + output parser +
retry-on-invalid-json — stands as the production approach rather than a
contingency.

This does not block either project: DocuMind and BISINDO AI were already
scoped assuming a parser layer might be needed (see Day 7 "Fallback
strategy" note), so no rework — just confirmation to build it as planned.
