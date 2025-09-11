# Lesson 1: Introduction to Prompting - Personal Finance Advisory AI Assistant

## Overview

This lesson introduces the fundamentals of prompt engineering through the lens of creating personal finance advisory AI assistants. You'll learn how to craft prompts that instruct an AI to convincingly adopt the persona of different financial professionals during client advisory sessions.

## Learning Objectives

By the end of this lesson, you will:

1. **Understand Role-Based Prompting**: Learn how to craft prompts that define specific professional personas for AI assistants
2. **Master Persona Development**: Experiment with different personal finance professional roles and expertise levels
3. **Create Client-Focused Responses**: Develop prompts that generate consistent, professional responses for financial planning scenarios
4. **Practice Iterative Refinement**: Learn to systematically improve AI assistant performance through prompt iteration

## Context: Personal Finance Advisory

Personal finance advisory requires expertise across multiple domains - from investment planning and debt management to retirement planning and tax optimization. Different client situations call for different advisory approaches and expertise levels.

This lesson focuses on creating AI assistants that can adopt various personal finance professional personas:

- **Certified Financial Planner (CFP)**: Comprehensive financial planning and long-term strategy
- **Investment Advisor**: Portfolio management and investment strategy
- **Debt Counselor**: Debt consolidation and credit improvement strategies
- **Retirement Planning Specialist**: 401(k) optimization and retirement income planning

## Exercise Structure

### Starter Exercise (`exercises/starter/`)
The starter notebook provides a guided learning experience with TODO sections for hands-on practice:

1. **Plain Prompt Baseline**: Start with a basic financial assistant
2. **CFP Persona Creation**: Define a Certified Financial Planner role
3. **Expertise Enhancement**: Add specific personal finance knowledge areas
4. **Communication Style**: Refine tone and approach for client interactions
5. **Investment Advisor**: Create an alternative investment-focused persona
6. **Multi-Scenario Testing**: Test personas across different client situations
7. **Reflection & Analysis**: Evaluate persona effectiveness

### Solution Exercise (`exercises/solution/`)
The solution notebook demonstrates best practices and complete implementations:

- Complete persona definitions with detailed expertise areas
- Professional communication style examples
- Comprehensive scenario testing
- Analysis of different approach effectiveness

## Key Scenarios Covered

### Primary Client Scenario
**Alex Chen, 28-year-old Software Engineer**
- Annual income: $95,000
- Recent $15,000 bonus
- Mixed debt and investment priorities
- First-time investor seeking guidance

### Additional Testing Scenarios
1. **Retirement Planning**: Mid-career professional assessing retirement readiness
2. **Family Financial Planning**: New parents balancing multiple financial priorities
3. **Debt Management**: Recent graduate managing student loans and credit card debt

## Technical Setup

### Prerequisites
- Python environment with required packages
- OpenAI API access configured for Vocareum
- Environment variables properly set

### Key Dependencies
```python
import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display
```

### Vocareum Configuration
The notebooks are configured to work with the Vocareum classroom environment:
```python
client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

## Learning Progression

### 1. Foundation (Plain Prompt)
Start with basic prompts to establish baseline AI behavior and understand the importance of role definition.

### 2. Role Definition (CFP Persona)
Learn to create specific professional roles that change AI response quality and focus.

### 3. Expertise Integration
Add detailed domain knowledge to create more authoritative and accurate financial guidance.

### 4. Communication Refinement
Develop client-appropriate communication styles that balance professionalism with accessibility.

### 5. Persona Comparison
Compare different financial professional personas (CFP vs. Investment Advisor) to understand specialization benefits.

### 6. Scenario Adaptation
Test persona consistency across diverse client situations and financial challenges.

## Key Concepts

### Role-Based Prompting
- **Persona Definition**: Creating specific professional identities for AI assistants
- **Expertise Specification**: Adding relevant knowledge areas and experience
- **Communication Style**: Defining appropriate tone and approach for target audience

### Personal Finance Domain
- **Comprehensive Planning**: Holistic approach to client financial health
- **Specialized Advisory**: Focused expertise in specific areas (investment, debt, retirement)
- **Client Education**: Empowering clients through explanation and guidance
- **Fiduciary Standards**: Maintaining professional ethics and client-first approach

### Prompt Engineering Techniques
- **Progressive Enhancement**: Building complexity through iterative refinement
- **Context Specification**: Adding relevant background and constraints
- **Output Formatting**: Structuring responses for maximum clarity and actionability

## Best Practices

### For Personal Finance AI Personas
1. **Regulatory Awareness**: Include references to industry standards (CFP Board, fiduciary duty)
2. **Evidence-Based Approach**: Emphasize data-driven and research-backed recommendations
3. **Client Education**: Focus on explaining the "why" behind financial advice
4. **Risk Assessment**: Appropriate recommendations based on client circumstances
5. **Professional Boundaries**: Maintain appropriate disclaimers and scope of advice

### For Prompt Development
1. **Clear Role Definition**: Start with specific professional identity
2. **Relevant Expertise**: Add knowledge areas that match the role's specialization
3. **Appropriate Communication**: Match tone and style to target audience
4. **Scenario Testing**: Validate persona effectiveness across multiple situations
5. **Iterative Refinement**: Continuously improve based on output quality

## Real-World Applications

The techniques learned in this lesson can be applied to:

- **Financial Planning Software**: Creating specialized advisory modules
- **Robo-Advisor Platforms**: Enhancing automated financial guidance
- **Educational Tools**: Building financial literacy and planning resources
- **Client Onboarding**: Developing needs assessment and goal-setting systems
- **Professional Training**: Creating practice scenarios for financial advisors

## Next Steps

This foundation in role-based prompting prepares you for advanced techniques in subsequent lessons:

- **Lesson 2**: Chain-of-Thought and ReACT reasoning for complex financial analysis
- **Lesson 3**: Prompt instruction refinement for sophisticated financial planning scenarios
- **Lesson 4**: Chaining prompts to create comprehensive financial planning workflows
- **Lesson 5**: Building self-learning financial advisory systems with feedback loops

## Success Metrics

By completing this lesson, you should be able to:

✅ Create effective role-based prompts for financial professionals  
✅ Define persona-specific expertise and communication styles  
✅ Generate consistent, professional financial guidance across scenarios  
✅ Understand the impact of prompt refinement on AI assistant quality  
✅ Apply these techniques to real-world personal finance applications  

---

**Ready to build your first personal finance AI assistant? Start with the starter notebook and work through each progressive enhancement!** 🎯💰