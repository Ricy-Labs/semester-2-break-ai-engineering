# Day 12  Embedding Model Comparison

## Goal

Compare two sentence-transformers models `all-MiniLM-L6-v2` (used in Day 11) and `all-mpnet-base-v2` on the same document/query set from Day 11, to decide which one should be the default embedding model for **DocuMind**.

## Why compare

Day 11 used `all-MiniLM-L6-v2` for the manual cosine similarity pipeline without testing alternatives. Before moving into Module 4 (Vector Databases), it makes sense to check whether a heavier model gives meaningfully better retrieval quality, since ChromaDB will be built on top of whatever model is chosen here.

## Models compared

| Model | Embedding dim | Relative size | Known trade-off |
|---|---|---|---|
| `all-MiniLM-L6-v2` | 384 | Small, fast | Lower semantic resolution, good enough for most short-query retrieval |
| `all-mpnet-base-v2` | 768 | ~3x larger, slower | Generally stronger semantic quality, higher compute/storage cost |

## Setup

- Same document set and queries as Day 11 (kept identical for apples-to-apples comparison)
- Both models loaded via `sentence-transformers`
- Metric: cosine similarity (manual, same function as Day 11 no vector DB yet)

```python
from sentence_transformers import SentenceTransformer
import time

model_a = SentenceTransformer("all-MiniLM-L6-v2")
model_b = SentenceTransformer("all-mpnet-base-v2")

# encode same corpus + query with both models
# record: encoding time, output shape, cosine similarity scores
```

## Results (placeholder — pending real run)

| Metric | MiniLM-L6-v2 | mpnet-base-v2 |
|---|---|---|
| Embedding dimension | 384 | 768 |
| Encoding time (corpus) | faster (baseline) | ~2-3x slower (estimate) |
| Top-1 similarity score (sample query) | TBD | TBD |
| Qualitative relevance of top match | TBD | TBD |

## Analysis (placeholder reasoning)

- If `mpnet` doesn't show a **clear, consistent** improvement in top-match relevance over `MiniLM`, the extra compute/storage cost (2x dimension, slower encoding) isn't justified for DocuMind's use case.
- `MiniLM` is likely to remain the default unless real results show mpnet meaningfully changes which documents get retrieved as top match not just a marginal score difference.
- This decision matters because Module 4 (ChromaDB) will store whatever embeddings are chosen here at scale; switching later means re-embedding the whole corpus.

## Decision (pending real results)

Default for DocuMind: **TBD after real run**  leaning toward keeping `all-MiniLM-L6-v2` unless mpnet shows clear qualitative gains.

## Next steps

- [ ] Run actual encoding + similarity comparison, replace placeholder numbers
- [ ] Confirm final model decision with real qualitative check (not just cosine score)
- [ ] Remove DRAFT flag once real results are in
- [ ] Proceed to Module 4: Vector Databases (ChromaDB)
