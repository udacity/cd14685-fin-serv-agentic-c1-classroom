"""
Financial Investigation Tools for ReACT Framework

This module provides pre-defined tools for financial compliance investigations
that can be used with the ReACT (Reasoning and Acting) framework.
"""

import json
import re
from datetime import datetime, timedelta


# Tool 1: Transaction History Lookup
def get_transaction_history(account_id, days=30):
    """Retrieve transaction history for an account (simulated data)"""
    
    # TODO: Implement different transaction patterns based on account_id
    # Hint: Use if/elif statements to return different data for:
    # - "high_risk" accounts: Multiple cash deposits just under $10K
    # - "business" accounts: Large wire transfers
    # - Other accounts: Normal transactions
    
    transactions = []  # TODO: Replace with actual transaction data
    
    return {
        "account_id": account_id,
        "period_days": days,
        "transaction_count": len(transactions),
        "transactions": transactions
    }


# Tool 2: Customer Profile Lookup
def get_customer_profile(customer_id):
    """Retrieve customer profile and risk information (simulated data)"""
    
    # TODO: Create profiles dictionary with customer data
    # Include: name, occupation, income, account_age, risk_score, etc.
    profiles = {
        # TODO: Add CUST_001, CUST_002, CUST_003 profiles
    }
    
    return profiles.get(customer_id, {"error": "Customer not found"})


# Tool 3: Regulatory Threshold Check
def check_regulatory_thresholds(transaction_amount, transaction_type):
    """Check transaction against regulatory reporting thresholds"""
    
    # TODO: Define regulatory thresholds
    thresholds = {
        "CTR_threshold": 10000,  # Currency Transaction Report
        "SAR_threshold": 5000,   # Suspicious Activity Report
        "wire_threshold": 3000,  # Enhanced monitoring for wires
    }
    
    # TODO: Calculate compliance requirements
    results = {
        "amount": transaction_amount,
        "type": transaction_type,
        # TODO: Add threshold checks
    }
    
    return results


# Tool Registry
INVESTIGATION_TOOLS = {
    "get_transaction_history": get_transaction_history,
    "get_customer_profile": get_customer_profile,
    "check_regulatory_thresholds": check_regulatory_thresholds
}


# Tool Execution Functions
def parse_tool_calls(text):
    """Parse JSON tool calls from LLM response"""
    # TODO: Create regex pattern to find JSON tool calls
    json_pattern = r''  # TODO: Write regex pattern
    
    # TODO: Find matches and parse JSON
    tool_calls = []
    
    return tool_calls


def execute_tool(tool_name, parameters):
    """Execute a tool with given parameters"""
    # TODO: Check if tool exists and execute
    if tool_name not in INVESTIGATION_TOOLS:
        return {"error": f"Tool {tool_name} not found"}
    
    try:
        # TODO: Execute tool function
        result = None
        return result
    except Exception as e:
        return {"error": f"Tool execution failed: {str(e)}"}


def process_tool_calls(llm_response):
    """Process all tool calls in LLM response and return results"""
    # TODO: Parse tool calls and execute them
    # TODO: Print execution details
    # TODO: Return results
    
    results = []
    return results
