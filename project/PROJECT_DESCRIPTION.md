# 🏦 Financial Services Agentic AI Project

## 📋 Project Description

**Build an AI-powered Suspicious Activity Report (SAR) processing system** that automates financial crime detection using multi-agent architecture with Chain-of-Thought and ReACT prompting strategies.

### 🎯 What You'll Build

You will create a complete SAR processing system that:
- **Detects suspicious financial activity** using AI-powered pattern recognition
- **Generates regulatory-compliant reports** for FinCEN submission
- **Implements human-in-the-loop decision gates** for compliance oversight
- **Creates comprehensive audit trails** for regulatory examination

### 🏗️ System Architecture Overview

```
📊 CSV Data → 🔍 Risk Analyst Agent → 👤 Human Review → ✅ Compliance Officer Agent → 📄 SAR Filing
                 (Chain-of-Thought)                      (ReACT Framework)
```

## 📂 Project Directory Structure

### 🚀 **START HERE: Essential Files**

```
project/
├── PROJECT_DESCRIPTION.md          # ← YOU ARE HERE (this file)
├── GRADING_RUBRIC.md               # Assessment criteria
└── starter/                        # ← YOUR MAIN WORKING DIRECTORY
    ├── README.md                   # Complete project guide
    ├── .env.template              # API key setup
    ├── requirements.txt           # Dependencies to install
    └── notebooks/                 # Interactive learning
        ├── 01_data_exploration.ipynb      # Week 1: Start here!
        └── 02_agent_development.ipynb     # Week 2-3: Build agents
```

### 📊 **Data & Resources (Provided)**

```
starter/
├── data/                          # Sample financial data
│   ├── customers.csv             # Customer profiles (150+ records)
│   ├── accounts.csv              # Account information
│   └── transactions.csv          # Transaction records (500+ with suspicious patterns)
└── docs/                         # Reference materials
    ├── prompting_guide.md        # Chain-of-Thought & ReACT tutorials
    └── regulatory_context.md     # Real SAR requirements
```

### 💻 **Code to Implement (Your Work)**

```
starter/src/                       # Core modules you'll build
├── foundation_sar.py             # Week 1: Data schemas & utilities
├── risk_analyst_agent.py         # Week 2: Chain-of-Thought agent
└── compliance_officer_agent.py   # Week 3: ReACT narrative agent
```

### 🧪 **Testing & Outputs (Generated)**

```
starter/
├── tests/                        # Unit test templates
├── outputs/
│   ├── filed_sars/              # Generated SAR documents
│   └── audit_logs/              # Decision audit trails
```

## � **Learning Path**

### **Phase 1: Foundation & Data Modeling**
📖 **Start with:** `notebooks/01_data_exploration.ipynb`
🎯 **Goal:** Understand financial data and build foundation components

**Tasks:**
1. Explore customer, account, and transaction data
2. Identify suspicious activity patterns
3. Implement Pydantic schemas in `foundation_sar.py`
4. Create data loading and audit logging systems

**Deliverable:** Working foundation module with validated schemas

### **Phase 2: Risk Analyst Agent**
📖 **Continue with:** `notebooks/02_agent_development.ipynb`
🎯 **Goal:** Build Chain-of-Thought reasoning for suspicious activity classification

**Tasks:**
1. Study Chain-of-Thought prompting methodology
2. Implement risk analysis agent in `risk_analyst_agent.py`
3. Test with different suspicious activity patterns
4. Validate JSON output parsing and error handling

**Deliverable:** Risk Analyst Agent that classifies 5 crime types with confidence scores

### **Phase 3: Compliance Officer Agent**
📖 **Continue with:** `notebooks/02_agent_development.ipynb`
🎯 **Goal:** Build ReACT framework for regulatory narrative generation

**Tasks:**
1. Learn ReACT (Reasoning + Action) prompting
2. Implement compliance agent in `compliance_officer_agent.py`
3. Generate SAR narratives ≤120 words with regulatory citations
4. Validate narrative completeness and terminology

