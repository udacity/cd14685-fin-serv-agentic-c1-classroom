# 🏦 Financial Services Agentic AI Project - SAR Processing System

## 📋 Project Overview

You will build an **AI-powered Suspicious Activity Report (SAR) processing system** that automates financial crime detection using a multi-agent architecture. This project simulates real-world regulatory requirements that financial institutions face when detecting and reporting suspicious activities to authorities like FinCEN.

### 🎯 Learning Objectives

By completing this project, you will:

1. **Design Multi-Agent Systems**: Build cooperating AI agents with distinct responsibilities
2. **Implement Prompting Strategies**: Apply Chain-of-Thought and ReACT prompting frameworks
3. **Handle Structured Data**: Work with Pydantic schemas for data validation and type safety
4. **Build Compliance Workflows**: Create audit trails and regulatory reporting systems
5. **Optimize AI Costs**: Implement efficient two-stage processing to minimize API calls

### 🏗️ System Architecture

Your system will consist of **two specialized AI agents**:

```
📊 Data Processing → 🔍 Risk Analyst Agent → 👤 Human Review → ✅ Compliance Officer Agent → 📄 SAR Filing
```

- **Risk Analyst Agent**: Uses Chain-of-Thought reasoning to classify suspicious activities
- **Compliance Officer Agent**: Uses ReACT prompting to generate regulatory narratives
- **Human-in-the-Loop**: Critical decision gates for regulatory compliance

### 🎯 Business Context: Why SAR Processing Matters

**Regulatory Requirements:**
- Financial institutions **must** file SARs within 30 days of detecting suspicious activity
- Failure to file can result in **criminal penalties** and fines exceeding $1 billion
- Average investigation costs $500-2,000 per case
- Large banks file 15,000-50,000 SARs annually

**Your AI Solution Addresses:**
- **Volume**: Process millions of transactions efficiently
- **Quality**: Consistent analytical frameworks reduce false positives
- **Cost**: Automated screening and documentation
- **Risk**: Systematic detection prevents regulatory violations

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- VS Code with Jupyter extension (recommended)

### 1. Environment Setup

```bash
# Clone the project (if not already done)
cd project/starter

# Install dependencies
pip install -r requirements.txt

# Set up your OpenAI API key
cp .env.template .env
# Edit .env and add your OPENAI_API_KEY
```

### 2. Project Structure

```
starter/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── .env.template               # Environment variables template
├── data/                       # Sample financial data
│   ├── customers.csv           # Customer profiles
│   ├── accounts.csv            # Account information
│   └── transactions.csv        # Transaction records
├── notebooks/                  # Jupyter notebooks for development
│   ├── 01_data_exploration.ipynb
│   ├── 02_agent_development.ipynb
│   └── 03_workflow_integration.ipynb
├── src/                        # Source code modules
│   ├── __init__.py
│   ├── foundation_sar.py       # Core data schemas (TO IMPLEMENT)
│   ├── risk_analyst_agent.py   # Risk analysis agent (TO IMPLEMENT)
│   └── compliance_officer_agent.py  # Compliance agent (TO IMPLEMENT)
├── tests/                      # Unit tests
│   ├── __init__.py
│   ├── test_foundation.py     # Foundation tests (10) - Run to validate Phase 1
│   ├── test_risk_analyst.py   # Risk Analyst tests (10) - Run to validate Phase 2  
│   └── test_compliance_officer.py # Compliance tests (10) - Run to validate Phase 3
├── outputs/                    # Generated files
│   ├── filed_sars/            # SAR documents
│   └── audit_logs/            # Decision audit trails
└── docs/                      # Additional documentation
    ├── prompting_guide.md
    ├── regulatory_context.md
    └── troubleshooting.md
```

## 📚 Project Phases

### Phase 1: Foundation & Data Modeling (Week 1)
**Notebook: `01_data_exploration.ipynb`**

**Learning Focus:** Pydantic schemas, data validation, type safety

**Tasks:**
1. **Explore the Dataset**: Understand customer, account, and transaction data
2. **Design Data Schemas**: Create Pydantic models for type safety
3. **Build DataLoader**: Combine fragmented data into unified cases
4. **Implement Logging**: Create audit trail system

**Key Files to Implement:**
- `src/foundation_sar.py` - Core data schemas and utilities

**Success Criteria:**
- [ ] All data schemas validate correctly
- [ ] DataLoader creates unified case objects
- [ ] Audit logging captures all operations
- [ ] **Unit tests pass**: `python -m pytest tests/test_foundation.py -v` (10/10 tests should pass)

