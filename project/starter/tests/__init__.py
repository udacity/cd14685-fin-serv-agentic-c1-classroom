# SAR Processing System - Test Package
"""
Unit tests for the SAR processing system components.

Run tests with: python -m pytest tests/

Note: Tests use mock OpenAI API responses to avoid consuming actual API quota.
Tests are configured to work with Vocareum OpenAI API routing.
"""

import os
import pytest
from unittest.mock import Mock, patch
from typing import Dict, Any


def create_mock_openai_client():
    """
    Create a mock OpenAI client for testing.
    
    This function creates a mock client that simulates Vocareum OpenAI API
    responses without making actual API calls.
    
    Returns:
        Mock: Mock OpenAI client for testing
    """
    mock_client = Mock()
    
    # Mock chat completions response
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message = Mock()
    mock_response.choices[0].message.content = "Mock AI response for testing"
    
    mock_client.chat.completions.create.return_value = mock_response
    
    return mock_client


def setup_test_environment():
    """
    Set up test environment with mock configurations.
    
    This function sets up environment variables and mocks required for testing
    the SAR processing system without actual API calls.
    """
    # Set up mock API key for testing
    os.environ['OPENAI_API_KEY'] = 'voc-test-api-key-for-unit-tests-only'


@pytest.fixture
def mock_vocareum_client():
    """
    Pytest fixture providing a mock Vocareum OpenAI client.
    
    Returns:
        Mock: Configured mock client for testing
    """
    setup_test_environment()
    return create_mock_openai_client()
