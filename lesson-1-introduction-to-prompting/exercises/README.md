# Lesson 1 Exercise: Financial AI Assistant for Customer Risk Assessment

## Exercise Introduction: Building Intelligent Financial AI Personas

You've learned about prompting fundamentals and role-based AI for creating specialized agent personas. Now, you'll put that into practice in a realistic financial services scenario by creating an AI-powered customer risk assessment assistant that can adapt its expertise and communication style based on different roles within a financial institution.

### The Challenge: Crafting Specialized Financial AI Personas

Imagine you work at a financial institution that needs AI assistants to help with customer risk assessment. Different roles require different approaches - a compliance officer needs detailed regulatory analysis, while a relationship manager needs customer-friendly summaries. How do you create AI personas that can effectively serve these different needs while maintaining accuracy and professionalism?

### Your Mission: Becoming an AI Persona Architect

In this exercise you'll act as an AI architect, guiding the development of specialized financial AI personas for customer risk assessment. You will:

1. Start with basic prompts and observe the AI's initial responses to financial scenarios
2. Systematically develop role-based personas with **financial expertise attributes**
3. Refine **tone and communication style** to match professional requirements
4. Test the personas with realistic customer scenarios to ensure effectiveness

## Instructions

Follow these steps to complete the exercise in your development environment:

### 1. Open the Notebook
Launch the "Lesson 1: Financial AI Assistant - Customer Risk Assessment" exercise notebook.

### 2. Initial Setup
- Add your OpenAI API key to the notebook
- Review the customer data scenarios provided

### 3. Step 1: Plain Prompt Testing
- Find the section "1. Plain Prompt Testing"
- Run the code cell that sends a `control_system_prompt` ("You are a helpful financial assistant") and asks about a customer risk scenario
- Observe this initial, generic response. This is your control baseline.

### 4. Step 2: Compliance Officer Persona
- Go to section "2. Compliance Officer Persona"
- You'll see a `TODO: compliance_system_prompt = "+++++++++++"`
- **Your Task**: Replace this with a detailed role definition for a compliance officer specialized in customer risk assessment. For example: `compliance_system_prompt = "You are a Senior Compliance Officer at a major financial institution..."`
- Run this cell using the same customer scenario
- Review the AI's compliance-focused analysis and regulatory perspective

### 5. Step 3: Define Persona-Specific Expertise
- Move to section "3. Define Persona-Specific Expertise"
- You will find several `TODO` items within the `expertise_system_prompt` string, marked with `+++++++++++`
- **Your Task**: Fill in specialized expertise areas for financial risk assessment (e.g., regulatory knowledge, risk frameworks, industry experience)
- Run the cell and compare this response to previous ones, noting the enhanced technical depth

### 6. Step 4: Communication Style Refinement
- Proceed to section "4. Communication Style Refinement"
- Find the `TODO` items in the `style_system_prompt` string
- **Your Task**: Add specific communication requirements for financial professionals (tone, terminology, report structure)
- Run this cell and observe how style specifications enhance the AI's professional presentation

### 7. Step 5: Relationship Manager Persona
- Navigate to section "5. Relationship Manager Persona"
- Find the `TODO` in the `relationship_manager_prompt` for creating a customer-facing role
- **Your Task**: Create a persona for a relationship manager who needs to explain risk assessments to customers in accessible terms
- Run the cell and analyze how the same risk data is presented differently for customer communication

### 8. Step 6: Multi-Scenario Testing
- Go to section "6. Multi-Scenario Testing"
- Find multiple `TODO` placeholders for different customer risk scenarios
- **Your Task**: Test your refined personas with various customer profiles (high-risk, low-risk, complex cases)
- Run each scenario and evaluate persona consistency and effectiveness

### 9. Step 7: Reflection & Best Practices
- Go to section "7. Reflection & Best Practices"
- In the markdown cell, find the `TODO` and document your insights on which persona refinements were most effective for financial services applications and why
- Consider regulatory requirements, customer communication needs, and professional standards

## Success Criteria

By the end of this exercise, you should be able to:
- ✅ Create effective role-based prompts for financial services personas
- ✅ Develop specialized AI assistants for compliance and customer relationship roles
- ✅ Apply persona-specific expertise and communication styles appropriately
- ✅ Test and validate AI personas with realistic financial scenarios
- ✅ Understand how role-based prompting enhances AI effectiveness in financial services
- ✅ Demonstrate professional communication standards in AI-generated content

## Financial Services Context

This exercise focuses on:
- **Customer Risk Assessment**: Core financial services function requiring specialized expertise
- **Regulatory Compliance**: Essential requirement for financial AI systems
- **Professional Communication**: Different stakeholders need different communication approaches
- **Multi-Persona Architecture**: Real financial institutions need various AI assistant types

## Learning Outcomes

This hands-on practice reinforces:
- Role-based prompting principles from the lesson
- Financial services domain application
- Professional AI persona development
- Communication style adaptation for different audiences
- Quality assessment and iteration in AI system development

## Next Steps

After completing this exercise, you'll be ready to:
- Apply role-based prompting to more complex financial scenarios
- Understand how different AI personas serve different business needs
- Prepare for advanced prompting techniques in subsequent lessons
- Build sophisticated AI systems for financial services applications
