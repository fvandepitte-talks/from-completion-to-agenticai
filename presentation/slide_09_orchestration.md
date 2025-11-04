# Slide 09: Multi-Agent Orchestration

## 🤝 Part 5: From Single Agents to Agent Teams

### The Evolution: Single → Multiple Specialized Agents

**Single Agent Limitation:**
- One agent tries to do everything
- Jack of all trades, master of none
- Complex prompts become unwieldy

**Multi-Agent Solution:**
- **Specialist agents** for specific tasks
- **Orchestrator** coordinates the workflow
- **Better results** through specialization

### Conference Planning Example:

```
User Request: "Plan a full-day AI conference for 200 people"

┌─────────────────────────────────────────────────────────────┐
│ Orchestrator Agent: Analyzes request, creates workflow      │
└─────────────────┬───────────────────────────────────────────┘
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │Content  │ │Logistics│ │Speaker  │
   │Agent    │ │Agent    │ │Agent    │
   └─────────┘ └─────────┘ └─────────┘
```

### Agent Specializations:
- **Content Agent:** Session descriptions, marketing copy
- **Logistics Agent:** Venue booking, catering, equipment  
- **Speaker Agent:** Outreach, scheduling, travel coordination
- **Orchestrator:** Workflow coordination, quality control

---
**Demo:** Complete Event Planning Pipeline