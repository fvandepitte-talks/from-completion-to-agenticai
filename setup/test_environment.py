#!/usr/bin/env python3
"""
Test script to verify the environment setup for the AI talk
"""

import sys
import importlib
from datetime import datetime

def test_import(module_name, display_name=None):
    """Test if a module can be imported"""
    if display_name is None:
        display_name = module_name
    
    try:
        importlib.import_module(module_name)
        print(f"✅ {display_name}: OK")
        return True
    except ImportError as e:
        print(f"❌ {display_name}: FAILED - {e}")
        return False

def main():
    """Run all environment tests"""
    print("🧪 Testing Environment Setup")
    print("=" * 50)
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python Version: {sys.version}")
    print("=" * 50)
    
    # Core requirements
    tests = [
        ("agno", "AGNO AI Framework"),
        ("azure.ai.inference", "Azure AI Inference"),
        ("azure.identity", "Azure Identity"),
        ("openai", "OpenAI"),
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
        ("matplotlib", "Matplotlib"),
        ("seaborn", "Seaborn"),
        ("jupyter", "Jupyter"),
        ("plotly", "Plotly"),
        ("requests", "Requests"),
        ("sentence_transformers", "Sentence Transformers"),
        ("chromadb", "ChromaDB"),
        ("sqlalchemy", "SQLAlchemy"),
        ("icalendar", "iCalendar"),
        ("dotenv", "Python-dotenv")
    ]
    
    passed = 0
    total = len(tests)
    
    print("\n🔍 Testing Package Imports:")
    print("-" * 30)
    
    for module, display in tests:
        if test_import(module, display):
            passed += 1
    
    print("-" * 30)
    print(f"📊 Results: {passed}/{total} packages imported successfully")
    
    if passed == total:
        print("\n🎉 Environment Setup Complete!")
        print("✅ All packages are ready for your AI demonstration")
        print("\n🚀 Next Steps:")
        print("1. Set up your .env file with Azure credentials")
        print("2. Launch Jupyter: jupyter lab")
        print("3. Open notebooks/01_foundation_llm_text_generation.ipynb")
        return True
    else:
        print(f"\n⚠️ {total - passed} packages failed to import")
        print("Please check the environment setup guide and try again")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)