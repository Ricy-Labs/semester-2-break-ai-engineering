# Day 9  Embeddings Fundamentals

**Module:** 03 - Embeddings
**Date:** [fill in today's date]
**Project link:** DocuMind (RAG pipeline)

---

## 1. What is an Embedding

An embedding is a numeric vector representation of text (or other data) in a high-dimensional space, where semantic meaning is encoded as position and distance.

Two pieces of text with similar meaning end up close together in vector space, even if they share no exact words. This is the core reason embeddings matter for retrieval: keyword search matches strings, embedding search matches meaning.

**Example logic:**
- "How do I reset my password?" and "I forgot my login credentials" → close vectors (same intent, different words)
- "How do I reset my password?" and "What's the weather today?" → distant vectors (unrelated intent)

This distinction is why embeddings are the right layer for the retrieval step in RAG, and why generation (LLM) and retrieval (embedding model) are two separate concerns in the pipeline  they solve different problems and use different models.

---

## 2. sentence-transformers (DocuMind stack)

`sentence-transformers` is the library used in DocuMind to generate embeddings locally, since Groq (the LLM provider for this project) does not expose an embedding endpoint  embedding generation and text generation are handled by different, specialized models.

**Key models compared:**

| Model | Dimension | Speed | Use case |
|---|---|---|---|
| all-MiniLM-L6-v2 | 384 | Fast | Good default for prototyping, lower resource cost |
| all-mpnet-base-v2 | 768 | Slower | Higher accuracy, better for production retrieval quality |

**Trade-off logic:** higher dimension generally captures more semantic nuance but costs more compute and storage per vector. For an early-stage project like DocuMind, starting with `all-MiniLM-L6-v2` is the reasonable default  it's cheap enough to iterate quickly, and can be swapped for `all-mpnet-base-v2` later if retrieval quality becomes the bottleneck.

---

## 3. Hands-on: Generating and Comparing Embeddings

Basic workflow tested:

1. Load a sentence-transformers model (`all-MiniLM-L6-v2`)
2. Encode a small set of sample sentences into vectors
3. Compute cosine similarity between vector pairs

**Cosine similarity** measures the angle between two vectors rather than their magnitude  this matters because it means embedding comparison is about *direction* (semantic meaning) not *length* (how much text there is).

**Observed pattern:**
- Semantically related sentences → similarity scores clustering high (roughly 0.6–0.9 range)
- Unrelated sentences → similarity scores dropping much lower (roughly below 0.3)

This confirms the core assumption RAG depends on: semantic closeness in vector space is a usable proxy for "these two texts are talking about the same thing."

---

## 4. Chunking — Why It Matters Before Embedding

A full document usually can't (and shouldn't) be embedded as a single vector:

- **Context dilution**  a long document covers many topics; one embedding vector can't represent all of them well
- **Retrieval precision**  if a user asks about one specific paragraph, retrieving the whole document as a single unit returns too much irrelevant context
- **Model limits**  embedding models have a max input length; long documents may get truncated silently if not chunked

**Chunking strategy notes:**
- Split documents into smaller segments (e.g., paragraphs or fixed token windows)
- Use overlap between chunks so context isn't lost at chunk boundaries (a sentence split across two chunks would lose meaning without overlap)
- Each chunk gets its own embedding vector, stored individually

This is the direct bridge into Module 4 (Vector Databases), where these chunk-level vectors need to be stored and searched efficiently.

---

## 5. Connection to DocuMind Architecture

Today's topic maps directly onto the retrieval half of DocuMind's RAG pipeline:

```
Document upload
      ↓
Chunking (split into smaller segments, with overlap)
      ↓
Embedding (sentence-transformers → vector per chunk)
      ↓
Store in ChromaDB (Module 4)
      ↓
User query → embedded with the same model
      ↓
Similarity search against stored chunks
      ↓
Top-matching chunks → passed to Groq (LLaMA 3.3 70B) as context
      ↓
Generated answer
```

The key insight: the query and the documents must be embedded with the **same model**, otherwise their vectors live in incompatible spaces and similarity comparison becomes meaningless.

---

## Next Steps (Module 3 continued / Module 4 preview)

- [ ] Experiment with chunk size / overlap values on a real sample document
- [ ] Compare `all-MiniLM-L6-v2` vs `all-mpnet-base-v2` on the same DocuMind sample docs
- [ ] Move into Module 4: Vector Databases (ChromaDB setup for DocuMind)
