# AI Coding Agent Instructions

## Project Overview
This is a technical talk repository demonstrating the evolution from simple LLM completion to sophisticated multi-agent AI systems, using conference management as the practical domain. The project uses **AGNO AI framework with Azure AI Foundry** for orchestration.

The demos will all be in context of managing conferences/events, showcasing real-world applications like session planning, speaker management, attendee support, logistics coordination, and analytics.

## Architecture & Key Components

### Technology Stack
- **AI Framework**: AGNO AI (v2.0+) for multi-agent orchestration
- **Azure Services**: Azure AI Foundry + Azure OpenAI Service
- **Core Libraries**: sentence-transformers, chromadb (RAG), sqlalchemy, icalendar
- **Notebooks**: Jupyter-based demonstrations in progressive complexity

### Project Structure
```
notebooks/          # Progressive demo notebooks (Foundation → Orchestration)
setup/             # Environment setup and testing utilities
.env.template      # Azure credential configuration template
requirements.txt   # Comprehensive dependency list with Azure best practices
```

## Development Workflows

### Environment Setup (Critical First Step)
```bash
# Always use the venv (pre-created)
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Test environment before coding
python setup/test_environment.py
```

### Azure Configuration Requirements
1. Copy `.env.template` to `.env` with real credentials
2. **Azure OpenAI**: Required for Foundation demos (gpt-4.1-nano deployment)
3. **Azure AI Foundry**: Required for AGNO AI orchestration demos (Phi-4 model)
4. Fallback OpenAI API key for offline demos

### Demo Notebook Pattern
Each notebook follows this progression:
1. **Foundation** → Basic completion (Azure OpenAI direct)
2. **Conversation** → Chat interface with memory
3. **Knowledge** → RAG with ChromaDB + sentence-transformers
4. **Tools** → Function calling for actions
5. **Orchestration** → Multi-agent workflows via AGNO AI

## Project-Specific Conventions

### Conference Management Domain
- **Use Case**: All demos center on conference/event management scenarios
- **Data Examples**: Sessions, speakers, attendees, venues, schedules
- **Business Metrics**: Include realistic impact numbers (75% time reduction, etc.)

### Azure Integration Patterns
- Use `azure-identity` for authentication (not hardcoded keys)
- Environment variables for all Azure endpoints and model names
- Follow Azure OpenAI API version patterns (`2024-12-01-preview`)
- Separate Azure OpenAI (foundation) from Azure AI Foundry (orchestration)

### Notebook Development Standards
- **10-minute segments**: Each demo should run in ~10 minutes
- **Progressive complexity**: Build concepts incrementally
- **Error handling**: Include fallback outputs for API failures
- **Visual outputs**: Use plotly/matplotlib for engagement

## Key Integration Points

### AGNO AI Framework Integration
- Import pattern: `import agno`
- Configuration via environment variables (AZURE_AI_FOUNDRY_*)
- Multi-agent definition and orchestration patterns
- Integration with Azure AI Foundry project endpoints

### Azure AI Services Chain
```
Azure Identity → Azure OpenAI (Foundation) → Azure AI Foundry (AGNO) → Multi-Agent Orchestration
```

### RAG Implementation Stack
- **Embeddings**: sentence-transformers for vector generation
- **Vector DB**: chromadb for similarity search
- **Documents**: Conference-specific knowledge base
- **Retrieval**: Context injection into prompts

## Critical Files & Patterns

### Environment Testing (`setup/test_environment.py`)
- Validates all dependencies before demos
- Tests Azure connectivity and authentication
- Provides clear success/failure feedback with next steps

### Configuration Template (`.env.template`)
- Pre-configured with specific Azure endpoints
- Model deployment names (gpt-4.1-nano, Phi-4)
- Demo data variables for consistency

### Requirements Management (`requirements.txt`)
- Azure-optimized versions with compatibility notes
- Comprehensive stack for all 5 demo stages
- Version pinning for reproducible demos

## Demo Execution Notes

### Talk Structure (50 minutes + Q&A)
- **5 demos × 10 minutes each**: Foundation → Conversation → Knowledge → Tools → Orchestration
- **Conference theme**: Maintains audience engagement and practical relevance
- **Live coding**: Notebooks designed for live execution or pre-run with explanations

### Troubleshooting Patterns
- **Backup outputs**: Pre-generated results for network failures
- **Environment validation**: Always run `test_environment.py` first
- **Azure fallbacks**: OpenAI API key as backup for Azure issues
- **Clean installs**: `venv/` deletion and recreation for dependency conflicts

## When Working on This Codebase

1. **Start with environment test**: Run `python setup/test_environment.py`
2. **Follow the progression**: Understand Foundation → Orchestration evolution
3. **Test Azure connectivity**: Verify `.env` configuration before notebook development
4. **Maintain demo timing**: Keep notebook execution under 10 minutes per demo
5. **Use conference examples**: All code should relate to event management scenarios
6. **Include error handling**: Demos must be robust for live presentation