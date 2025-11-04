# 🚀 Environment Setup Guide

## Prerequisites

- Python 3.9+ (we tested with Python 3.13.3)
- macOS, Linux, or Windows
- Terminal/Command Prompt access
- Azure account (for Azure AI Foundry integration)

## 📦 Quick Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd from-completion-to-agenticai
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
# Check AGNO AI installation
python -c "import agno; print('✅ AGNO AI installed successfully')"

# Check Azure libraries
python -c "import azure.ai.inference; print('✅ Azure AI libraries ready')"

# Check Jupyter
python -c "import jupyter; print('✅ Jupyter ready')"
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```bash
# Azure AI Foundry Configuration
AZURE_AI_FOUNDRY_ENDPOINT=your_endpoint_here
AZURE_AI_FOUNDRY_KEY=your_key_here
AZURE_AI_FOUNDRY_MODEL_NAME=your_model_name_here

# Optional: OpenAI fallback
OPENAI_API_KEY=your_openai_key_here
```

### Azure AI Foundry Setup
1. Log into [Azure AI Foundry](https://ai.azure.com)
2. Deploy your preferred model (e.g., Phi-4, GPT-4o-mini)
3. Copy the endpoint URL to your `.env` file
4. Update model name in notebooks if different from "Phi-4"

### Azure CLI Authentication
```bash
# Install Azure CLI (if not already installed)
# macOS: brew install azure-cli
# Windows: Download from Microsoft
# Linux: See Azure CLI docs

# Login to Azure
az login

# Verify login (optional)
az account show
```

## 🚦 Test Your Setup

Run this test script to verify everything works:

```bash
python setup/test_environment.py
```

## 📚 Launch Jupyter

```bash
# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

Navigate to `notebooks/` and open `01_foundation_llm_text_generation.ipynb`

## 🛠 Troubleshooting

### Common Issues

**Issue: AGNO AI import error**
```bash
# Solution: Reinstall agno
pip uninstall agno
pip install agno --no-cache-dir
```

**Issue: Azure authentication error**
```bash
# Solution: Login with Azure CLI
az login

# If still issues, check your subscription
az account list
az account set --subscription "your-subscription-id"
```

**Issue: Jupyter widgets not displaying**
```bash
# Solution: Enable widgets
jupyter nbextension enable --py widgetsnbextension
```

**Issue: ChromaDB compilation error**
```bash
# Solution: Install build tools (macOS)
xcode-select --install

# Solution: Install build tools (Linux)
sudo apt-get install build-essential
```

## 📋 Package Versions

The setup was tested with these key versions:
- agno: 2.2.6
- azure-ai-inference: 1.0.0b9
- azure-identity: 1.25.1
- jupyter: 1.1.1
- pandas: 2.3.3
- matplotlib: 3.10.7
- sentence-transformers: 5.1.2

## 🆘 Getting Help

If you encounter issues:

1. **Check Python Version**: Ensure you're using Python 3.9+
2. **Virtual Environment**: Make sure it's activated (you should see `(venv)` in your prompt)
3. **Clean Install**: Delete `venv/` folder and recreate if needed
4. **Dependencies**: Run `pip list` to verify all packages installed correctly

## 🎯 Ready to Present!

Once setup is complete, you can run all notebooks successfully for your conference management AI demonstration.

---

**Next Step**: Open `notebooks/01_foundation_llm_text_generation.ipynb` and start your AI journey!