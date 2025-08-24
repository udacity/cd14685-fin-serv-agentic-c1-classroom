# Risk Analyst Agent Tests - Top 10 Essential Tests

"""
Streamlined test suite for risk_analyst_agent.py module focusing on core functionality
"""

import pytest
import json
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Import risk analyst components - these will work once students implement them
try:
    from src.risk_analyst_agent import RiskAnalystAgent
    from src.foundation_sar import (
        RiskAnalystOutput,
        ExplainabilityLogger,
        CaseData,
        CustomerData,
        AccountData,
        TransactionData
    )
    
    # Test if RiskAnalystAgent is actually implemented (not just empty pass statements)
    try:
        # Check if RiskAnalystAgent has proper methods defined, not just an empty pass
        # If the class methods are just "pass", they won't have proper implementations
        mock_client = Mock()
        mock_logger = Mock()
        test_agent = RiskAnalystAgent(mock_client, mock_logger)
        
        # Check if the agent has the required methods and attributes with proper implementation
        # Check if system_prompt has real content (not just TODO placeholder)
        has_real_prompt = (hasattr(test_agent, 'system_prompt') and 
                          test_agent.system_prompt is not None and
                          len(str(test_agent.system_prompt)) > 50 and
                          "TODO" not in test_agent.system_prompt)
        
        # Check if analyze_case method exists and is not just a pass statement
        # Try calling it to see if it's implemented
        has_real_analyze = False
        if hasattr(test_agent, 'analyze_case') and callable(getattr(test_agent, 'analyze_case', None)):
            try:
                # A properly implemented analyze_case should raise an error or return something when called
                # An empty pass statement will just return None
                result = test_agent.analyze_case(None)
                # If it returns None for None input, it's likely just a pass statement
                has_real_analyze = result is not None
            except Exception:
                # If it raises an exception, it means there's some implementation (good!)
                has_real_analyze = True
        
        # Check if helper methods exist and are implemented
        has_extract_json = (hasattr(test_agent, '_extract_json_from_response') and
                           callable(getattr(test_agent, '_extract_json_from_response', None)))
        
        # Only consider it implemented if it has real content, not just placeholder methods
        if has_real_prompt and has_real_analyze and has_extract_json:
            RISK_ANALYST_IMPLEMENTED = True
        else:
            # Missing required implementation - just placeholder methods
            RISK_ANALYST_IMPLEMENTED = False
    except Exception as e:
        # Any error means implementation is incomplete
        RISK_ANALYST_IMPLEMENTED = False
        
except ImportError:
    # Graceful fallback when students haven't implemented yet
    RISK_ANALYST_IMPLEMENTED = False

if not RISK_ANALYST_IMPLEMENTED:
    print("⚠️  Risk Analyst Agent not yet implemented - tests will be skipped")
    print("💡 Implement the RiskAnalystAgent class in src/risk_analyst_agent.py to run these tests")

