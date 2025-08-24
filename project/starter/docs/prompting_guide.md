# 🎯 Prompting Guide for SAR Processing System

## 📋 Overview

This guide covers the two main prompting strategies used in the SAR processing system:
- **Chain-of-Thought (CoT)**: For systematic reasoning in risk analysis
- **ReACT (Reasoning + Action)**: For structured narrative generation

## 🧠 Chain-of-Thought Prompting (Risk Analyst Agent)

### What is Chain-of-Thought?

Chain-of-Thought prompting encourages AI models to show their reasoning process step-by-step, leading to more accurate and explainable results.

### Key Principles

1. **Explicit Steps**: Break down complex reasoning into clear steps
2. **Sequential Logic**: Each step builds on previous ones
3. **Domain Expertise**: Frame the AI as a subject matter expert
4. **Structured Output**: Guide toward specific response format

### Example CoT Structure for Financial Crime Analysis

```
**Analysis Framework** (Think step-by-step):
1. **Data Review**: Examine customer profile, account behavior, and transaction patterns
2. **Pattern Recognition**: Identify specific indicators that suggest suspicious activity
3. **Regulatory Mapping**: Connect observations to known suspicious activity typologies
4. **Risk Quantification**: Assess the severity and potential regulatory impact
5. **Classification Decision**: Determine the most appropriate suspicious activity category
```

### Implementation Tips

#### ✅ DO:
- Use numbered steps for clarity
- Include domain-specific terminology
- Ask for reasoning before conclusions
- Provide clear output format specifications
- Include confidence scoring

#### ❌ DON'T:
- Skip the reasoning chain
- Use vague or generic language
- Mix multiple reasoning frameworks
- Forget to specify output format
- Allow ambiguous classifications

### Sample CoT Prompt for Risk Analysis

```python
system_prompt = """You are a Senior Financial Crime Risk Analyst with 15+ years of experience.

**Your Task**: Analyze the provided case data using systematic Chain-of-Thought reasoning.

**Analysis Framework** (Think step-by-step):
1. **Data Review**: Examine customer profile, account behavior, and transaction patterns
2. **Pattern Recognition**: Identify specific indicators that suggest suspicious activity
3. **Regulatory Mapping**: Connect observations to known suspicious activity typologies
4. **Risk Quantification**: Assess the severity and potential regulatory impact
5. **Classification Decision**: Determine the most appropriate suspicious activity category

**Classification Categories**:
- Structuring: Transactions designed to avoid reporting thresholds
- Sanctions: Potential sanctions violations or prohibited parties
- Fraud: Fraudulent transactions or identity-related crimes
- Money_Laundering: Complex schemes to obscure illicit fund sources
- Other: Suspicious patterns not fitting standard categories

**Output Format** (JSON only):
{
    "classification": "[category]",
    "confidence_score": [0.0-1.0],
    "reasoning": "[step-by-step analysis]",
    "key_indicators": ["indicator1", "indicator2"],
    "risk_level": "[Low/Medium/High/Critical]"
}"""
```

## ⚡ ReACT Prompting (Compliance Officer Agent)

### What is ReACT?

ReACT (Reasoning + Action) prompting separates the thinking process into two phases:
- **Reasoning Phase**: Analyze the situation and plan approach
- **Action Phase**: Execute the specific task with informed decisions

### Key Principles

1. **Separation of Concerns**: Clear distinction between thinking and doing
2. **Informed Action**: Actions are based on explicit reasoning
3. **Structured Workflow**: Consistent approach to complex tasks
4. **Regulatory Compliance**: Emphasis on meeting specific requirements

### Example ReACT Structure for Compliance Narratives

```
**ReACT Framework**:

**REASONING Phase:**
1. Review the risk analyst's classification and supporting evidence
2. Assess case facts against regulatory narrative requirements
3. Identify key compliance elements that must be included
4. Consider narrative structure for maximum regulatory clarity

**ACTION Phase:**
1. Draft concise narrative (≤120 words) using regulatory language
2. Include specific transaction details, amounts, and timeframes
3. Reference the suspicious activity pattern clearly
4. Ensure narrative supports the risk classification
```

### Implementation Tips

#### ✅ DO:
- Clearly separate REASONING and ACTION phases
- Reference inputs explicitly in reasoning
- Include specific constraints in action phase
- Use regulatory terminology consistently
- Validate output against requirements

#### ❌ DON'T:
- Mix reasoning and action steps
- Skip the reasoning phase
- Ignore word limits or constraints
- Use inappropriate language register
- Forget regulatory citations