**Deliverable:** Compliance Officer Agent that generates regulatory-compliant narratives

### **Phase 4: System Integration**
📖 **Create:** `notebooks/03_workflow_integration.ipynb`
🎯 **Goal:** Build complete two-stage workflow with human oversight

**Tasks:**
1. Integrate both agents into unified workflow
2. Implement human-in-the-loop decision gates
3. Generate complete SAR documents
4. Create efficiency metrics and cost optimization

**Deliverable:** End-to-end SAR processing system with audit trails

## 🚀 **Getting Started**

### **Dependencies**

Before starting the project, ensure you have:

```
Python 3.8+
OpenAI API key
VS Code with Jupyter extension (recommended)
Git (for version control)
```

**Required Python packages** (automatically installed via requirements.txt):
```
pandas>=2.0.0          # Data manipulation
pydantic>=2.0.0         # Data validation
openai>=1.0.0          # AI/LLM integration
python-dotenv>=1.0.0   # Environment variables
jupyter>=1.0.0         # Notebook development
pytest>=7.0.0          # Testing framework
matplotlib>=3.7.0      # Visualization
seaborn>=0.12.0        # Statistical plots
```

### **Installation**

Step-by-step setup to get your development environment running:

**1. Navigate to the starter directory:**
```bash
cd project/starter
```

**2. Install Python dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables:**
```bash
cp .env.template .env
```

**4. Configure your OpenAI API key:**
```bash
# Edit .env file and add:
OPENAI_API_KEY=your_actual_api_key_here
```

**5. Verify installation:**
```bash
python -c "import pandas, pydantic, openai; print('✅ All dependencies installed successfully!')"
```

**6. Start exploring the data:**
```bash
# Open the first notebook
jupyter notebook notebooks/01_data_exploration.ipynb
# OR use VS Code
code notebooks/01_data_exploration.ipynb
```

## 💡 **Key Learning Objectives**

### **Technical Skills:**
- **Multi-Agent Systems**: Design agents with distinct responsibilities
- **Advanced Prompting**: Chain-of-Thought and ReACT methodologies
- **Data Validation**: Pydantic schemas for type safety
- **Error Handling**: Robust LLM output parsing
- **System Integration**: Human-in-the-loop workflows

### **AI/ML Concepts:**
- **Structured Reasoning**: Step-by-step analytical frameworks
- **Explainable AI**: Audit trails for regulatory compliance
- **Cost Optimization**: Two-stage processing to minimize API calls
- **Performance Monitoring**: Validation and efficiency metrics

### **Domain Knowledge:**
- **Financial Crime Detection**: Real suspicious activity patterns
- **Regulatory Compliance**: BSA/AML requirements and SAR filing
- **Risk Assessment**: Customer profiling and transaction monitoring
- **Audit Documentation**: Complete decision trails for examination

## 🧪 **Testing**

The project includes comprehensive testing frameworks to validate your implementation:

### **Running Tests**

**Unit Tests for Foundation Components:**
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test modules
python -m pytest tests/test_foundation.py -v
python -m pytest tests/test_risk_analyst.py -v
python -m pytest tests/test_compliance_officer.py -v
```

**Interactive Testing via Notebooks:**
```bash
# Test data loading and schema validation
jupyter notebook notebooks/01_data_exploration.ipynb

