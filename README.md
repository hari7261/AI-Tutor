# 🎓 AI Tutor - Local AI Study Buddy

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Compatible-green.svg)](https://ollama.ai/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A powerful, privacy-focused AI tutoring application that runs entirely on your local machine. Get personalized explanations and generate custom quizzes across multiple subjects without sending any data to external servers.

![AI Tutor Demo](/image.png)

## ✨ Features

### 🎯 **Personalized Learning**
- **Multiple Education Levels**: School, High School, Graduate, PG/PhD
- **Subject Variety**: Math, History, Computer Science, Physics, Biology, Chemistry
- **Adaptive Explanations**: Content complexity adjusts to your education level

### 🤖 **Dual Learning Modes**
- **Explain a Topic**: Get detailed, step-by-step explanations with examples
- **Generate a Quiz**: Create custom multiple-choice questions with explanations

### 🔒 **100% Privacy**
- **Local Processing**: All AI computations happen on your device
- **No Data Transfer**: Your questions and conversations never leave your machine
- **Offline Capable**: Works without internet once models are downloaded

### 🧠 **Multiple AI Models**
- **Gemma3**: Google's latest model, optimized for educational content
- **DeepSeek Coder**: Specialized for programming and computer science
- **Llama3**: Meta's powerful general-purpose model
- **Auto-Detection**: Automatically discovers installed Ollama models

## 🚀 Quick Start

### Prerequisites

1. **Python 3.7+** installed on your system
2. **Ollama** installed and running ([Download Ollama](https://ollama.ai/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hari7261/AI-Tutor.git
   cd AI-Tutor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install AI models** (choose one or more)
   ```bash
   # Recommended: Gemma3 (best for general education)
   ollama pull gemma3
   
   # For coding and computer science
   ollama pull deepseek-coder
   
   # Alternative general-purpose model
   ollama pull llama3
   ```

4. **Start Ollama server** (if not already running)
   ```bash
   ollama serve
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser** and navigate to `http://localhost:8501`

## 🎮 How to Use

### 1. Configure Your Learning Preferences
- **Education Level**: Select your current academic level
- **Subject**: Choose the subject you want to study
- **Mode**: Pick between explanation or quiz generation
- **AI Model**: The app will automatically detect and list available models

### 2. Ask Questions or Request Topics
- **Explanation Mode**: "Explain photosynthesis" or "How does machine learning work?"
- **Quiz Mode**: "Create a quiz about World War 2" or "Test me on calculus derivatives"

### 3. Interactive Learning
- Get detailed explanations with examples
- Receive custom quizzes with immediate feedback
- Build on previous conversations for deeper understanding

## 📁 Project Structure

```
AI-Tutor/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore           # Git ignore rules
├── assets/              # Images and media
│   └── demo.gif         # Application demo
├── docs/                # Additional documentation
│   ├── installation.md  # Detailed installation guide
│   ├── usage.md         # Usage examples and tips
│   └── troubleshooting.md # Common issues and solutions
├── config/              # Configuration files
│   └── models.yaml      # Model configuration
└── tests/               # Test files
    └── test_app.py      # Unit tests
```

## 🧩 Core Modules

### 1. **Model Detection (`get_available_models()`)**
- Automatically discovers installed Ollama models
- Handles different API response formats
- Prioritizes models based on educational performance
- Provides fallback options and error handling

### 2. **Education Level Adaptation**
- Adjusts explanation complexity based on selected level
- Customizes vocabulary and examples
- Scales problem difficulty appropriately

### 3. **Subject-Specific Prompting**
- Tailors AI responses to subject context
- Incorporates subject-specific terminology
- Provides relevant examples and analogies

### 4. **Streaming Response Handler**
- Real-time response display for better user experience
- Handles connection errors gracefully
- Provides visual feedback during generation

### 5. **Session Management**
- Maintains conversation history
- Preserves context across interactions
- Enables follow-up questions and clarifications

## 🔧 Configuration

### Model Priority
The application prioritizes models in the following order:
1. `gemma3:latest` - Best for general education
2. `deepseek-coder` - Optimal for programming topics
3. `llama3` - Reliable general-purpose alternative

### Custom Model Configuration
Edit `config/models.yaml` to customize model preferences:

```yaml
models:
  preferred_order:
    - "gemma3:latest"
    - "deepseek-coder"
    - "llama3"
  
  subject_recommendations:
    "Computer Science": "deepseek-coder"
    "Math": "gemma3"
    "Physics": "gemma3"
```

## 🛠️ Development

### Setting up Development Environment

1. **Fork the repository**
2. **Create a virtual environment**
   ```bash
   python -m venv ai-tutor-env
   source ai-tutor-env/bin/activate  # On Windows: ai-tutor-env\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Run tests**
   ```bash
   pytest tests/
   ```

### Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes
- Maintain test coverage above 80%

## 🐛 Troubleshooting

### Common Issues

**"No Ollama models found"**
- Ensure Ollama is running: `ollama serve`
- Check installed models: `ollama list`
- Install a model: `ollama pull gemma3`

**Connection errors**
- Verify Ollama is accessible on default port (11434)
- Check firewall settings
- Restart Ollama service

**Performance issues**
- Use smaller models for better speed
- Ensure sufficient RAM (8GB+ recommended)
- Close unnecessary applications

See [docs/troubleshooting.md](docs/troubleshooting.md) for detailed solutions.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📖 Improve documentation
- 🧪 Add test cases
- 🎨 Enhance UI/UX

## 📊 Performance Metrics

| Model | Size | Speed | Education Quality |
|-------|------|-------|------------------|
| Gemma3 | 3.3GB | Fast | ⭐⭐⭐⭐⭐ |
| DeepSeek Coder | 776MB | Very Fast | ⭐⭐⭐⭐ (CS Topics) |
| Llama3 | 4.7GB | Medium | ⭐⭐⭐⭐ |

## 🗺️ Roadmap

- [ ] **Multi-language Support** - Add support for multiple languages
- [ ] **Voice Integration** - Voice-to-text and text-to-voice
- [ ] **Progress Tracking** - Learning progress and analytics
- [ ] **Study Plans** - Automated curriculum generation
- [ ] **Collaborative Learning** - Share sessions with classmates
- [ ] **Mobile App** - Native mobile applications

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for providing the local AI infrastructure
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Google](https://ai.google.dev/) for the Gemma model family
- [DeepSeek](https://deepseek.com/) for the specialized coding model

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/hari7261/AI-Tutor/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/hari7261/AI-Tutor/discussions)
- 📧 **Email**: [Contact Us](mailto:your-email@example.com)

---

<div align="center">
  <p>Made with ❤️ for learners everywhere</p>
  <p>⭐ Star this repo if you find it helpful!</p>
</div>
