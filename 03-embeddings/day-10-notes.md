# Day 10 Chunking Strategy & Embedding Model Comparison

**Module:** 03 - Embeddings
**Date:** August 14, 2026
**Project link:** DocuMind (RAG pipeline)

---

## 1. Goal for Today

Continuation from Day 9's open items:
1. Test different chunk size / overlap combinations on a sample document
2. Compare `all-MiniLM-L6-v2` vs `all-mpnet-base-v2` on the same sample

---

## 2. Chunk Size / Overlap Experiment (DRAFT theoretical)

**Setup (planned):**
- Sample document: one representative DocuMind test doc
- Chunk sizes to test: 256, 512, 1024 tokens
- Overlap to test: 0%, 10%, 20%

**Expected pattern (based on theory, not measured):**

| Chunk size | Overlap | Expected retrieval precision | Expected context completeness |
|---|---|---|---|
| 256 | 10% | Higher precision, risk of losing context | Lower |
| 512 | 10–20% | Balanced likely best default | Balanced |
| 1024 | 20% | Lower precision, more context per chunk | Higher |

**Reasoning (not yet validated):** smaller chunks should return more targeted matches but risk splitting an idea across chunks; larger chunks preserve more context per match but dilute the embedding's specificity, which could pull in irrelevant chunks during retrieval. 512 tokens with ~10–20% overlap is the commonly recommended starting point in RAG literature, so it's the working hypothesis for DocuMind's default  **needs to be confirmed empirically**.

---

## 3. Model Comparison: `all-MiniLM-L6-v2` vs `all-mpnet-base-v2` (DRAFT theoretical)

| Aspect | all-MiniLM-L6-v2 | all-mpnet-base-v2 |
|---|---|---|
| Dimension | 384 | 768 |
| Expected relative speed | Faster | Slower (~2-3x, unverified) |
| Expected relative accuracy | Good baseline | Likely better semantic nuance |
| Storage cost per chunk | Lower | Higher |

**Hypothesis (not yet tested on DocuMind data):** `all-mpnet-base-v2` should produce noticeably better similarity separation between related/unrelated chunks compared to `all-MiniLM-L6-v2`, at the cost of slower encoding and larger vector storage. Whether that trade-off is worth it for DocuMind depends on real query-quality testing no evidence yet either way.

---

## 4. Open Questions / Risks

- No real numbers exist yet for either the chunk experiment or the model comparison  everything above is a placeholder hypothesis
- Real test needs an actual DocuMind sample document with known "ground truth" relevant sections, so retrieval quality can be judged, not guessed
- Need to decide the evaluation method (manual inspection vs a small labeled query set) before running this for real

---

## Next Steps

- [ ] **Priority:** Re-run this as a real hands-on experiment with actual chunk size/overlap values and actual similarity scores  replace all theoretical tables above
- [ ] Pick or write 1 ground-truth sample doc + a few test queries with known correct chunks
- [ ] Move into Module 4: Vector Databases (ChromaDB setup) once chunking strategy is confirmed
