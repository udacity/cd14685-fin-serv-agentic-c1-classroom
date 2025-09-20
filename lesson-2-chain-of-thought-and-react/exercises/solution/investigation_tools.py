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
    
    # Simulate different transaction patterns based on account_id
    if "high_risk" in account_id.lower():
        transactions = [
            {"date": "2025-09-15", "amount": 9800, "type": "cash_deposit", "location": "Branch_A"},
            {"date": "2025-09-14", "amount": 9750, "type": "cash_deposit", "location": "Branch_B"},
            {"date": "2025-09-13", "amount": 9900, "type": "cash_deposit", "location": "Branch_C"},
            {"date": "2025-09-12", "amount": 9850, "type": "cash_deposit", "location": "Branch_A"},
            {"date": "2025-09-11", "amount": 9600, "type": "cash_deposit", "location": "Branch_D"}
        ]
    elif "business" in account_id.lower():
        transactions = [
            {"date": "2025-09-15", "amount": 250000, "type": "wire_transfer", "location": "Singapore_Bank"},
            {"date": "2025-09-15", "amount": -240000, "type": "wire_transfer", "location": "Internal_Transfer"},
            {"date": "2025-09-10", "amount": 275000, "type": "wire_transfer", "location": "Singapore_Bank"},
            {"date": "2025-09-10", "amount": -260000, "type": "wire_transfer", "location": "Internal_Transfer"}
        ]
    else:
        transactions = [
            {"date": "2025-09-15", "amount": 2500, "type": "payroll_deposit", "location": "ACH"},
            {"date": "2025-09-12", "amount": -1200, "type": "rent_payment", "location": "Online"},
            {"date": "2025-09-10", "amount": -350, "type": "grocery", "location": "POS"}
        ]
    
    return {
        "account_id": account_id,
        "period_days": days,
        "transaction_count": len(transactions),
        "transactions": transactions
    }


# Tool 2: Customer Profile Lookup
def get_customer_profile(customer_id):
    """Retrieve customer profile and risk information (simulated data)"""
    
    profiles = {
        "CUST_001": {
            "name": "Maria Santos",
            "occupation": "Restaurant Manager",
            "annual_income": 54000,
            "account_age_years": 3,
            "previous_sars": 0,
            "risk_score": 6.2,
            "address": "Local Resident"
        },
        "CUST_002": {
            "name": "Robert Chen",
            "occupation": "Business Owner",
            "annual_income": 200000,
            "account_age_years": 0.5,
            "previous_sars": 0,
            "risk_score": 8.7,
            "address": "Multiple Jurisdictions"
        },
        "CUST_003": {
            "name": "Sarah Johnson",
            "occupation": "Software Engineer",
            "annual_income": 85000,
            "account_age_years": 5,
            "previous_sars": 0,
            "risk_score": 2.1,
            "address": "Local Resident"
        }
    }
    
    return profiles.get(customer_id, {"error": "Customer not found"})


# Tool 3: Regulatory Threshold Check
def check_regulatory_thresholds(transaction_amount, transaction_type):
    """Check transaction against regulatory reporting thresholds"""
    
    thresholds = {
        "CTR_threshold": 10000,  # Currency Transaction Report
        "SAR_threshold": 5000,   # Suspicious Activity Report (if suspicious)
        "wire_threshold": 3000,  # Enhanced monitoring for wires
    }
    
    results = {
        "amount": transaction_amount,
        "type": transaction_type,
        "ctr_required": transaction_amount >= thresholds["CTR_threshold"],
        "below_ctr_threshold": 8000 <= transaction_amount < thresholds["CTR_threshold"],
        "wire_monitoring": transaction_type == "wire_transfer" and transaction_amount >= thresholds["wire_threshold"],
        "potential_structuring": transaction_amount >= 8000 and transaction_amount < thresholds["CTR_threshold"]
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
    json_pattern = r'```json\s*({.*?})\s*```'
    matches = re.findall(json_pattern, text, re.DOTALL)
    
    tool_calls = []
    for match in matches:
        try:
            tool_call = json.loads(match)
            if "tool" in tool_call and "parameters" in tool_call:
                tool_calls.append(tool_call)
        except json.JSONDecodeError:
            continue
    
    return tool_calls


def execute_tool(tool_name, parameters):
    """Execute a tool with given parameters"""
    if tool_name not in INVESTIGATION_TOOLS:
        return {"error": f"Tool {tool_name} not found"}
    
    try:
        tool_function = INVESTIGATION_TOOLS[tool_name]
        result = tool_function(**parameters)
        return result
    except Exception as e:
        return {"error": f"Tool execution failed: {str(e)}"}


def process_tool_calls(llm_response):
    """Process all tool calls in LLM response and return results"""
    tool_calls = parse_tool_calls(llm_response)
    results = []
    
    for tool_call in tool_calls:
        tool_name = tool_call["tool"]
        parameters = tool_call["parameters"]
        
        print(f"🔧 Executing: {tool_name}")
        print(f"📝 Parameters: {parameters}")
        
        result = execute_tool(tool_name, parameters)
        results.append({
            "tool": tool_name,
            "parameters": parameters,
            "result": result
        })
        
        print(f"✅ Result: {json.dumps(result, indent=2)}")
        print("-" * 40)
    
    return results
