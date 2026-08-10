# Day 6 Module 2: Comparing 3rd-Party Platforms & Model Configuration
    
## Focus
Went deeper into Module 2, picking up where Day 5 left off: moving past
"Groq works" to understanding *why* Groq (or any given platform) is the
right choice, and how model configuration should differ between BISINDO
AI and DocuMind rather than using one default setup for both.

## Theory
- **3rd-party platform landscape**: compared Groq against alternatives
  (Together AI, Hugging Face Inference API, OpenAI-compatible endpoints)
  across inference speed, pricing, model availability, and rate limits.
- **Why Groq for this sprint**: LPU-based inference gives low latency,
  which matters for BISINDO AI's real-time gesture-to-sentence step;
  free-tier availability makes it practical for a student sprint.
- **Model configuration as a design decision, not a default**:
  - `temperature`  low (~0.1-0.3) for BISINDO AI's gesture-to-sentence
    output, where consistency matters more than variety; moderate
    (~0.5-0.7) for DocuMind's RAG answers, where natural phrasing helps
    but grounding in retrieved context still needs to hold.
  - `max_tokens`  kept tight for gesture-to-sentence (short, single
    output); needs more headroom for RAG answers depending on context
    length.
  - `top_p`  noted as a secondary lever, mostly left at default unless
    temperature tuning isn't enough.

## Practice
- Re-ran `prompt_templates.py` against the real Groq API with varied
  `temperature` values for both templates (RAG answer, gesture-to-
  sentence) to observe how output changed.
- Logged output differences side-by-side for low vs. moderate
  temperature on the same dummy inputs from Day 5.
- Confirmed: low temperature kept gesture-to-sentence output stable
  across repeated calls; moderate temperature on RAG answers produced
  more natural phrasing without drifting from the dummy context.

## Notes / Findings
- Model config isn't one-size-fits-all across projects  BISINDO AI and
  DocuMind should carry different default configs going forward, not
  share a single settings block in `prompt_templates.py`.
- Platform choice (Groq specifically) is now justified by latency +
  cost fit, not just "it's what we set up on Day 5"  useful to have
  written down for the portfolio README later.

## Next
Continue Module 2  likely diving into structured output / function
calling behavior on 3rd-party platforms, still tying back to BISINDO AI
and DocuMind.