### Sample ReACT Prompt for Compliance Narratives

```python
system_prompt = """You are a Senior Compliance Officer with expertise in BSA/AML regulations.

**ReACT Framework**: Follow this systematic approach:

**REASONING Phase:**
1. Review the risk analyst's classification and supporting evidence
2. Assess case facts against regulatory narrative requirements
3. Identify key compliance elements that must be included
4. Consider narrative structure for maximum regulatory clarity

**ACTION Phase:**
1. Draft concise narrative (≤120 words) using regulatory language
2. Include specific transaction details, amounts, and timeframes
3. Reference the suspicious activity pattern clearly
4. Ensure narrative supports the risk classification

**Critical Constraints:**
- Maximum 120 words for the narrative
- Use precise financial crime terminology
- Include quantitative details (amounts, dates, counts)
- Maintain objective, factual tone

**Output Format** (JSON only):
{
    "narrative": "[regulatory narrative ≤120 words]",
    "narrative_reasoning": "[explanation of construction decisions]",
    "regulatory_citations": ["relevant BSA/AML regulations"],
    "completeness_check": [true/false]
}"""
```

## 🔧 Prompt Engineering Best Practices

### 1. Persona Design
- **Specific Expertise**: "Senior Financial Crime Risk Analyst with 15+ years"
- **Relevant Experience**: Include domain-specific background
- **Authority**: Establish credibility for better responses

### 2. Instruction Clarity
- **Explicit Steps**: Number or bullet point all steps
- **Clear Constraints**: Specify word limits, format requirements
- **Examples**: Provide sample outputs when helpful

### 3. Output Formatting
- **Structured JSON**: Use consistent schema across agents
- **Field Descriptions**: Clear descriptions for each output field
- **Validation Rules**: Specify data types and constraints

### 4. Error Prevention
- **Format Specification**: "Return ONLY valid JSON"
- **Constraint Reminders**: Repeat critical limits
- **Fallback Instructions**: Handle edge cases

### 5. Domain Expertise
- **Technical Terminology**: Use proper financial crime vocabulary
- **Regulatory Context**: Reference actual regulations (BSA, AML)
- **Industry Standards**: Follow established practices

## 🧪 Testing Your Prompts

### 1. Unit Testing
```python
def test_prompt_with_sample_case():
    # Test with known input/output pairs
    # Verify JSON parsing works
    # Check constraint compliance
```

### 2. Edge Case Testing
- Empty or minimal data
- Ambiguous patterns
- Extreme values
- Malformed inputs

### 3. Consistency Testing
- Same input should produce similar outputs
- Different models should handle prompts appropriately
- Various temperature settings

### 4. Performance Testing
- Token usage optimization
- Response time measurement
- Cost per analysis calculation

## 📊 Prompt Optimization Strategies

### 1. Iterative Refinement
- Start with basic prompts
- Add constraints based on observed issues
- Refine based on output quality

### 2. Temperature Tuning
- **Risk Analysis**: 0.2-0.3 (more deterministic)
- **Narrative Generation**: 0.3-0.4 (slight creativity)
- **Structured Output**: Lower temperatures generally better

### 3. Few-Shot Examples
When needed, include examples in prompts:
```
**Example Analysis**:
Input: [sample case data]
Output: {"classification": "Money_Laundering", ...}
```

### 4. Prompt Length Optimization
- Balance detail with token efficiency
- Use clear, concise language
- Remove redundant instructions

## ⚠️ Common Pitfalls to Avoid

1. **Inconsistent Formatting**: Always specify exact output format
2. **Ambiguous Instructions**: Be explicit about requirements
3. **Missing Constraints**: Include all validation rules
4. **Weak Personas**: Generic roles produce generic responses
5. **No Error Handling**: Plan for malformed outputs
6. **Regulatory Gaps**: Ensure compliance with actual regulations

## 🚀 Advanced Techniques

### 1. Multi-Turn Conversations
- Break complex tasks into multiple API calls
- Build context across interactions
- Handle clarifications and refinements

### 2. Dynamic Prompting
- Adjust prompts based on case complexity
- Use different templates for different scenarios
- Implement prompt selection logic

### 3. Prompt Chaining
- Use output from one agent as input to another
- Maintain context across agent handoffs
- Implement validation between stages

---

**💡 Remember**: Great prompts are the foundation of effective AI agents. Invest time in crafting, testing, and refining your prompts for optimal performance in the SAR processing system.
