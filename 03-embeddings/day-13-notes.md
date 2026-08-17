# Day 13 Semantic Search Evaluation (Stress Testing Manual Cosine Similarity)

**Module:** 3  Embeddings
**Project:** DocuMind
**Date:** Day 13

## Objective

Extend the Day 11 manual cosine similarity search by testing it against harder query types  ambiguous phrasing, paraphrases, and edge cases  to identify where a naive manual similarity search starts to break down. The goal is not just "does it work," but "where and why does it fail," since that failure point is the concrete justification for introducing a vector database in Module 4.

## Background

Day 11 established the baseline: generate embeddings with `all-MiniLM-L6-v2`, compute cosine similarity manually (no ChromaDB), and do qualitative evaluation on straightforward queries. That baseline worked reasonably well for queries closely matching document vocabulary. Day 13 pushes on that assumption.

## Test Query Categories

Three categories designed to probe different weaknesses:

1. **Paraphrased queries**  same intent, different wording than the source document (tests whether the embedding model captures meaning vs. surface lexical overlap)
2. **Ambiguous queries**  short or vague queries that could plausibly match multiple unrelated chunks (tests precision / top-k relevance)
3. **Edge case queries**  queries using domain-specific terms not well represented in general-purpose embedding training data, or queries that combine two unrelated concepts from the document

## Methodology

- Reuse the same document corpus and embeddings from Day 11
- For each category, write 3–5 test queries
- Run manual cosine similarity, record top-3 matches and their scores
- Manually label whether each top match is actually relevant (qualitative judgment)
- Compare behavior across categories to surface patterns

## Results (placeholder — pending real run)

| Query Type | Example Query | Top Match Relevant? | Similarity Score | Notes |
|---|---|---|---|---|
| Paraphrased | *(TBD)* | *(TBD)* | *(TBD)* | *(TBD)* |
| Ambiguous | *(TBD)* | *(TBD)* | *(TBD)* | *(TBD)* |
| Edge case | *(TBD)* | *(TBD)* | *(TBD)* | *(TBD)* |

## Expected Observations (hypothesis, to be confirmed)

- Paraphrased queries should still perform reasonably well, since `all-MiniLM-L6-v2` is trained for semantic similarity rather than keyword matching.
- Ambiguous queries are expected to show smaller score gaps between the top-1 and top-2 matches — a sign the model is uncertain, which manual top-k selection can't account for (no re-ranking, no metadata filtering).
- Edge case / domain-specific queries are expected to perform worst, since general-purpose embedding models weren't trained on domain-specific corpora — this is a likely candidate for later fine-tuning or hybrid search discussion.
- Manual cosine similarity has no mechanism for filtering, indexing, or approximate nearest neighbor search — at small scale this doesn't matter, but the exercise should make clear why it won't scale.

## Key Takeaway (why this matters for Module 4)

This evaluation exists to build intuition, not just to log numbers. The specific failure modes observed here (ambiguous score gaps, weak domain-term matches, no filtering mechanism) are exactly the problems ChromaDB is introduced to address in Module 4 — via indexing, metadata filtering, and more efficient similarity search at scale. Understanding the manual limitation first should make the value of the abstraction concrete instead of assumed.

## Next Steps

- Run the actual experiment and replace placeholder results
- Day 14 candidate: embedding model comparison (`all-MiniLM-L6-v2` vs `all-mpnet-base-v2`) using this same query set as a shared benchmark
- Carry failure patterns observed here into Module 4 planning