# Test agent implementations
jupyter notebook notebooks/02_agent_development.ipynb
```

### **Test Categories Breakdown**

**Foundation Tests (`test_foundation.py`):**
- **Schema Validation**: Verify Pydantic models work with real CSV data
- **Data Loading**: Test DataLoader creates unified case objects correctly
- **Audit Logging**: Validate ExplainabilityLogger captures all operations
- **Error Handling**: Ensure graceful handling of malformed data

**Risk Analyst Tests (`test_risk_analyst.py`):**
- **Prompt Engineering**: Test Chain-of-Thought reasoning framework
- **Classification Accuracy**: Verify correct suspicious activity categorization
- **JSON Parsing**: Test structured output handling and error recovery
- **Edge Cases**: Validate behavior with unusual or minimal data

**Compliance Officer Tests (`test_compliance_officer.py`):**
- **ReACT Framework**: Test Reasoning + Action prompt structure
- **Narrative Quality**: Verify regulatory compliance and word limits
- **Citation Accuracy**: Test proper regulatory references
- **Integration**: Validate works with Risk Analyst outputs

**Integration Tests:**
- **End-to-End Workflow**: Complete processing from CSV to SAR document
- **Human Gates**: Test decision points and user interaction
- **Performance**: Validate system efficiency and cost optimization

### **Test Data and Scenarios**

The testing framework includes:
- **Synthetic Test Cases**: Pre-built scenarios for each suspicious activity type
- **Real Data Validation**: Tests using the provided CSV datasets
- **Edge Case Coverage**: Malformed inputs, missing data, API failures
- **Performance Benchmarks**: Response time and accuracy metrics

Example test execution:
```bash
# Quick validation test
python src/foundation_sar.py

# Comprehensive test suite
python -m pytest tests/ --tb=short

