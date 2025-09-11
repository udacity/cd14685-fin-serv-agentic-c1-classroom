# Lesson 5: LLM Feedback Loops - Self-Learning Loan Agent

## Overview

This lesson teaches students how to build AI agents that learn financial approval patterns through feedback loops. Students will create a self-learning agent that discovers categorical rules about loan approval using credit level and income level, improving its decision-making through experience.

## Learning Objectives

By the end of this lesson, students will be able to:

1. **Implement Self-Correcting Agents**: Build agents that learn from both correct and incorrect decisions
2. **Design Categorical Learning Systems**: Create agents that discover patterns using categorical variables
3. **Apply Ground Truth Feedback**: Use deterministic feedback to enable precise learning
4. **Analyze Learning Progression**: Track and measure agent improvement over time
5. **Understand Real-World Applications**: Connect concepts to credit scoring and risk assessment systems

## Exercise Structure

### 📁 Files Included

1. **`lesson-5-self-learning-loan-agent-exercise.ipynb`** - Student exercise with TODO tasks (20-minute completion)
2. **`lesson-5-self-learning-loan-agent-solution.ipynb`** - Complete solution implementation

## 🎯 Exercise: Self-Learning Loan Agent

### Problem Statement

Students build a self-learning AI agent that learns to approve/deny loans based on categorical variables:
- **Credit Level**: LOW (300-599) | MEDIUM (600-749) | HIGH (750-850)
- **Income Level**: LOW (<$50K) | MEDIUM ($50K-$79K) | HIGH ($80K+)

The agent must discover the hidden ground truth rule through experience:
```
SUCCESS = (MEDIUM credit + HIGH income) OR (HIGH credit)
```

### Key Learning Mechanisms

1. **Correct Approvals**: Agent approves → Loan succeeds → Learn success pattern
2. **Wrong Approvals**: Agent approves → Loan fails → Learn failure pattern  
3. **Correct Denials**: Agent denies → Should deny → Confirm good judgment
4. **Missed Opportunities**: Agent denies → Should approve → Self-correct by learning success pattern

### Student Tasks (20-minute completion)

1. **Complete Helper Functions**: 
   - Implement `categorize_credit()` and `categorize_income()` functions
   - Implement `get_ground_truth_outcome()` rule

2. **Implement `SelfLearningLoanAgent` class**:
   - Complete `make_loan_decision()` with categorical learning
   - Complete `receive_feedback()` with all four learning scenarios
   - Implement learning state tracking and pattern analysis

3. **Complete the simulation**:
   - Run agent through loan applications with feedback loops
   - Track accuracy improvement over time
   - Analyze discovered patterns

### Performance Improvement Timeline
- **Rounds 1-3**: Random exploration phase (low accuracy)
- **Rounds 4-10**: Initial pattern recognition (improving accuracy)
- **Rounds 11-20**: Confident pattern-based decisions (high accuracy)

## 🔍 Expected Learning Outcomes

### Pattern Discovery Through Self-Learning
The agent should gradually discover through feedback loops:
- **HIGH credit** always leads to success regardless of income
- **MEDIUM credit** only succeeds with HIGH income
- **LOW credit** never succeeds regardless of income

### Self-Learning Progression
- **Early decisions**: Random exploration to gather data
- **Middle decisions**: Pattern recognition begins emerging
- **Later decisions**: Confident categorical-based decisions
- **Self-correction**: Missed opportunities become learned success patterns

### Real-World Connection
Students understand how self-learning applies to:
- Credit scoring models that adapt to new data
- Risk assessment systems that improve over time
- Recommendation engines that learn user preferences
- Any AI system that discovers decision boundaries through experience

## 💡 Key Insights for Students

1. **Self-Learning Process**: Agents can discover hidden rules through experience rather than programming
2. **Categorical Variables**: Discrete categories can reveal clearer patterns than continuous variables
3. **Feedback Loop Importance**: Each decision becomes training data for future decisions
4. **Ground Truth Learning**: Deterministic feedback enables precise pattern discovery
5. **Self-Correction Capability**: Learning from missed opportunities is crucial for improvement

## 🚀 Extension Ideas

1. **Add Third Variable**: Include employment length or debt-to-income ratio
2. **Probabilistic Feedback**: Replace deterministic outcomes with probability-based results
3. **Dynamic Rules**: Change the ground truth rule mid-simulation to test adaptability
4. **Confidence Scoring**: Add agent confidence levels to decisions
5. **Explainable AI**: Generate explanations for why certain patterns work
6. **Performance Comparison**: Compare self-learning agent vs static rule-based agent

## Prerequisites

- OpenAI API key configured
- Understanding of basic prompt engineering
- Familiarity with Python dictionaries and loops
- Basic knowledge of financial lending concepts

## Time Investment

- **Student Exercise**: 20 minutes to complete TODO sections
- **Solution Review**: 10 minutes to understand complete implementation
- **Extension Activities**: 15+ minutes for creative modifications

This exercise provides hands-on experience with self-learning AI agents and demonstrates core concepts that apply to real financial AI systems that improve through experience.
