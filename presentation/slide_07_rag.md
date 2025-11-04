# Slide 07: Knowledge Enhancement with RAG

## 📚 Part 3: Retrieval-Augmented Generation (RAG)

### The Problem: LLMs Have Knowledge Cutoffs
- Training data has a specific cutoff date
- No access to private/internal documents  
- Can't know real-time information
- May "hallucinate" outdated or incorrect facts

### The Solution: RAG Architecture

```
User Query → Vector Search → Retrieve Relevant Docs → LLM + Context → Response
```

**Example:**
1. **User asks:** "What's the Wi-Fi password for the venue?"
2. **System retrieves:** Conference venue documentation
3. **LLM generates:** "The Wi-Fi network is 'TechConf2025' with password 'Innovation123'"

### Key Components:
- **Document Store** - Your knowledge base
- **Vector Embeddings** - Mathematical representation of text meaning
- **Similarity Search** - Find most relevant documents
- **Context Injection** - Add relevant info to prompt

---
**Demo:** Conference FAQ System with Real-Time Knowledge