# Test with coverage report
python -m pytest tests/ --cov=src --cov-report=html
```

## 📋 **Project Instructions**

This section contains all student deliverables and implementation requirements for the SAR processing system.

### **Phase 1 Deliverables: Foundation & Data Modeling**

**Core Implementation (`src/foundation_sar.py`):**
- [ ] **CustomerData Schema**: Pydantic model matching `data/customers.csv` structure
- [ ] **AccountData Schema**: Pydantic model for account information with balance validation
- [ ] **TransactionData Schema**: Transaction records with amount and date validation
- [ ] **CaseData Schema**: Unified schema combining customer, accounts, and transactions
- [ ] **RiskAnalystOutput Schema**: Structured output for risk analysis results
- [ ] **ComplianceOfficerOutput Schema**: Structured output for compliance narratives
- [ ] **ExplainabilityLogger Class**: Audit logging system with JSONL output
- [ ] **DataLoader Class**: CSV data processing and case object creation

**Validation Requirements:**
- All schemas must validate successfully with provided CSV data
- Implement field validators for critical data (dates, amounts, risk ratings)
- Handle optional fields and missing data gracefully
- Include comprehensive error messages for validation failures

### **Phase 2 Deliverables: Risk Analyst Agent**

**Core Implementation (`src/risk_analyst_agent.py`):**
- [ ] **Chain-of-Thought System Prompt**: 5-step reasoning framework for financial crime analysis
- [ ] **RiskAnalystAgent Class**: Main agent class with OpenAI integration
- [ ] **analyze_case Method**: Process CaseData and return RiskAnalystOutput
- [ ] **JSON Parsing Logic**: Robust extraction and validation of LLM responses
- [ ] **Error Handling**: Comprehensive error recovery for API failures and malformed outputs

**Classification Requirements:**
- Support 5 suspicious activity types: Structuring, Sanctions, Fraud, Money_Laundering, Other
- Generate confidence scores (0.0-1.0) for all classifications
- Provide clear reasoning chains following Chain-of-Thought methodology
- Include key suspicious indicators in structured format
- Assign risk levels: Low, Medium, High, Critical

### **Phase 3 Deliverables: Compliance Officer Agent**

**Core Implementation (`src/compliance_officer_agent.py`):**
- [ ] **ReACT System Prompt**: Reasoning + Action framework for narrative generation
- [ ] **ComplianceOfficerAgent Class**: Main agent class with regulatory focus
- [ ] **generate_compliance_narrative Method**: Create SAR narratives from risk analysis
- [ ] **Narrative Validation**: Word count limits (≤120 words) and terminology checking
- [ ] **Regulatory Citations**: Include relevant BSA/AML regulation references

**Compliance Requirements:**
- Generate narratives suitable for FinCEN submission
- Include all required elements: who, what, when, where, why
- Use appropriate regulatory terminology and professional tone
- Validate narrative completeness and regulatory compliance
- Provide reasoning for narrative construction decisions

### **Phase 4 Deliverables: System Integration**

**Workflow Implementation (`notebooks/03_workflow_integration.ipynb`):**
- [ ] **Two-Stage Processing**: Risk analysis → Human review → Compliance generation
- [ ] **Human Decision Gates**: Interactive approval/rejection points
- [ ] **SAR Document Generation**: Complete regulatory forms with all required fields
- [ ] **Audit Trail Creation**: Comprehensive logging of all decisions and reasoning
- [ ] **Efficiency Metrics**: Cost tracking and performance optimization demonstrations

**Integration Requirements:**
- Process real cases from provided CSV data
- Demonstrate human-in-the-loop decision making
- Generate complete SAR documents in JSON format
- Create audit logs suitable for regulatory examination
- Show cost optimization benefits of two-stage approach

### **Documentation Requirements**

**Code Documentation:**
- [ ] Comprehensive docstrings for all classes and methods
- [ ] Inline comments explaining complex logic and business rules
- [ ] Type hints for all function parameters and return values
- [ ] Clear error messages and logging statements

**Implementation Documentation:**
- [ ] Updated README.md with any customizations or additional features
- [ ] Notebook documentation showing development process and testing
- [ ] Example outputs demonstrating system capabilities
- [ ] Performance metrics and efficiency analysis

## � **Success Criteria**

By project completion, your system should:
- ✅ Process real financial data with proper validation
- ✅ Classify 5 types of suspicious activities with confidence scores
- ✅ Generate regulatory-compliant narratives ≤120 words
- ✅ Include human decision gates for compliance oversight
- ✅ Create complete audit trails for all decisions
- ✅ Demonstrate cost optimization through two-stage processing

## 🛠️ **Built With**

This project utilizes the following technologies and frameworks:

* **[Python 3.8+](https://python.org)** - Core programming language
* **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation and settings management
* **[OpenAI API](https://platform.openai.com/)** - Large Language Model integration
* **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
* **[Jupyter](https://jupyter.org/)** - Interactive development environment
* **[pytest](https://pytest.org/)** - Testing framework
* **[python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variable management
* **[Matplotlib](https://matplotlib.org/)** - Data visualization
* **[Seaborn](https://seaborn.pydata.org/)** - Statistical data visualization

**AI/ML Frameworks:**
* **Chain-of-Thought Prompting** - Systematic reasoning methodology
* **ReACT Framework** - Reasoning + Action structured prompting
* **Multi-Agent Architecture** - Specialized AI agents with distinct responsibilities

**Financial Services Context:**
* **BSA/AML Regulations** - Bank Secrecy Act and Anti-Money Laundering compliance
* **FinCEN SAR Requirements** - Suspicious Activity Report filing standards
* **Financial Crime Typologies** - Industry-standard suspicious activity classifications

### **Built-in Resources:**
1. **README.md** - Comprehensive project guide with code examples
2. **docs/prompting_guide.md** - Detailed Chain-of-Thought and ReACT tutorials
3. **docs/regulatory_context.md** - Real-world SAR requirements
4. **Interactive notebooks** - Step-by-step guided implementation

### **Common Questions:**
- **"Where do I start?"** → Open `notebooks/01_data_exploration.ipynb`
- **"How do I design prompts?"** → Check `docs/prompting_guide.md`
- **"What are SAR requirements?"** → Read `docs/regulatory_context.md`
- **"How do I test my agents?"** → Use test scenarios in notebooks

### **Debugging Tips:**
- Always print raw LLM responses before parsing JSON
- Use the provided validation functions to check outputs
- Test with sample cases before running on full datasets
- Check the audit logs for detailed decision trails

## ⚠️ **Important Notes**

### **Educational Context:**
- This is a **simulation** using synthetic financial data
- Real SAR systems require additional regulatory approvals
- Focus on learning AI techniques rather than actual compliance
