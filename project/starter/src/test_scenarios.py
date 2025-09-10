# Pre-built Test Scenarios for Agent Development
"""
This module provides comprehensive test scenarios for both Risk Analyst and Compliance Officer agents.
Students can import these scenarios to validate their agent implementations without having to 
write complex test cases themselves.

Usage:
    from test_scenarios import RiskAnalystScenarios, ComplianceOfficerScenarios
    
    # Run risk analyst scenarios
    scenarios = RiskAnalystScenarios()
    results = scenarios.run_all_scenarios(your_risk_agent)
    
    # Run compliance officer scenarios  
    compliance_scenarios = ComplianceOfficerScenarios()
    results = compliance_scenarios.run_all_scenarios(your_compliance_agent)
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import random

# Import foundation components (will work after students implement them)
try:
    from foundation_sar import (
        CustomerData, AccountData, TransactionData, CaseData,
        RiskAnalystOutput, ComplianceOfficerOutput, ExplainabilityLogger
    )
    FOUNDATION_AVAILABLE = True
except ImportError:
    FOUNDATION_AVAILABLE = False
    print("ℹ️ Foundation components not yet implemented. Test scenarios ready when you complete foundation_sar.py")


class RiskAnalystScenarios:
    """
    Comprehensive test scenarios for Risk Analyst Agent validation.
    
    This class provides pre-built test cases covering all suspicious activity types
    and edge cases that students' agents should handle correctly.
    """
    
    def __init__(self):
        self.scenarios = self._create_test_scenarios()
        
    def _create_test_scenarios(self) -> Dict[str, Dict[str, Any]]:
        """Create comprehensive test scenarios for risk analysis"""
        
        scenarios = {
            "structuring_classic": {
                "name": "Classic Structuring Pattern",
                "description": "Multiple cash deposits just under $10K threshold",
                "expected_classification": "Structuring",
                "expected_risk_level": "High",
                "min_confidence": 0.8,
                "customer_data": {
                    "customer_id": "CUST_STRUCT_001",
                    "name": "Sarah Thompson",
                    "date_of_birth": "1985-03-15",
                    "ssn_last_4": "4567",
                    "address": "456 Oak Avenue, Springfield, IL 62701",
                    "customer_since": "2018-06-01",
                    "risk_rating": "Medium"
                },
                "account_data": {
                    "account_id": "ACC_CHK_4567",
                    "customer_id": "CUST_STRUCT_001",
                    "account_type": "Checking",
                    "opening_date": "2018-06-01",
                    "current_balance": 45000.0,
                    "average_monthly_balance": 35000.0,
                    "status": "Active"
                },
                "transactions": [
                    {
                        "transaction_id": "TXN_STRUCT_001",
                        "account_id": "ACC_CHK_4567",
                        "amount": 9800.0,
                        "transaction_type": "Cash_Deposit",
                        "date": "2024-01-15",
                        "description": "Cash deposit",
                        "counterparty": None,
                        "location": "Springfield Branch"
                    },
                    {
                        "transaction_id": "TXN_STRUCT_002", 
                        "account_id": "ACC_CHK_4567",
                        "amount": 9500.0,
                        "transaction_type": "Cash_Deposit",
                        "date": "2024-01-16",
                        "description": "Cash deposit",
                        "counterparty": None,
                        "location": "Downtown Branch"
                    },
                    {
                        "transaction_id": "TXN_STRUCT_003",
                        "account_id": "ACC_CHK_4567", 
                        "amount": 9900.0,
                        "transaction_type": "Cash_Deposit",
                        "date": "2024-01-17",
                        "description": "Cash deposit",
                        "counterparty": None,
                        "location": "Springfield Branch"
                    }
                ],
                "key_indicators": ["threshold avoidance", "repeated cash deposits", "multiple locations"]
            },
            
            "money_laundering_complex": {
                "name": "Complex Money Laundering Pattern",
                "description": "Large wire transfers to high-risk jurisdictions with layered transactions",
                "expected_classification": "Money_Laundering",
                "expected_risk_level": "Critical",
                "min_confidence": 0.85,
                "customer_data": {
                    "customer_id": "CUST_ML_001",
                    "name": "International Trading Corp",
                    "date_of_birth": "1975-12-01",
                    "ssn_last_4": "9876",
                    "address": "789 Business Plaza, Miami, FL 33101",
                    "customer_since": "2019-03-15",
                    "risk_rating": "High"
                },
                "account_data": {
                    "account_id": "ACC_BUS_9876",
                    "customer_id": "CUST_ML_001",
                    "account_type": "Business",
                    "opening_date": "2019-03-15",
                    "current_balance": 125000.0,
                    "average_monthly_balance": 200000.0,
                    "status": "Active"
                },
                "transactions": [
                    {
                        "transaction_id": "TXN_ML_001",
                        "account_id": "ACC_BUS_9876",
                        "amount": 250000.0,
                        "transaction_type": "Wire_Transfer",
                        "date": "2024-01-10",
                        "description": "International wire transfer",
                        "counterparty": "Offshore Finance Ltd",
                        "location": "Cayman Islands"
                    },
                    {
                        "transaction_id": "TXN_ML_002",
                        "account_id": "ACC_BUS_9876",
                        "amount": 180000.0,
                        "transaction_type": "Wire_Transfer",
                        "date": "2024-01-12",
                        "description": "Business payment",
                        "counterparty": "Global Investments SA",
                        "location": "Switzerland"
                    },
                    {
                        "transaction_id": "TXN_ML_003",
                        "account_id": "ACC_BUS_9876",
                        "amount": 320000.0,
                        "transaction_type": "Wire_Transfer",
                        "date": "2024-01-15",
                        "description": "Investment transfer",
                        "counterparty": "Pacific Holdings",
                        "location": "Hong Kong"
                    }
                ],
                "key_indicators": ["high-risk jurisdictions", "large amounts", "rapid succession", "shell companies"]
            },
            
            "fraud_identity": {
                "name": "Identity Fraud Pattern",
                "description": "Rapid account activity inconsistent with customer profile",
                "expected_classification": "Fraud",
                "expected_risk_level": "High",
                "min_confidence": 0.75,
                "customer_data": {
                    "customer_id": "CUST_FRAUD_001",
                    "name": "Elderly Customer",
                    "date_of_birth": "1945-08-20",
                    "ssn_last_4": "2468",
                    "address": "123 Retirement Village, Tampa, FL 33601",
                    "customer_since": "2010-02-01",
                    "risk_rating": "Low"
                },
                "account_data": {
                    "account_id": "ACC_SAV_2468",
                    "customer_id": "CUST_FRAUD_001",
                    "account_type": "Savings",
                    "opening_date": "2010-02-01",
                    "current_balance": 2500.0,
                    "average_monthly_balance": 15000.0,
                    "status": "Active"
                },
                "transactions": [
                    {
                        "transaction_id": "TXN_FRAUD_001",
                        "account_id": "ACC_SAV_2468",
                        "amount": 45000.0,
                        "transaction_type": "ACH_Transfer",
                        "date": "2024-01-20",
                        "description": "Online transfer",
                        "counterparty": "Unknown Recipient",
                        "location": "Online"
                    },
                    {
                        "transaction_id": "TXN_FRAUD_002",
                        "account_id": "ACC_SAV_2468",
                        "amount": 30000.0,
                        "transaction_type": "Wire_Transfer",
                        "date": "2024-01-21",
                        "description": "Urgent wire transfer",
                        "counterparty": "Foreign Exchange Co",
                        "location": "Online"
                    }
                ],
                "key_indicators": ["profile inconsistency", "large amounts", "online activity", "elderly customer"]
            },
            
            "sanctions_violation": {
                "name": "Sanctions Violation",
                "description": "Transactions involving sanctioned entities",
                "expected_classification": "Sanctions",
                "expected_risk_level": "Critical",
                "min_confidence": 0.90,
                "customer_data": {
                    "customer_id": "CUST_SANC_001",
                    "name": "Import Export LLC",
                    "date_of_birth": "1982-04-10",
                    "ssn_last_4": "1357",
                    "address": "555 Trade Center, New York, NY 10001",
                    "customer_since": "2020-09-15",
                    "risk_rating": "High"
                },
                "account_data": {
                    "account_id": "ACC_BUS_1357",
                    "customer_id": "CUST_SANC_001",
                    "account_type": "Business",
                    "opening_date": "2020-09-15",
                    "current_balance": 85000.0,
                    "average_monthly_balance": 150000.0,
                    "status": "Active"
                },
                "transactions": [
                    {
                        "transaction_id": "TXN_SANC_001",
                        "account_id": "ACC_BUS_1357",
                        "amount": 95000.0,
                        "transaction_type": "Wire_Transfer",
                        "date": "2024-01-25",
                        "description": "Trade payment",
                        "counterparty": "Sanctioned Entity Corp",
                        "location": "Restricted Country"
                    }
                ],
                "key_indicators": ["sanctioned entity", "prohibited jurisdiction", "trade payment"]
            },
            
            "benign_activity": {
                "name": "Benign Business Activity",
                "description": "Normal business transactions that should not trigger alerts",
                "expected_classification": "Other",
                "expected_risk_level": "Low",
                "min_confidence": 0.6,
                "customer_data": {
                    "customer_id": "CUST_NORMAL_001",
                    "name": "Local Restaurant Inc",
                    "date_of_birth": "1990-07-05",
                    "ssn_last_4": "8642",
                    "address": "111 Main Street, Anytown, USA 12345",
                    "customer_since": "2015-01-15",
                    "risk_rating": "Low"
                },
                "account_data": {
                    "account_id": "ACC_BUS_8642",
                    "customer_id": "CUST_NORMAL_001",
                    "account_type": "Business",
                    "opening_date": "2015-01-15",
                    "current_balance": 25000.0,
                    "average_monthly_balance": 28000.0,
                    "status": "Active"
                },
                "transactions": [
                    {
                        "transaction_id": "TXN_NORM_001",
                        "account_id": "ACC_BUS_8642",
                        "amount": 3500.0,
                        "transaction_type": "Cash_Deposit",
                        "date": "2024-01-15",
                        "description": "Daily cash deposit",
                        "counterparty": None,
                        "location": "Local Branch"
                    },
                    {
                        "transaction_id": "TXN_NORM_002",
                        "account_id": "ACC_BUS_8642",
                        "amount": 1200.0,
                        "transaction_type": "ACH_Transfer",
                        "date": "2024-01-16",
                        "description": "Supplier payment",
                        "counterparty": "Food Supplier Co",
                        "location": "ACH"
                    }
                ],
                "key_indicators": ["consistent with business", "normal amounts", "regular pattern"]
            }
        }
        
        return scenarios
    
    def create_case_data(self, scenario_name: str) -> Optional['CaseData']:
        """Create CaseData object from scenario (requires foundation_sar.py to be implemented)"""
        if not FOUNDATION_AVAILABLE:
            print("⚠️ Cannot create CaseData - foundation_sar.py not yet implemented")
            return None
            
        scenario = self.scenarios[scenario_name]
        
        # Create customer data
        customer = CustomerData(**scenario["customer_data"])
        
        # Create account data  
        account = AccountData(**scenario["account_data"])
        
        # Create transaction data
        transactions = [TransactionData(**txn) for txn in scenario["transactions"]]
        
        # Create case data
        case_data = CaseData(
            case_id=f"CASE_{scenario_name.upper()}",
            customer=customer,
            accounts=[account],
            transactions=transactions,
            created_at=datetime.now()
        )
        
        return case_data
    
    def run_scenario_test(self, agent, scenario_name: str) -> Dict[str, Any]:
        """Run a single scenario test against a Risk Analyst Agent"""
        if not FOUNDATION_AVAILABLE:
            return {"error": "Foundation components not available"}
            
        scenario = self.scenarios[scenario_name]
        case_data = self.create_case_data(scenario_name)
        
        if not case_data:
            return {"error": "Could not create case data"}
        
        try:
            # Run analysis
            start_time = datetime.now()
            result = agent.analyze_case(case_data)
            end_time = datetime.now()
            
            # Validate result
            test_results = {
                "scenario_name": scenario_name,
                "description": scenario["description"],
                "expected_classification": scenario["expected_classification"],
                "actual_classification": result.classification,
                "expected_risk_level": scenario["expected_risk_level"],
                "actual_risk_level": result.risk_level,
                "confidence_score": result.confidence_score,
                "execution_time": (end_time - start_time).total_seconds(),
                "classification_correct": result.classification == scenario["expected_classification"],
                "confidence_acceptable": result.confidence_score >= scenario["min_confidence"],
                "risk_level_correct": result.risk_level == scenario["expected_risk_level"],
                "reasoning": result.reasoning[:200] + "..." if len(result.reasoning) > 200 else result.reasoning,
                "key_indicators": result.key_indicators
            }
            
            test_results["overall_pass"] = (
                test_results["classification_correct"] and 
                test_results["confidence_acceptable"]
            )
            
            return test_results
            
        except Exception as e:
            return {
                "scenario_name": scenario_name,
                "error": str(e),
                "overall_pass": False
            }
    
    def run_all_scenarios(self, agent) -> Dict[str, Any]:
        """Run all scenario tests against a Risk Analyst Agent"""
        results = {}
        
        print("🧪 Running Risk Analyst Scenario Tests...")
        print("=" * 50)
        
        for scenario_name in self.scenarios.keys():
            print(f"\n🔍 Testing: {self.scenarios[scenario_name]['name']}")
            result = self.run_scenario_test(agent, scenario_name)
            results[scenario_name] = result
            
            if "error" in result:
                print(f"   ❌ ERROR: {result['error']}")
            elif result.get("overall_pass", False):
                print(f"   ✅ PASS - Classification: {result['actual_classification']} (confidence: {result['confidence_score']:.2f})")
            else:
                print(f"   ❌ FAIL - Expected: {result['expected_classification']}, Got: {result['actual_classification']}")
        
        # Calculate summary statistics
        total_tests = len(results)
        passed_tests = sum(1 for r in results.values() if r.get("overall_pass", False))
        failed_tests = total_tests - passed_tests
        
        summary = {
            "total_scenarios": total_tests,
            "passed": passed_tests,
            "failed": failed_tests,
            "pass_rate": passed_tests / total_tests if total_tests > 0 else 0,
            "detailed_results": results
        }
        
        print(f"\n📊 SUMMARY: {passed_tests}/{total_tests} scenarios passed ({summary['pass_rate']:.1%})")
        
        return summary
    
    def get_scenario_list(self) -> List[str]:
        """Get list of available test scenarios"""
        return list(self.scenarios.keys())
    
    def get_scenario_description(self, scenario_name: str) -> str:
        """Get description of a specific scenario"""
        return self.scenarios[scenario_name]["description"]


class ComplianceOfficerScenarios:
    """
    Comprehensive test scenarios for Compliance Officer Agent validation.
    
    This class provides pre-built test cases for validating SAR narrative generation
    across different suspicious activity types and regulatory requirements.
    """
    
    def __init__(self):
        self.scenarios = self._create_compliance_scenarios()
    
    def _create_compliance_scenarios(self) -> Dict[str, Dict[str, Any]]:
        """Create test scenarios for compliance narrative generation"""
        
        scenarios = {
            "structuring_narrative": {
                "name": "Structuring SAR Narrative",
                "description": "Generate compliant narrative for structuring activity",
                "risk_analysis": {
                    "classification": "Structuring",
                    "confidence_score": 0.85,
                    "reasoning": "Multiple cash deposits just under $10,000 threshold over 3 consecutive days",
                    "key_indicators": ["threshold avoidance", "repeated amounts", "cash deposits", "multiple locations"],
                    "risk_level": "High"
                },
                "expected_elements": ["Bank Secrecy Act", "$10,000", "currency transaction reporting", "structuring"],
                "max_words": 120,
                "required_regulatory_citations": ["31 USC 5324", "BSA"]
            },
            
            "money_laundering_narrative": {
                "name": "Money Laundering SAR Narrative",
                "description": "Generate compliant narrative for money laundering activity",
                "risk_analysis": {
                    "classification": "Money_Laundering",
                    "confidence_score": 0.90,
                    "reasoning": "Large wire transfers to high-risk jurisdictions with complex layering pattern",
                    "key_indicators": ["high-risk jurisdictions", "large amounts", "layered transactions", "shell companies"],
                    "risk_level": "Critical"
                },
                "expected_elements": ["money laundering", "high-risk", "wire transfer", "layering"],
                "max_words": 120,
                "required_regulatory_citations": ["18 USC 1956", "BSA"]
            },
            
            "fraud_narrative": {
                "name": "Fraud SAR Narrative", 
                "description": "Generate compliant narrative for fraud activity",
                "risk_analysis": {
                    "classification": "Fraud",
                    "confidence_score": 0.78,
                    "reasoning": "Elderly customer account showing uncharacteristic large online transfers",
                    "key_indicators": ["profile inconsistency", "elderly customer", "online activity", "large amounts"],
                    "risk_level": "High"
                },
                "expected_elements": ["fraud", "elderly", "inconsistent", "online"],
                "max_words": 120,
                "required_regulatory_citations": ["18 USC 1344", "BSA"]
            },
            
            "sanctions_narrative": {
                "name": "Sanctions Violation SAR Narrative",
                "description": "Generate compliant narrative for sanctions violation",
                "risk_analysis": {
                    "classification": "Sanctions",
                    "confidence_score": 0.95,
                    "reasoning": "Wire transfer to entity on OFAC sanctions list",
                    "key_indicators": ["sanctioned entity", "OFAC list", "prohibited transaction"],
                    "risk_level": "Critical"
                },
                "expected_elements": ["sanctions", "OFAC", "prohibited", "violation"],
                "max_words": 120,
                "required_regulatory_citations": ["31 CFR 501", "OFAC"]
            }
        }
        
        return scenarios
    
    def create_risk_analysis_output(self, scenario_name: str) -> Optional['RiskAnalystOutput']:
        """Create RiskAnalystOutput from scenario data"""
        if not FOUNDATION_AVAILABLE:
            print("⚠️ Cannot create RiskAnalystOutput - foundation_sar.py not yet implemented")
            return None
            
        scenario = self.scenarios[scenario_name]
        risk_data = scenario["risk_analysis"]
        
        return RiskAnalystOutput(
            classification=risk_data["classification"],
            confidence_score=risk_data["confidence_score"],
            reasoning=risk_data["reasoning"],
            key_indicators=risk_data["key_indicators"],
            risk_level=risk_data["risk_level"]
        )
    
    def validate_narrative(self, narrative: str, scenario_name: str) -> Dict[str, Any]:
        """Validate generated narrative against scenario requirements"""
        scenario = self.scenarios[scenario_name]
        
        # Word count check
        word_count = len(narrative.split())
        word_count_valid = word_count <= scenario["max_words"]
        
        # Required elements check
        narrative_lower = narrative.lower()
        elements_found = []
        elements_missing = []
        
        for element in scenario["expected_elements"]:
            if element.lower() in narrative_lower:
                elements_found.append(element)
            else:
                elements_missing.append(element)
        
        # Regulatory citations check
        citations_found = []
        citations_missing = []
        
        for citation in scenario["required_regulatory_citations"]:
            if citation in narrative:
                citations_found.append(citation)
            else:
                citations_missing.append(citation)
        
        # Basic structure checks
        has_dollar_amount = "$" in narrative
        has_customer_ref = any(word in narrative_lower for word in ["customer", "account holder", "client", "subject"])
        has_activity_ref = any(word in narrative_lower for word in ["transaction", "transfer", "deposit", "activity"])
        
        return {
            "word_count": word_count,
            "word_count_valid": word_count_valid,
            "max_words": scenario["max_words"],
            "elements_found": elements_found,
            "elements_missing": elements_missing,
            "elements_score": len(elements_found) / len(scenario["expected_elements"]),
            "citations_found": citations_found,
            "citations_missing": citations_missing,
            "citations_score": len(citations_found) / len(scenario["required_regulatory_citations"]),
            "has_dollar_amount": has_dollar_amount,
            "has_customer_ref": has_customer_ref,
            "has_activity_ref": has_activity_ref,
            "structure_score": sum([has_dollar_amount, has_customer_ref, has_activity_ref]) / 3
        }
    
    def run_scenario_test(self, agent, scenario_name: str) -> Dict[str, Any]:
        """Run a single compliance scenario test"""
        if not FOUNDATION_AVAILABLE:
            return {"error": "Foundation components not available"}
        
        scenario = self.scenarios[scenario_name]
        
        # Create mock case data (simplified for narrative testing)
        risk_analysis = self.create_risk_analysis_output(scenario_name)
        
        if not risk_analysis:
            return {"error": "Could not create risk analysis data"}
        
        try:
            # Create minimal case data for compliance testing
            customer = CustomerData(
                customer_id="TEST_CUSTOMER",
                name="Test Customer",
                date_of_birth="1980-01-01",
                ssn_last_4="1234",
                address="123 Test St",
                customer_since="2020-01-01",
                risk_rating="Medium"
            )
            
            account = AccountData(
                account_id="TEST_ACCOUNT",
                customer_id="TEST_CUSTOMER",
                account_type="Checking",
                opening_date="2020-01-01",
                current_balance=10000.0,
                average_monthly_balance=8000.0,
                status="Active"
            )
            
            case_data = CaseData(
                case_id="TEST_CASE",
                customer=customer,
                accounts=[account],
                transactions=[],
                created_at=datetime.now()
            )
            
            # Generate narrative
            start_time = datetime.now()
            result = agent.generate_compliance_narrative(case_data, risk_analysis)
            end_time = datetime.now()
            
            # Validate narrative
            validation = self.validate_narrative(result.narrative, scenario_name)
            
            test_results = {
                "scenario_name": scenario_name,
                "description": scenario["description"],
                "narrative": result.narrative,
                "narrative_length": len(result.narrative),
                "word_count": validation["word_count"],
                "execution_time": (end_time - start_time).total_seconds(),
                "validation": validation,
                "regulatory_citations": getattr(result, 'regulatory_citations', []),
                "overall_pass": (
                    validation["word_count_valid"] and
                    validation["elements_score"] >= 0.5 and
                    validation["structure_score"] >= 0.5
                )
            }
            
            return test_results
            
        except Exception as e:
            return {
                "scenario_name": scenario_name,
                "error": str(e),
                "overall_pass": False
            }
    
    def run_all_scenarios(self, agent) -> Dict[str, Any]:
        """Run all compliance scenario tests"""
        results = {}
        
        print("📝 Running Compliance Officer Scenario Tests...")
        print("=" * 50)
        
        for scenario_name in self.scenarios.keys():
            print(f"\n✅ Testing: {self.scenarios[scenario_name]['name']}")
            result = self.run_scenario_test(agent, scenario_name)
            results[scenario_name] = result
            
            if "error" in result:
                print(f"   ❌ ERROR: {result['error']}")
            elif result.get("overall_pass", False):
                print(f"   ✅ PASS - Narrative: {result['word_count']} words")
                print(f"      Preview: {result['narrative'][:100]}...")
            else:
                print(f"   ❌ FAIL - Validation issues detected")
                if result.get("validation"):
                    val = result["validation"]
                    print(f"      Word count: {val['word_count']}/{val['max_words']}")
                    print(f"      Elements: {val['elements_score']:.1%}")
                    print(f"      Structure: {val['structure_score']:.1%}")
        
        # Calculate summary
        total_tests = len(results)
        passed_tests = sum(1 for r in results.values() if r.get("overall_pass", False))
        
        summary = {
            "total_scenarios": total_tests,
            "passed": passed_tests,
            "failed": total_tests - passed_tests,
            "pass_rate": passed_tests / total_tests if total_tests > 0 else 0,
            "detailed_results": results
        }
        
        print(f"\n📊 SUMMARY: {passed_tests}/{total_tests} scenarios passed ({summary['pass_rate']:.1%})")
        
        return summary


# Convenience functions for easy import and use
def get_risk_analyst_scenarios():
    """Get Risk Analyst test scenarios instance"""
    return RiskAnalystScenarios()

def get_compliance_officer_scenarios():
    """Get Compliance Officer test scenarios instance"""
    return ComplianceOfficerScenarios()

def run_quick_agent_test(risk_agent, compliance_agent=None):
    """Run a quick test on both agents with key scenarios"""
    results = {}
    
    # Test Risk Analyst
    if risk_agent:
        print("🔍 Quick Risk Analyst Test...")
        risk_scenarios = RiskAnalystScenarios()
        key_scenarios = ["structuring_classic", "money_laundering_complex"]
        
        for scenario in key_scenarios:
            result = risk_scenarios.run_scenario_test(risk_agent, scenario)
            results[f"risk_{scenario}"] = result
            
            if result.get("overall_pass", False):
                print(f"   ✅ {scenario}: {result['actual_classification']}")
            else:
                print(f"   ❌ {scenario}: Failed")
    
    # Test Compliance Officer
    if compliance_agent:
        print("📝 Quick Compliance Officer Test...")
        compliance_scenarios = ComplianceOfficerScenarios()
        key_scenarios = ["structuring_narrative", "money_laundering_narrative"]
        
        for scenario in key_scenarios:
            result = compliance_scenarios.run_scenario_test(compliance_agent, scenario)
            results[f"compliance_{scenario}"] = result
            
            if result.get("overall_pass", False):
                print(f"   ✅ {scenario}: {result['word_count']} words")
            else:
                print(f"   ❌ {scenario}: Failed")
    
    return results

# Example usage when imported
if __name__ == "__main__":
    print("🧪 SAR Agent Test Scenarios")
    print("=" * 30)
    
    # Show available scenarios
    risk_scenarios = RiskAnalystScenarios()
    compliance_scenarios = ComplianceOfficerScenarios()
    
    print(f"📊 Risk Analyst Scenarios: {len(risk_scenarios.scenarios)}")
    for name, scenario in risk_scenarios.scenarios.items():
        print(f"   • {scenario['name']}: {scenario['description']}")
    
    print(f"\n📝 Compliance Officer Scenarios: {len(compliance_scenarios.scenarios)}")
    for name, scenario in compliance_scenarios.scenarios.items():
        print(f"   • {scenario['name']}: {scenario['description']}")
    
    print("\n💡 Usage:")
    print("   from test_scenarios import get_risk_analyst_scenarios, get_compliance_officer_scenarios")
    print("   risk_tests = get_risk_analyst_scenarios()")
    print("   results = risk_tests.run_all_scenarios(your_risk_agent)")
