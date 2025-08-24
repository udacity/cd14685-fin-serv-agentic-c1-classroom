# Lesson 4: Chaining Prompts for Agentic Reasoning

## Overview

This lesson teaches you how to build sophisticated multi-step AI workflows using prompt chaining with validation gates. You'll learn to design agentic AI systems that can perform complex reasoning tasks by breaking them into structured stages.

## Learning Objectives

By completing this lesson, you will be able to:

- **Design Multi-Step Workflows**: Create AI systems that chain prompts together for complex reasoning
- **Implement Validation Gates**: Use Pydantic models to ensure data quality between workflow stages
- **Build Robust Error Handling**: Create systems that gracefully handle validation failures
- **Generate Automated Scripts**: Develop AI that can create monitoring and automation code
- **Apply Agentic Reasoning**: Use structured approaches for sophisticated AI decision-making

## Key Concepts

### Prompt Chaining
- **Sequential Processing**: Link outputs from one AI prompt to inputs of the next
- **Context Preservation**: Maintain information flow across multiple reasoning stages
- **Workflow Orchestration**: Coordinate complex multi-step AI processes

### Validation Gates
- **Data Integrity**: Ensure structured outputs meet quality standards
- **Error Prevention**: Catch issues before they cascade through the workflow
- **Quality Control**: Validate AI responses using programmatic checks

### Agentic Reasoning
- **Structured Decision Making**: Break complex problems into manageable steps
- **Iterative Refinement**: Use validation feedback to improve prompt quality
- **Production Readiness**: Build reliable systems for real-world deployment

## Exercise Structure

### Three-Stage Financial Compliance Workflow

1. **Stage 1: Data Collection**
   - Extract customer information from unstructured text
   - Validate data completeness and format
   - Structure information for subsequent analysis

2. **Stage 2: Risk Analysis** 
   - Assess multiple risk factors systematically
   - Calculate risk scores and classifications
   - Identify mitigation factors

3. **Stage 3: Compliance Report**
   - Generate final compliance determination
   - Specify regulatory requirements
   - Create monitoring scripts for ongoing oversight

## Files in This Directory

### `lesson-4-financial-compliance-workflow.ipynb`
**Main Exercise Notebook** - Contains TODO sections for you to complete:

- Pydantic model validation logic
- Stage-specific prompt engineering
- Workflow orchestration implementation
- Error handling and recovery

### `lesson-4-financial-compliance-workflow-solution.ipynb`
**Complete Solution** - Fully implemented version showing:

- Complete Pydantic models with validation
- Optimized prompts for each stage
- Robust workflow orchestration
- Advanced error handling patterns

## Technical Requirements

### Prerequisites
- Python 3.8+
- OpenAI API access
- Basic understanding of Pydantic for data validation

### Required Packages
```bash
pip install -r ../../requirements.txt
```

### Key Dependencies
- `openai` - For AI model access
- `pydantic` - For data validation and modeling
- `python-dotenv` - For environment variable management

## Getting Started

### 1. Environment Setup
```bash
# Install dependencies
pip install -r ../../requirements.txt

# Configure API key in .env file
cp ../../.env.example ../../.env
# Edit .env and add your OpenAI API key
```

### 2. Start with the Exercise Notebook
Open `lesson-4-financial-compliance-workflow.ipynb` and work through the TODO sections:

1. **Complete Pydantic Models** (15 min)
   - Add validation logic for customer names
   - Implement risk factor validation
   - Create compliance status validation

2. **Build Stage Prompts** (25 min)
   - Create data extraction prompt
   - Design risk assessment prompt  
   - Develop compliance reporting prompt

3. **Implement Workflow** (10 min)
   - Connect the three stages
   - Add error handling
   - Test complete workflow

### 3. Validation and Testing
- Run each stage individually to verify prompts
- Test validation gates with invalid data
- Execute complete workflow with sample scenario

### 4. Compare with Solution
Review the solution notebook to see:
- Best practices for prompt engineering
- Advanced validation techniques
- Production-ready error handling

## Success Criteria

By the end of this exercise, your implementation should:

✅ **Extract structured data** from unstructured customer scenarios  
✅ **Validate data quality** using Pydantic models at each stage  
✅ **Generate risk assessments** with scores and factor analysis  
✅ **Produce compliance reports** with specific recommendations  
✅ **Create monitoring scripts** for ongoing oversight  
✅ **Handle errors gracefully** when validation fails  

## Real-World Applications

This pattern is applicable to many financial services scenarios:

- **Credit Risk Assessment**: Multi-factor loan approval workflows
- **Transaction Monitoring**: Automated suspicious activity detection
- **Regulatory Reporting**: Compliance documentation generation
- **Customer Onboarding**: KYC/AML verification processes
- **Investment Analysis**: Multi-stage due diligence workflows


## Troubleshooting

### Common Issues

**Validation Errors**: 
- Check Pydantic model field definitions
- Verify JSON structure in AI responses
- Ensure all required fields are present

**API Errors**:
- Verify OpenAI API key is correctly set
- Check internet connectivity
- Monitor API usage limits

**Prompt Quality**:
- Test prompts with various input scenarios
- Refine instructions for better JSON output
- Add examples to improve AI understanding

