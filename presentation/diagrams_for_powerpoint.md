# Visual Diagrams for PowerPoint Creation

## Slide 03: LLM Token Generation Flow

### Main Flow Diagram
Create a vertical flowchart with these elements:

```
┌─────────────────────────────────────────┐
│          INPUT PROMPT                   │
│    "The conference will be held in"     │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│           TOKENIZATION                  │
│  ["The", "conference", "will", "be",    │
│         "held", "in"]                   │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│        CONTEXT ANALYSIS                 │
│   🧠 Neural networks analyze all        │
│      previous tokens for meaning        │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│      PROBABILITY CALCULATION            │
│   Brussels: 15%  🏙️                    │
│   Amsterdam: 12% 🏙️                    │
│   London: 10%    🏙️                    │
│   Paris: 8%      🏙️                    │
│   Berlin: 6%     🏙️                    │
│   Other: 49%     ...                   │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│         TOKEN SELECTION                 │
│    🎲 Temperature influences choice     │
│         Selected: "Brussels"            │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│        UPDATE CONTEXT                   │
│  "The conference will be held in        │
│            Brussels"                    │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│            REPEAT CYCLE                 │
│   Continue until [STOP] token or        │
│        max_tokens reached               │
└─────────────────────────────────────────┘
```

### Visual Design Tips for PowerPoint:

1. **Colors:**
   - Input: Light blue background
   - Processing steps: Gradient from blue to green
   - Probabilities: Bar chart with different colors
   - Output: Green background

2. **Icons:**
   - 🧠 for neural processing
   - 🎲 for randomness/temperature
   - 🏙️ for city names
   - ⚡ for speed/processing
   - 🔄 for the repeat cycle

3. **Animations:**
   - Flow top to bottom with appear animations
   - Probability bars animate in with fly-in effects
   - Token selection highlights the chosen option
   - Repeat arrow pulses to show continuous cycle

4. **Side Panel (Optional):**
   Add a side panel showing:
   - Current temperature setting (slider)
   - Token count: 6/100
   - Processing time: ~0.1s per token

## Slide 04: Token Probabilities Visualization

### Horizontal Bar Chart
```
Next Token Probabilities:
Brussels    ████████████████████ 15%
Amsterdam   ███████████████      12%
London      ██████████████       10%
Paris       ███████████          8%
Berlin      ████████             6%
Madrid      ██████               5%
Rome        █████                4%
Vienna      ████                 3%
Other       ████████████████████████████████████████ 37%
```

### Temperature Effect Visualization
Show three scenarios side by side:

**Temperature = 0.1 (Conservative)**
```
Brussels    ████████████████████████████████████ 85%
Amsterdam   ████ 10%
London      ██ 5%
```

**Temperature = 0.7 (Balanced)**
```
Brussels    ████████████████████ 15%
Amsterdam   ███████████████      12%
London      ██████████████       10%
Paris       ███████████          8%
Other       ██████████████████████████████████ 55%
```

**Temperature = 1.5 (Creative)**
```
Brussels    ████████ 8%
Amsterdam   ███████ 7%
London      ███████ 7%
Paris       ██████ 6%
Berlin      ██████ 6%
Rome        █████ 5%
Tokyo       █████ 5%
Sydney      ████ 4%
Other       ███████████████████████████████ 52%
```

### Design Notes:
- Use animated horizontal bars
- Show temperature slider changing
- Highlight how distribution changes
- Use consistent colors for same cities across scenarios