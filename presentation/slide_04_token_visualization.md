# Slide 04: Token Generation Visualization

## 🎯 Token-by-Token: "The conference will be held in..."

### Step-by-Step Generation Process

| Step | Context | Next Token Probabilities | Selected |
|------|---------|-------------------------|----------|
| 1 | "The conference will be held in" | Brussels (15%), Amsterdam (12%), London (10%)... | **Brussels** |
| 2 | "...held in Brussels" | next (8%), during (6%), from (5%)... | **during** |
| 3 | "...Brussels during" | March (12%), the (8%), 2025 (7%)... | **March** |
| 4 | "...during March" | 2025 (25%), and (5%), for (3%)... | **2025** |

### Why This Matters:
- **Probabilistic, not deterministic** - same prompt can give different results
- **Context-dependent** - each token influences the next
- **Explains "hallucination"** - model confidently predicts plausible but incorrect information
- **Temperature controls randomness** - lower = more predictable, higher = more creative

---
**Demo Time:** Conference Event Description Generator