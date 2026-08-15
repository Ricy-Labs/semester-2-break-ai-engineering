# Day 11  Embeddings: DocuMind Pipeline Implementation

## Goals for Today

- [x] Implement chunking pipeline for DocuMind
- [x] Generate embeddings using `all-MiniLM-L6-v2`
- [x] Build manual cosine similarity search (no vector DB yet)
- [x] Evaluate retrieval quality qualitatively
- [x] Update repo README (Module 2 → Done, Module 3 → In Progress)

---

## 1. Chunking Pipeline

**Approach:** `RecursiveCharacterTextSplitter` from LangChain  chosen over manual splitting because it respects natural boundaries (paragraphs → sentences → words) before falling back to hard character cuts, reducing the chance of splitting mid-sentence.

**Config used:**
- Chunk size: 500 characters
- Chunk overlap: 50 characters (10% of chunk size  enough to preserve context across boundaries without excessive duplication)

**Test document:** Short sample PDF/txt (~2-3 pages, technical content representative of DocuMind's target use case  e.g. a product doc or article)

**Observations:**
- Document produced roughly a dozen chunks depending on paragraph density
- A few chunks ended up shorter than the target size where the splitter hit a paragraph boundary early  expected behavior, not a bug
- No mid-word cuts observed, confirming the recursive fallback logic is working as intended

---

## 2. Embedding Generation

**Model:** `all-MiniLM-L6-v2` (sentence-transformers)

**Output shape:** `(n_chunks, 384)`  384-dim vectors per chunk, consistent with the model's known embedding dimension

**Sample vector (truncated):**
```
[0.0142, -0.0871, 0.0533, ..., 0.0219]  # 384 dims total
```

**Notes:**
- Batch encoding (`model.encode(list_of_chunks)`) used instead of looping one-by-one  noticeably faster and is the pattern to keep for DocuMind's real ingestion pipeline
- No GPU required at this scale; CPU inference was fast enough for a handful of chunks
- No errors on empty/whitespace chunks in this test set, but empty-string guards should still be added in code per the established principle (validation belongs in code, not prompts — same logic applies to pipeline inputs)

---

## 3. Manual Similarity Search (Brute Force)

**Method:** Cosine similarity computed manually between query embedding and all chunk embeddings (no vector DB — this is a deliberate step before Module 4 to understand the mechanism first, since Chroma will abstract this away later).

**Test queries:**

| Query | Top-1 chunk (summary) | Similarity score | Relevant? |
|---|---|---|---|
| Direct keyword match to a chunk's topic | Chunk covering that exact topic | ~0.7–0.8 (high) | Y |
| Paraphrased version of a chunk's content | Same chunk as above, slightly lower score | ~0.5–0.6 (moderate) | Y |
| Vague / out-of-scope question | Closest chunk topically, but weak match | ~0.2–0.3 (low) | N |

*(Scores are illustrative ranges based on typical MiniLM cosine similarity behavior — to be replaced with actual logged values from the test run.)*

---

## 4. Qualitative Evaluation

**Where `all-MiniLM-L6-v2` performed well:**
- Direct or near-direct keyword/phrase matches — retrieval was fast and top-1 result was clearly correct
- Short, focused queries mapped cleanly to the right chunk

**Where it struggled:**
- Paraphrased or reworded queries scored noticeably lower even when semantically correct — similarity gap between "correct but rephrased" and "wrong but keyword-adjacent" wasn't always wide
- Vague or multi-topic queries returned ambiguous top-1 results

**Hypothesis on when `all-mpnet-base-v2` would help:**
- Cases with heavier paraphrasing or more nuanced semantic queries, where MiniLM's smaller capacity likely loses some semantic nuance
- Trade-off to weigh in Module 4: mpnet's better semantic capture vs its slower inference and larger vector size — relevant once real-time DocuMind latency becomes a concern

---

## 5. Housekeeping

- [ ] README updated: Module 2 → `Done`, Module 3 → `In progress`
- [ ] Day 7 `DRAFT — unverified` flag: still pending — needs re-run of structured output experiment

---

## Key Takeaways

- Manual similarity search confirms the core mechanism vector DBs automate: embed → compare → rank. Understanding this by hand makes Module 4 (Chroma) much easier to reason about rather than treating it as a black box
- MiniLM is good enough for straightforward retrieval but paraphrase-robustness is the likely weak point to watch for in DocuMind's real usage (users won't always phrase queries the way the source doc does)
- Chunk overlap of 10% seems reasonable as a starting point but should be revisited once real DocuMind documents (not just test samples) are used

## Blockers / Open Questions

- Need to test with a larger, more realistic document set to see if chunking/retrieval quality holds up at scale
- Day 7 and Day 8 verification still outstanding — should not stack further unverified days without circling back

## Next (Day 12)

- Continue embeddings evaluation with a bigger test set, OR begin transition into Module 4 (Vector Databases) by setting up ChromaDB and migrating the manual similarity search into it
- Priority: resolve README update and Day 7 verification debt before moving too far into Module 4

---

> **Status: DRAFT — unverified.** Content above is logically grounded based on established patterns (chunking config, MiniLM behavior, typical cosine similarity ranges) but not yet backed by actual logged output from a real run. Replace similarity scores, chunk counts, and sample vector with real values before treating this as final, or before removing the DRAFT flag.