### Phase 2: Risk Analyst Agent (Week 2)
**Notebook: `02_agent_development.ipynb`**

**Learning Focus:** Chain-of-Thought prompting, financial crime detection

**Tasks:**
1. **Study Chain-of-Thought Prompting**: Learn systematic reasoning frameworks
2. **Implement Risk Classification**: Build agent to categorize suspicious activities
3. **Handle Structured Output**: Parse and validate AI responses
4. **Test with Real Data**: Validate against sample cases

**Key Files to Implement:**
- `src/risk_analyst_agent.py` - Risk analysis with Chain-of-Thought reasoning

**Success Criteria:**
- [ ] Agent classifies 5 activity types: Structuring, Sanctions, Fraud, Money_Laundering, Other
- [ ] Structured JSON output with confidence scores
- [ ] Chain-of-Thought reasoning visible in responses
- [ ] Handles edge cases and parsing errors
- [ ] **Unit tests pass**: `python -m pytest tests/test_risk_analyst.py -v` (10/10 tests should pass)

### Phase 3: Compliance Officer Agent (Week 3)
**Notebook: `02_agent_development.ipynb` (continued)**

**Learning Focus:** ReACT prompting, regulatory narrative generation

**Tasks:**
1. **Learn ReACT Framework**: Reasoning + Action structured prompting
2. **Generate SAR Narratives**: Create regulatory-compliant documentation
3. **Enforce Constraints**: 120-word limits, specific terminology
4. **Regulatory Citations**: Include relevant BSA/AML references

**Key Files to Implement:**
- `src/compliance_officer_agent.py` - Compliance narrative generation

**Success Criteria:**
- [ ] Generates compliant SAR narratives ≤120 words
- [ ] Includes regulatory citations
- [ ] ReACT reasoning framework visible
- [ ] Validates narrative completeness
- [ ] **Unit tests pass**: `python -m pytest tests/test_compliance_officer.py -v` (10/10 tests should pass)

### Phase 4: Workflow Integration (Week 4)
**Notebook: `03_workflow_integration.ipynb`**

**Learning Focus:** Multi-agent coordination, human-in-the-loop systems

**Tasks:**
1. **Build Two-Stage Workflow**: Risk analysis → Human review → Compliance generation
2. **Implement Human Gates**: Decision points for proceeding with SAR filing
3. **Generate SAR Documents**: Complete regulatory forms
4. **Create Efficiency Metrics**: Track cost savings and processing times

**Success Criteria:**
- [ ] Complete workflow processes real cases
- [ ] Human review points function correctly
- [ ] SAR documents generated with all required fields
- [ ] Audit trails capture all decisions
- [ ] Efficiency metrics show cost optimization

## 💡 Key Implementation Hints

### 1. Pydantic Schema Design
```python
from pydantic import BaseModel, Field, field_validator
from typing import Literal, List, Optional

class CustomerData(BaseModel):
    customer_id: str = Field(..., description="Unique customer identifier")
    # Add more fields based on data/customers.csv
    
    @field_validator('customer_id')
    @classmethod
    def validate_customer_id(cls, v):
        # Add your validation logic
        return v
```

### 2. Chain-of-Thought Prompting Structure
```python
system_prompt = """You are a Senior Financial Crime Risk Analyst...

**Analysis Framework** (Think step-by-step):
1. **Data Review**: Examine customer profile...
2. **Pattern Recognition**: Identify indicators...
3. **Regulatory Mapping**: Connect to typologies...
4. **Risk Quantification**: Assess severity...
5. **Classification Decision**: Determine category...
"""
```

### 3. ReACT Framework Implementation
```python
react_prompt = """**ReACT Framework**: Follow this approach:

**REASONING Phase:**
1. Review the risk analyst's findings...
2. Assess regulatory requirements...

**ACTION Phase:**
1. Draft concise narrative...
2. Include specific details...
"""
```

### 4. Error Handling & Validation
```python
try:
    # Parse AI response
    result = json.loads(response_content)
    validated_output = YourPydanticModel(**result)
except json.JSONDecodeError:
    # Handle parsing errors
except ValidationError:
    # Handle schema validation errors
```

## 📊 Sample Data Overview

Your dataset includes:
- **150 customers** with varying risk ratings
- **200+ accounts** across different types
- **500+ transactions** with suspicious patterns

