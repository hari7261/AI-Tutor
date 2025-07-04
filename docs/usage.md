# 📚 Usage Guide

Learn how to effectively use AI Tutor to enhance your learning experience. This guide covers all features and provides practical examples.

## Getting Started

### 1. Launch the Application
```bash
cd AI-Tutor
streamlit run app.py
```

### 2. Configure Your Preferences
The sidebar contains all your learning preferences:

#### Education Level
- **School** (Ages 6-14): Simple explanations, basic vocabulary
- **High School** (Ages 14-18): Moderate complexity, exam preparation
- **Graduate** (Ages 18-22): Advanced concepts, research-oriented
- **PG/PhD** (Ages 22+): Expert-level explanations, cutting-edge topics

#### Subject Selection
- **Math**: Algebra, calculus, statistics, geometry
- **History**: World history, regional studies, historical analysis
- **Computer Science**: Programming, algorithms, data structures
- **Physics**: Mechanics, thermodynamics, quantum physics
- **Biology**: Cell biology, genetics, ecology, anatomy
- **Chemistry**: Organic, inorganic, physical chemistry

#### Learning Mode
- **Explain a Topic**: Get detailed explanations
- **Generate a Quiz**: Create practice questions

## Feature Deep Dive

### 🎯 Explanation Mode

Perfect for understanding new concepts or getting clarification on difficult topics.

#### Example Queries

**Math - High School Level:**
```
Input: "Explain quadratic equations"
Output: Step-by-step breakdown including:
- Definition and standard form
- Methods of solving (factoring, quadratic formula)
- Real-world applications
- Practice examples
```

**Computer Science - Graduate Level:**
```
Input: "Explain machine learning algorithms"
Output: Comprehensive coverage including:
- Types of ML algorithms
- Mathematical foundations
- Implementation considerations
- Use cases and limitations
```

**Physics - School Level:**
```
Input: "How does gravity work?"
Output: Simple explanation with:
- Basic concept of gravity
- Everyday examples
- Fun facts and demonstrations
```

#### Best Practices for Explanations
- **Be Specific**: "Explain photosynthesis in plants" vs "Tell me about plants"
- **Ask Follow-ups**: Build on previous explanations
- **Request Examples**: "Can you give me real-world examples?"
- **Seek Clarification**: "Can you explain that part about..."

### 🧩 Quiz Mode

Ideal for testing your knowledge and exam preparation.

#### Example Quiz Generations

**History - High School:**
```
Input: "World War 2"
Output: Multiple-choice question with:
- Clear question about WW2
- 4 realistic options (A, B, C, D)
- Correct answer marked [CORRECT]
- Detailed explanation of the answer
```

**Math - Graduate Level:**
```
Input: "Calculus derivatives"
Output: Problem-solving question with:
- Mathematical problem
- Multiple solution approaches
- Step-by-step solution
- Common mistake warnings
```

#### Quiz Generation Tips
- **Topic Specificity**: "Mitochondrial function" vs "Biology"
- **Difficulty Adjustment**: The AI adapts to your education level
- **Practice Sessions**: Generate multiple quizzes on the same topic
- **Review Mode**: Ask for explanations of quiz answers

## Advanced Usage Patterns

### 1. Progressive Learning
Start with broad topics and drill down:
```
Session 1: "Explain machine learning"
Session 2: "Tell me more about neural networks"
Session 3: "How do convolutional neural networks work?"
Session 4: "Quiz me on CNN architecture"
```

### 2. Exam Preparation
Combine explanations and quizzes:
```
Week 1: Explanation mode for all topics
Week 2: Quiz mode for weak areas
Week 3: Mixed review with both modes
```

### 3. Project-Based Learning
Use for real-world applications:
```
"Explain how to build a simple web application"
"What are the steps in data analysis?"
"How do I design a science experiment?"
```

## Model Selection Guide

### 🧠 Gemma3 (Recommended)
- **Best for**: General education, explanations
- **Strengths**: Clear explanations, good examples
- **Size**: 3.3GB
- **Use when**: Learning any subject comprehensively

### 💻 DeepSeek Coder
- **Best for**: Computer Science, Programming
- **Strengths**: Code examples, technical accuracy
- **Size**: 776MB
- **Use when**: Learning programming or CS concepts

### 🚀 Llama3
- **Best for**: Alternative general-purpose model
- **Strengths**: Balanced performance
- **Size**: 4.7GB
- **Use when**: Gemma3 isn't available

## Learning Strategies

### 📖 For Students

#### Daily Study Routine
1. **Morning Review** (15 mins)
   - Quiz mode on previous day's topics
   - Identify weak areas

2. **Learning Session** (45 mins)
   - Explanation mode for new concepts
   - Take notes on key points

3. **Practice Session** (30 mins)
   - Quiz mode on new topics
   - Review incorrect answers

#### Exam Preparation
1. **Topic Mapping** (Week 1)
   - List all exam topics
   - Get explanations for each

2. **Intensive Practice** (Week 2-3)
   - Daily quizzes on all topics
   - Focus on weak areas

3. **Final Review** (Week 4)
   - Mixed quizzes
   - Quick explanation refreshers

### 🎓 For Educators

#### Lesson Planning
- Generate quiz questions for class
- Get different explanation approaches
- Create homework problems

#### Student Support
- Provide personalized explanations
- Generate practice materials
- Offer different difficulty levels

## Tips for Effective Learning

### 📝 Note-Taking Integration
- Copy important explanations to your notes
- Screenshot quiz questions for review
- Create summary documents

### 🔄 Iterative Learning
- Ask follow-up questions for clarity
- Request alternative explanations
- Seek connections between topics

### 🎯 Goal-Oriented Sessions
- Set specific learning objectives
- Track your progress mentally
- Review and reflect on sessions

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Focus chat input | `Ctrl + L` |
| Submit message | `Enter` |
| New line in input | `Shift + Enter` |
| Clear chat | Refresh page |

## Privacy and Data

### What Stays Local
- ✅ All your questions and conversations
- ✅ AI model responses
- ✅ Learning preferences and history
- ✅ Generated quizzes and explanations

### What Never Leaves Your Device
- ❌ Personal information
- ❌ Study materials
- ❌ Conversation history
- ❌ Usage patterns

## Common Use Cases

### 📚 Homework Help
```
"Explain how to solve this physics problem: [paste problem]"
"What are the key themes in Romeo and Juliet?"
"How do I write a good research paper?"
```

### 🧪 Research Projects
```
"What are the latest developments in renewable energy?"
"Explain the methodology for statistical analysis"
"How do I design an experiment for [topic]?"
```

### 📊 Test Preparation
```
"Generate SAT math practice questions"
"Quiz me on AP Biology topics"
"Create GRE verbal reasoning problems"
```

### 💼 Professional Development
```
"Explain modern software development practices"
"What are the principles of project management?"
"How does financial analysis work?"
```

## Troubleshooting Usage Issues

### AI Responses Are Too Simple/Complex
- **Solution**: Adjust your education level setting
- **Tip**: Try different levels to find your sweet spot

### Quiz Questions Are Too Easy/Hard
- **Solution**: Change education level or be more specific
- **Example**: "Graduate-level organic chemistry quiz"

### Explanations Lack Detail
- **Solution**: Ask follow-up questions
- **Example**: "Can you explain that in more detail?"

### Model Responses Are Slow
- **Solution**: Switch to a smaller model
- **Alternative**: Close other applications to free up RAM

---

Ready to start learning? Try asking your first question! 🚀
