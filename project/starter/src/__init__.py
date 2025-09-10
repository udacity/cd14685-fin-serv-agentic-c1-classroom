# SAR Processing System - Source Code Package
"""
Financial Services Agentic AI Project
Suspicious Activity Report (SAR) Processing System

This package contains the core modules for building an AI-powered
SAR processing system for financial crime detection.
"""

__version__ = "1.0.0"
__author__ = "Udacity Student"

import os
from typing import Optional

def create_vocareum_openai_client():
    """
    Create an OpenAI client configured for Vocareum routing.
    
    This function handles the specific configuration required for Vocareum
    OpenAI API keys used in Udacity programs.
    
    Returns:
        openai.OpenAI: Configured OpenAI client instance
        
    Raises:
        ValueError: If OPENAI_API_KEY environment variable is not set
        ImportError: If openai package is not installed
    """
    try:
        import openai
    except ImportError:
        raise ImportError("openai package is required. Install with: pip install openai")
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable not found. "
            "Get your Vocareum OpenAI API key from 'Cloud Resources' in your Udacity workspace."
        )
    
    if not api_key.startswith('voc-'):
        print("⚠️ Warning: API key doesn't start with 'voc-'. "
              "Make sure you're using a Vocareum OpenAI API key from your Udacity workspace.")
    
    # Configure client for Vocareum routing
    client = openai.OpenAI(
        base_url="https://openai.vocareum.com/v1",
        api_key=api_key
    )
    
    print("✅ OpenAI client initialized with Vocareum routing")
    print(f"🔑 API key: {api_key[:8]}...{api_key[-4:]}")
    print("📍 Base URL: https://openai.vocareum.com/v1")
    
    return client
