# Day 5  Module 2 Start: Pre-trained Models & 3rd Party Platforms

## Focus
Started Module 2 with a mix of theory and hands-on practice, closing the
gap flagged in the Day 4 retrospective: prompt templates had only been
evaluated manually, never against a real LLM API.

## Theory
- **Pre-trained models**: what they are and why they're used instead of
  training from scratch leveraging large-scale pretraining instead of
  building a model per task.
- **Base vs. instruct/chat models**: base models predict raw continuations;
  instruct/chat models are fine-tuned to follow instructions and hold
  conversation, which is what both BISINDO AI and DocuMind rely on.
- **API providers**: Groq as the shared provider for both portfolio
  projects  running LLaMA 3.3 70B for BISINDO AI's gesture-to-sentence
  step and DocuMind's RAG answer generation.
- **API-level prompt mechanics**: system vs. user role in an actual API
  call (as opposed to Module 1's prompt-text-only view), token usage,
  temperature, and rate limits to watch for on Groq's free tier.

## Practice
- Set up Groq API access: API key stored in `.env`, excluded from git via
  `.gitignore` — key itself never committed.
- Ran the finalized `prompt_templates.py` (v1.0) against the real Groq API
  for the first time, replacing Day 3's manual/conceptual evaluation.
- Tested two templates end-to-end:
  - **RAG answer template (DocuMind)** — dummy retrieved context + query,
    since real document data isn't wired up yet.
  - **Gesture-to-sentence template (BISINDO AI)** — dummy gesture sequence
    input, since real MediaPipe output isn't wired up yet.
- Compared real API output against the Day 3 manual eval expectations to
  check whether the templates held up outside a conceptual walkthrough.

## Notes / Findings
- Real API output is the first concrete signal on whether the few-shot
  structure from Module 1 actually holds up with a live model — worth
  tracking closely once real BISINDO/DocuMind data is available, since
  dummy input can only validate format, not real-world edge cases.
- `.env` + `.gitignore` setup is now a reusable pattern for the rest of the
  sprint — any future API key (embeddings providers, vector DB, etc.) can
  follow the same setup.

## Next
Continue Module 2 — go deeper into 3rd-party platform options and how
model choice/config affects BISINDO AI and DocuMind specifically.
