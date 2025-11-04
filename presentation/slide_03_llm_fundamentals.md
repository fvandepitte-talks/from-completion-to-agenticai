# Slide 03: The Foundation - How LLMs Work

## 🧠 Part 1: Understanding Language Model Fundamentals

### The Core Process: Token-by-Token Generation

```
Input: "The conference will be held in"
         ↓
    [Tokenization]
         ↓
   ["The", "conference", "will", "be", "held", "in"]
         ↓
  [Context Analysis] → Build understanding from all previous tokens
         ↓
 [Probability Calc] → Brussels: 15%, Amsterdam: 12%, London: 10%...
         ↓
   [Token Selection] → Choose "Brussels" (with temperature influence)
         ↓
  [Add to Context] → "The conference will be held in Brussels"
         ↓
      [Repeat] → Continue until completion or max tokens
```

### Step-by-Step Breakdown:

1. **Tokenization** 
   - Break text into smaller pieces (words, parts of words)
   - "Hello world" → ["Hello", " world"]

2. **Context Understanding**
   - Model reads all previous tokens
   - Builds understanding of what comes next

3. **Probability Calculation**
   - For every possible next token
   - Based on patterns learned from training data

4. **Selection & Repeat**
   - Choose most likely token (with some randomness)
   - Add to context and repeat until done

### 🎛️ Controlling Randomness: Temperature & Top-p

#### Temperature (0.0 to 2.0+)
Controls how "creative" vs "predictable" the model is:

```
PROBABILITY DISTRIBUTION for next token:
Brussels: 15%  Amsterdam: 12%  London: 10%  Paris: 8%  Berlin: 6%...

Temperature = 0.0 (Deterministic)
└─ Always picks "Brussels" (highest probability)

Temperature = 0.7 (Balanced) 
└─ Brussels: 22%  Amsterdam: 18%  London: 15%...
   (Probabilities become more spread out)

Temperature = 1.5 (Creative)
└─ Brussels: 18%  Amsterdam: 17%  London: 16%  Paris: 15%...
   (Much more random, creative responses)
```

#### Top-p / Nucleus Sampling (0.0 to 1.0)
Only considers tokens that make up the top X% of probability:

```
Original probabilities: Brussels(15%), Amsterdam(12%), London(10%), Paris(8%)...

Top-p = 0.3 (30%)
└─ Only considers: Brussels(15%) + Amsterdam(12%) = 27%
   (Focuses on most likely options)

Top-p = 0.9 (90%) 
└─ Considers: Brussels + Amsterdam + London + Paris + Berlin + Madrid...
   (Includes more creative options)
```

#### Real-World Usage:
- **Customer Support Bot**: Temperature=0.1, Top-p=0.5 (consistent, reliable)
- **Creative Writing**: Temperature=0.8, Top-p=0.9 (varied, interesting)  
- **Code Generation**: Temperature=0.2, Top-p=0.6 (mostly correct, slight variety)

---
**Key Insight:** LLMs don't "think" - they predict the next most likely word based on patterns!