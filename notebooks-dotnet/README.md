# .NET Interactive Notebooks - From Completion to Agentic AI

This folder contains .NET implementations of the "From Completion to Agentic AI" demo notebooks, using Azure OpenAI SDK and Microsoft Semantic Kernel.

## 📚 Notebooks Overview

These notebooks demonstrate the same concepts as the Python notebooks but using .NET technologies:

1. **[01_chat_client.dib](01_chat_client.dib)** - Foundation & Conversational AI
   - Azure.AI.OpenAI SDK for chat completions
   - Conversation history management
   - Basic chat vs conversational context

2. **[02_rag_knowledge.dib](02_rag_knowledge.dib)** - RAG Knowledge System
   - Vector-based semantic search
   - Knowledge retrieval and context injection
   - Conference session recommendations

3. **[03_tool_calling.dib](03_tool_calling.dib)** - Function Calling
   - Azure OpenAI function calling
   - Dynamic tool invocation
   - Data enrichment with real-time information

4. **[04_agent_orchestration.dib](04_agent_orchestration.dib)** - Multi-Agent Orchestration
   - Microsoft Semantic Kernel for agent orchestration
   - Sequential and parallel agent workflows
   - Plugins and custom tools
   - Multi-agent collaboration patterns

## 🛠 Prerequisites

### Required Software
- **.NET SDK 8.0+**: [Download here](https://dotnet.microsoft.com/download)
- **Visual Studio Code**: [Download here](https://code.visualstudio.com/)
- **Polyglot Notebooks Extension**: [Install from VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.dotnet-interactive-vscode)

### Azure Services
- **Azure OpenAI Service** with a deployed model (e.g., gpt-4, gpt-4o-mini, gpt-4.1-nano)
- **Azure AI Foundry** (optional, for advanced orchestration scenarios)

## 🚀 Getting Started

### 1. Install Prerequisites

```bash
# Verify .NET installation
dotnet --version

# Should show 8.0.x or higher
```

### 2. Install Polyglot Notebooks Extension

In Visual Studio Code:
1. Open Extensions (Ctrl+Shift+X / Cmd+Shift+X)
2. Search for "Polyglot Notebooks"
3. Install the extension by Microsoft

### 3. Configure Azure Credentials

Copy the `.env.template` file from the repository root to `.env` and fill in your Azure credentials:

```bash
# From repository root
cp .env.template .env
```

Edit `.env` with your Azure OpenAI details:
```
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-nano
AZURE_OPENAI_API_VERSION=2024-12-01-preview
```

### 4. Open and Run Notebooks

1. Open VS Code in the repository folder
2. Navigate to `notebooks-dotnet/`
3. Open `01_chat_client.dib`
4. Click "Run All" or run cells individually

## 📦 NuGet Packages Used

The notebooks automatically install required packages using `#r "nuget:"` directives:

### Core Packages
- **Azure.AI.OpenAI** (2.1.0) - Azure OpenAI service client
- **Microsoft.SemanticKernel** (1.30.0) - Agent orchestration framework
- **Microsoft.SemanticKernel.Connectors.AzureOpenAI** (1.30.0) - Azure OpenAI integration
- **DotNetEnv** (3.1.1) - Environment variable management

### Additional Packages
- **System.Text.Json** (9.0.0) - JSON serialization
- **Microsoft.Extensions.VectorData** (9.0.0-preview) - Vector operations (RAG notebook)
- **Microsoft.SemanticKernel.Agents.Core** (1.30.0-alpha) - Agent framework (orchestration)

## 🔧 Troubleshooting

### Issue: Polyglot Notebooks Extension Not Working

**Solution:**
1. Ensure you have .NET SDK 8.0+ installed
2. Restart VS Code after installing the extension
3. Try creating a new .dib file to test the extension

### Issue: NuGet Package Not Found

**Solution:**
1. Check your internet connection
2. Clear NuGet cache: `dotnet nuget locals all --clear`
3. Try running the cell again

### Issue: Azure OpenAI API Errors

**Solution:**
1. Verify your `.env` file has correct credentials
2. Check that your Azure OpenAI deployment name matches `AZURE_OPENAI_DEPLOYMENT`
3. Ensure your API key has proper permissions
4. Verify the API version is supported

### Issue: "Could not load file or assembly" Errors

**Solution:**
1. Close and reopen VS Code
2. Clear the notebook kernel and restart
3. Try running cells in order from top to bottom

## 💡 Key Differences from Python Notebooks

### Advantages of .NET Implementation
- **Type Safety**: Compile-time type checking
- **Performance**: Generally faster execution
- **Native Azure Integration**: Seamless integration with Azure services
- **Enterprise Support**: Strong enterprise tooling and support

### Framework Equivalents
| Python | .NET |
|--------|------|
| AGNO AI | Microsoft Semantic Kernel |
| openai library | Azure.AI.OpenAI SDK |
| ChromaDB | Microsoft.Extensions.VectorData |
| sentence-transformers | Semantic Kernel Embeddings |

## 📖 Learning Path

Follow these notebooks in order for the best learning experience:

1. **Start with 01_chat_client.dib** to understand the basics of Azure OpenAI chat
2. **Progress to 02_rag_knowledge.dib** to add knowledge retrieval
3. **Explore 03_tool_calling.dib** to enable function calling
4. **Complete with 04_agent_orchestration.dib** for multi-agent systems

## 🔗 Additional Resources

### Documentation
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [.NET Interactive Notebooks Guide](https://github.com/dotnet/interactive/blob/main/docs/NotebookswithJupyter.md)

### Tutorials
- [Get started with Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/get-started/)
- [Azure OpenAI Quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart)

### Sample Code
- [Semantic Kernel Samples](https://github.com/microsoft/semantic-kernel/tree/main/dotnet/samples)
- [Azure OpenAI Samples](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/openai/Azure.AI.OpenAI/samples)

## 🤝 Contributing

If you find issues or have improvements for the .NET notebooks:
1. Open an issue describing the problem/enhancement
2. Submit a pull request with your changes
3. Ensure all notebooks run successfully before submitting

## 📄 License

Same as the main repository (see root README.md for details).

---

**Happy learning with .NET and Azure AI!** 🚀