**Key Suspicious Patterns to Detect:**
- **Structuring**: Multiple transactions just under $10,000 reporting threshold
- **Money Laundering**: Complex transaction chains obscuring fund sources
- **Sanctions**: Transactions involving prohibited parties or countries
- **Fraud**: Irregular patterns suggesting fraudulent activity

## 🧪 Testing Your Implementation

### **Progressive Testing Strategy**

Each project phase includes comprehensive unit tests that validate your implementation. The tests are designed to:
- **Skip automatically** when modules aren't implemented yet
- **Provide clear feedback** on what needs to be fixed
- **Validate production readiness** when implementation is complete

### **Running Tests by Phase**

```bash
# Phase 1: Foundation (after implementing foundation_sar.py)
python -m pytest tests/test_foundation.py -v
# Expected: 10 tests pass (or skip if not implemented)

# Phase 2: Risk Analyst (after implementing risk_analyst_agent.py)  
python -m pytest tests/test_risk_analyst.py -v
# Expected: 10 tests pass (or skip if not implemented)

# Phase 3: Compliance Officer (after implementing compliance_officer_agent.py)
python -m pytest tests/test_compliance_officer.py -v  
# Expected: 10 tests pass (or skip if not implemented)

# All phases complete - Full system validation
python -m pytest tests/ -v
# Expected: 30 tests pass (100% success rate)
```

### **Test Categories**

**Foundation Tests (10 tests)**:
- Data schema validation (Pydantic models)
- CSV loading and data aggregation
- Audit logging functionality
- Error handling and edge cases

**Risk Analyst Tests (10 tests)**:
- Agent initialization and configuration
- Chain-of-Thought analysis workflow
- OpenAI API integration and JSON parsing
- Error handling for malformed responses

**Compliance Officer Tests (10 tests)**:
- ReACT framework implementation
- Regulatory narrative generation (≤120 words)
- Multi-format response parsing
- Compliance validation and citations

### **Understanding Test Results**

**✅ PASSED**: Your implementation works correctly  
**⏭️ SKIPPED**: Module not implemented yet (expected during development)  
**❌ FAILED**: Implementation needs fixes - check error messages for guidance

### **Test-Driven Development Tips**

1. **Start with failing tests**: Run tests before implementing to understand requirements
2. **Implement incrementally**: Focus on making one test pass at a time
3. **Use test errors as guides**: Error messages tell you exactly what to fix
4. **Validate frequently**: Run tests after each major change

```bash
# Quick validation during development
python -m pytest tests/test_foundation.py::TestCustomerData::test_valid_customer_data -v
# Run specific test to debug individual functions
```

## 🎯 Assessment Criteria

Your project will be evaluated on:

1. **Technical Implementation (40%)**
   - Correct Pydantic schema design
   - Proper error handling and validation
   - Clean, well-structured code

2. **AI Agent Design (30%)**
   - Effective prompting strategies
   - Structured output parsing
   - Agent coordination

3. **Regulatory Compliance (20%)**
   - Accurate SAR narrative generation
   - Complete audit trails
   - Proper regulatory citations

4. **System Integration (10%)**
   - End-to-end workflow functionality
   - Human-in-the-loop implementation
   - Efficiency optimizations

## 🔧 Development Tips

### Debugging AI Responses
- Always print raw LLM responses before parsing
- Use structured logging to track decision flows
- Test with edge cases and malformed inputs

### Prompt Engineering
- Start with simple prompts and iterate
- Use examples in prompts for better performance
- Test prompts with different transaction patterns

### Performance Optimization
- Implement the two-stage workflow to minimize API calls
- Cache expensive operations where possible
- Use appropriate temperature settings (0.2-0.3 for structured tasks)

## 📚 Additional Resources

- **Regulatory Context**: `docs/regulatory_context.md`
- **Prompting Guide**: `docs/prompting_guide.md`
- **Troubleshooting**: `docs/troubleshooting.md`
- **BSA/AML Guidelines**: [FinCEN Official Resources](https://www.fincen.gov/)

## 🆘 Getting Help

1. **Review the documentation** in the `docs/` folder
2. **Check the test files** for expected behavior
3. **Use the notebooks** for interactive development
4. **Study the sample data** to understand patterns

Remember: This project simulates real regulatory requirements. Focus on building systems that are **explainable**, **auditable**, and **compliant** with financial regulations.

---

**Ready to build the future of financial crime detection? Let's get started! 🚀**
