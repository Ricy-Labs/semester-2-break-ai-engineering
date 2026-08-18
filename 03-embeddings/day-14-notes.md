# Day 14 Manual Semantic Search (Pre-ChromaDB)

## Objective

Before introducing ChromaDB in Module 4, implement a **manual semantic search pipeline** over a small document set using raw embeddings + cosine similarity. This continues the "mechanics before abstractions" principle established on Day 9  understanding how a vector DB works internally before letting it abstract the process away.

**Dependency note:** The embedding model used here should follow the decision from Day 12 (MiniLM vs mpnet comparison). If Day 12 is still unresolved, default to `all-MiniLM-L6-v2` for this exercise (faster iteration) and revisit once the Day 12 decision is finalized.

---

## Concept

A manual semantic search pipeline has 4 steps:

1. **Corpus prep**  take a small set of text chunks (10–20 items), reuse the `RecursiveCharacterTextSplitter` config from Day 11 (500-char chunks, 50-char overlap) if chunking is needed.
2. **Encode**  embed all chunks with the chosen sentence-transformers model → produces a matrix of shape `(n_chunks, embedding_dim)`.
3. **Query**  embed a user query with the same model → single vector.
4. **Rank**  compute cosine similarity between the query vector and every chunk vector, sort descending, return top-k.

This is essentially what ChromaDB will do internally with an ANN index — the manual version just does it with brute-force `numpy` instead of an optimized index structure.

---

## Implementation Plan (pseudocode)

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")  # pending Day 12 final decision

corpus = [...]  # 10-20 sample chunks
corpus_embeddings = model.encode(corpus)  # shape: (n, dim)

query = "..."
query_embedding = model.encode([query])[0]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

scores = [cosine_similarity(query_embedding, emb) for emb in corpus_embeddings]
top_k_idx = np.argsort(scores)[::-1][:3]
```

---

## Expected Results (placeholder — to be filled after running)

| Query | Top match (expected) | Similarity score | Notes |
|---|---|---|---|
| `[TBD]` | `[TBD]` | `[TBD]` | `[TBD]` |
| `[TBD]` | `[TBD]` | `[TBD]` | `[TBD]` |

---

## Key Learnings (placeholder)

- `[TBD — e.g. brute-force cosine similarity is O(n), fine for small corpus but won't scale — this is exactly the gap ChromaDB fills]`
- `[TBD — any surprising ranking behavior observed]`

---

## Outstanding

- [ ] Run actual implementation with real corpus + queries
- [ ] Fill in real similarity scores and observations above
- [ ] Remove DRAFT flag once verified
- [ ] Cross-check embedding model choice against finalized Day 12 decision
- [ ] Commit: `git add 03-embeddings/day-14-notes.md`

---

## Next

Module 4 (Vector Databases / ChromaDB) — replace this manual brute-force step with ChromaDB's indexed similarity search, and compare behavior/performance against this manual baseline.