class TestRiskAnalystAgent:
    """Test RiskAnalystAgent core functionality"""
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_agent_initialization(self):
        """Test RiskAnalystAgent initializes properly"""
        mock_client = Mock()
        logger = ExplainabilityLogger("test_risk.jsonl")
        
        agent = RiskAnalystAgent(mock_client, logger, model="gpt-4")
        
        assert agent.client == mock_client
        assert agent.logger == logger
        assert agent.model == "gpt-4"
        assert agent.system_prompt is not None
        assert len(agent.system_prompt) > 100  # Should have substantial prompt
        
        # Cleanup
        if os.path.exists("test_risk.jsonl"):
            os.remove("test_risk.jsonl")
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_analyze_case_success(self):
        """Test successful case analysis with valid response"""
        # Setup mock OpenAI client
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = '''```json
{
    "classification": "Structuring",
    "confidence_score": 0.85,
    "reasoning": "Multiple transactions just under $10,000 threshold suggest structuring",
    "key_indicators": ["threshold avoidance", "repeated amounts", "cash deposits"],
    "risk_level": "High"
}
```'''
        mock_client.chat.completions.create.return_value = mock_response
        
        # Setup logger
        logger = ExplainabilityLogger("test_analyze.jsonl")
        agent = RiskAnalystAgent(mock_client, logger)
        
        # Create test case data
        customer = CustomerData(
            customer_id="CUST_TEST",
            name="Test Customer", 
            date_of_birth="1980-01-01",
            ssn_last_4="1234",
            address="123 Test St",
            customer_since="2020-01-01",
            risk_rating="Medium"
        )
        
        account = AccountData(
            account_id="ACC_TEST",
            customer_id="CUST_TEST",
            account_type="Checking",
            opening_date="2020-01-01",
            current_balance=15000.0,
            average_monthly_balance=12000.0,
            status="Active"
        )
        
        transaction = TransactionData(
            transaction_id="TXN_TEST",
            account_id="ACC_TEST",
            transaction_date="2025-01-01",
            transaction_type="Cash_Deposit",
            amount=9900.0,
            description="Cash deposit",
            method="Cash"
        )
        
        case = CaseData(
            case_id="CASE_TEST",
            customer=customer,
            accounts=[account],
            transactions=[transaction],
            case_created_at=datetime.now().isoformat(),
            data_sources={"test": "data"}
        )
        
        # Run analysis
        result = agent.analyze_case(case)
        
        # Verify result
        assert isinstance(result, RiskAnalystOutput)
        assert result.classification == "Structuring"
        assert result.confidence_score == 0.85
        assert result.risk_level == "High"
        assert len(result.key_indicators) == 3
        
        # Verify API was called
        mock_client.chat.completions.create.assert_called_once()
        
        # Verify logging
        assert len(logger.entries) == 1
        assert logger.entries[0]["success"] == True
        assert logger.entries[0]["agent_type"] == "RiskAnalyst"
        
        # Cleanup
        if os.path.exists("test_analyze.jsonl"):
            os.remove("test_analyze.jsonl")
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_analyze_case_json_error(self):
        """Test handling of invalid JSON response"""
        # Setup mock with invalid JSON
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Invalid JSON response without proper structure"
        mock_client.chat.completions.create.return_value = mock_response
        
        logger = ExplainabilityLogger("test_json_error.jsonl")
        agent = RiskAnalystAgent(mock_client, logger)
        
        # Create minimal test case
        customer = CustomerData(
            customer_id="CUST_TEST",
            name="Test Customer",
            date_of_birth="1980-01-01",
            ssn_last_4="1234", 
            address="123 Test St",
            customer_since="2020-01-01",
            risk_rating="Low"
        )
        
        case = CaseData(
            case_id="CASE_ERROR",
            customer=customer,
            accounts=[],
            transactions=[TransactionData(
                transaction_id="TXN_ERROR",
                account_id="ACC_ERROR",
                transaction_date="2025-01-01",
                transaction_type="Test",
                amount=100.0,
                description="Test transaction",
                method="Test"
            )],
            case_created_at=datetime.now().isoformat(),
            data_sources={"test": "data"}
        )
        
        # Should raise ValueError for invalid JSON
        with pytest.raises(ValueError, match="Failed to parse Risk Analyst JSON output"):
            agent.analyze_case(case)
        
        # Verify error was logged
        assert len(logger.entries) == 1
        assert logger.entries[0]["success"] == False
        assert "JSON parsing failed" in logger.entries[0]["reasoning"]
        
        # Cleanup
        if os.path.exists("test_json_error.jsonl"):
            os.remove("test_json_error.jsonl")
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_extract_json_from_code_block(self):
        """Test JSON extraction from code blocks"""
        agent = RiskAnalystAgent(Mock(), Mock())
        
        response_with_json_block = '''Here is the analysis:
```json
{
    "classification": "Fraud",
    "confidence_score": 0.9,
    "reasoning": "Clear fraud indicators",
    "key_indicators": ["suspicious_pattern"],
    "risk_level": "Critical"
}
```
That completes the analysis.'''
        
        extracted = agent._extract_json_from_response(response_with_json_block)
        parsed = json.loads(extracted)
        
        assert parsed["classification"] == "Fraud"
        assert parsed["confidence_score"] == 0.9
        assert parsed["risk_level"] == "Critical"
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_extract_json_from_plain_text(self):
        """Test JSON extraction from plain text response"""
        agent = RiskAnalystAgent(Mock(), Mock())
        
        response_plain_json = '''{"classification": "Money_Laundering", "confidence_score": 0.75, "reasoning": "Complex layering scheme", "key_indicators": ["multiple_transfers"], "risk_level": "High"}'''
        
        extracted = agent._extract_json_from_response(response_plain_json)
        parsed = json.loads(extracted)
        
        assert parsed["classification"] == "Money_Laundering"
        assert parsed["confidence_score"] == 0.75
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_extract_json_empty_response(self):
        """Test handling of empty LLM response"""
        agent = RiskAnalystAgent(Mock(), Mock())
        
        # Should raise ValueError for empty response
        with pytest.raises(ValueError, match="No JSON content found"):
            agent._extract_json_from_response("")
        
        with pytest.raises(ValueError, match="No JSON content found"):
            agent._extract_json_from_response("   ")
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_format_accounts(self):
        """Test account formatting for prompts"""
        agent = RiskAnalystAgent(Mock(), Mock())
        
        accounts = [
            AccountData(
                account_id="ACC_001",
                customer_id="CUST_001",
                account_type="Checking",
                opening_date="2020-01-01",
                current_balance=15000.50,
                average_monthly_balance=12000.75,
                status="Active"
            ),
            AccountData(
                account_id="ACC_002", 
                customer_id="CUST_001",
                account_type="Savings",
                opening_date="2020-06-01",
                current_balance=25000.00,
                average_monthly_balance=20000.00,
                status="Active"
            )
        ]
        
        formatted = agent._format_accounts(accounts)
        
        assert "ACC_001" in formatted
        assert "Checking" in formatted
        assert "$15,000.50" in formatted
        assert "ACC_002" in formatted
        assert "Savings" in formatted
        assert "$25,000.00" in formatted
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_format_transactions(self):
        """Test transaction formatting for prompts"""
        agent = RiskAnalystAgent(Mock(), Mock())
        
        transactions = [
            TransactionData(
                transaction_id="TXN_001",
                account_id="ACC_001",
                transaction_date="2025-01-01",
                transaction_type="Cash_Deposit",
                amount=9900.0,
                description="Cash deposit at branch",
                method="Cash",
                location="Branch_001"
            ),
            TransactionData(
                transaction_id="TXN_002",
                account_id="ACC_001", 
                transaction_date="2025-01-02",
                transaction_type="Wire_Transfer",
                amount=15000.0,
                description="Wire to offshore account",
                method="Wire"
            )
        ]
        
        formatted = agent._format_transactions(transactions)
        
        assert "1. 2025-01-01: Cash_Deposit $9,900.00" in formatted
        assert "2. 2025-01-02: Wire_Transfer $15,000.00" in formatted
        assert "Cash deposit at branch" in formatted
        assert "Branch_001" in formatted
        assert "Wire to offshore account" in formatted
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_system_prompt_structure(self):
        """Test system prompt contains required elements"""
        agent = RiskAnalystAgent(Mock(), Mock())
        prompt = agent.system_prompt
        
        # Check for key Chain-of-Thought elements
        assert "Chain-of-Thought" in prompt or "step-by-step" in prompt
        assert "Financial Crime" in prompt or "Risk Analyst" in prompt
        
        # Check for classification categories
        assert "Structuring" in prompt
        assert "Sanctions" in prompt
        assert "Fraud" in prompt
        assert "Money_Laundering" in prompt
        assert "Other" in prompt
        
        # Check for JSON structure requirement
        assert "JSON" in prompt
        assert "classification" in prompt
        assert "confidence_score" in prompt
        assert "reasoning" in prompt
        assert "key_indicators" in prompt
        assert "risk_level" in prompt
    
    @pytest.mark.skipif(not RISK_ANALYST_IMPLEMENTED, reason="Risk Analyst Agent not implemented yet")
    def test_api_call_parameters(self):
        """Test OpenAI API call uses correct parameters"""
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = '''{"classification": "Other", "confidence_score": 0.5, "reasoning": "Test", "key_indicators": ["test"], "risk_level": "Low"}'''
        mock_client.chat.completions.create.return_value = mock_response
        
        logger = ExplainabilityLogger("test_api.jsonl")
        agent = RiskAnalystAgent(mock_client, logger, model="gpt-3.5-turbo")
        
        # Create minimal case
        customer = CustomerData(
            customer_id="CUST_API",
            name="API Test",
            date_of_birth="1990-01-01", 
            ssn_last_4="9999",
            address="API Test Address",
            customer_since="2021-01-01",
            risk_rating="Low"
        )
        
        case = CaseData(
            case_id="CASE_API",
            customer=customer,
            accounts=[],
            transactions=[TransactionData(
                transaction_id="TXN_API",
                account_id="ACC_API",
                transaction_date="2025-01-01",
                transaction_type="Test",
                amount=1000.0,
                description="API test",
                method="Test"
            )],
            case_created_at=datetime.now().isoformat(),
            data_sources={"api": "test"}
        )
        
        agent.analyze_case(case)
        
        # Verify API call parameters
        call_args = mock_client.chat.completions.create.call_args
        assert call_args.kwargs["model"] == "gpt-3.5-turbo"
        assert call_args.kwargs["temperature"] == 0.3
        assert call_args.kwargs["max_tokens"] == 1000
        assert len(call_args.kwargs["messages"]) == 2
        assert call_args.kwargs["messages"][0]["role"] == "system"
        assert call_args.kwargs["messages"][1]["role"] == "user"
        
        # Cleanup
        if os.path.exists("test_api.jsonl"):
            os.remove("test_api.jsonl")
