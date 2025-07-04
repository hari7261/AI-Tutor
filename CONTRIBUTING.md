# 🤝 Contributing to AI Tutor

Thank you for your interest in contributing to AI Tutor! This guide will help you get started with contributing to the project.

## 🚀 Quick Start for Contributors

### 1. Fork and Clone
```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/AI-Tutor.git
cd AI-Tutor

# Add upstream remote
git remote add upstream https://github.com/hari7261/AI-Tutor.git
```

### 2. Set Up Development Environment
```bash
# Create virtual environment
python -m venv ai-tutor-dev
source ai-tutor-dev/bin/activate  # macOS/Linux
ai-tutor-dev\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 3. Create a Branch
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or bug fix branch
git checkout -b fix/issue-number
```

## 📋 Types of Contributions

### 🐛 Bug Reports
Found a bug? Help us fix it!

**Before reporting:**
- Check existing issues
- Test with latest version
- Gather system information

**Include in your report:**
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version, etc.)
- Error messages and logs

### 💡 Feature Requests
Have an idea for improvement?

**Before requesting:**
- Check existing feature requests
- Consider if it fits the project scope
- Think about implementation complexity

**Include in your request:**
- Clear description of the feature
- Use cases and benefits
- Possible implementation approach
- Mockups or examples (if applicable)

### 📖 Documentation
Documentation improvements are always welcome!

**Areas to contribute:**
- Fix typos and grammar
- Add missing information
- Improve clarity and examples
- Translate to other languages
- Add video tutorials or guides

### 🧪 Code Contributions
Ready to code? Here's what we need:

**Priority areas:**
- Bug fixes
- Performance improvements
- New AI model integrations
- UI/UX enhancements
- Test coverage improvements

## 🛠️ Development Guidelines

### Code Style
We follow Python PEP 8 with some modifications:

```python
# Use type hints
def get_models() -> List[str]:
    return ["model1", "model2"]

# Clear variable names
available_models = get_available_models()
selected_model = st.selectbox("Model", available_models)

# Docstrings for functions
def format_prompt(education_level: str, subject: str, prompt: str) -> str:
    """
    Format a prompt for the AI model based on education level and subject.
    
    Args:
        education_level: The student's education level
        subject: The subject area for the prompt
        prompt: The user's input prompt
        
    Returns:
        Formatted prompt string for the AI model
    """
    pass
```

### File Structure
```
AI-Tutor/
├── app.py                    # Main application
├── components/               # Reusable UI components
│   ├── __init__.py
│   ├── sidebar.py           # Sidebar configuration
│   ├── chat.py              # Chat interface
│   └── models.py            # Model selection
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── prompts.py           # Prompt formatting
│   ├── models.py            # Model management
│   └── config.py            # Configuration loading
├── tests/                   # Test files
└── docs/                    # Documentation
```

### Testing
We aim for high test coverage:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run integration tests
pytest -m integration
```

**Test requirements:**
- Unit tests for new functions
- Integration tests for new features
- Mock external dependencies (Ollama)
- Test edge cases and error conditions

### Git Workflow

#### Commit Messages
Use conventional commit format:
```
type(scope): description

body (optional)

footer (optional)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(models): add support for llama3 model

fix(ui): resolve sidebar layout issue on mobile

docs(readme): update installation instructions

test(models): add unit tests for model detection
```

#### Pull Request Process

1. **Before submitting:**
   - Sync with upstream: `git pull upstream main`
   - Run tests: `pytest`
   - Check code style: `flake8 .`
   - Update documentation if needed

2. **PR Requirements:**
   - Clear title and description
   - Reference related issues
   - Include screenshots for UI changes
   - Add tests for new functionality
   - Update documentation

3. **PR Template:**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Performance improvement
   
   ## Testing
   - [ ] Tests pass locally
   - [ ] Added new tests
   - [ ] Manual testing completed
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] No breaking changes
   ```

## 🧩 Specific Contribution Areas

### Adding New AI Models

1. **Model Integration:**
```python
# In utils/models.py
SUPPORTED_MODELS = {
    'new-model': {
        'name': 'New Model',
        'size': '2GB',
        'best_for': ['General'],
        'install_command': 'ollama pull new-model'
    }
}
```

2. **Update Configuration:**
```yaml
# In config/models.yaml
preferred_models:
  - "new-model:latest"
```

3. **Add Tests:**
```python
def test_new_model_detection():
    # Test model detection logic
    pass
```

### UI/UX Improvements

1. **Component Structure:**
```python
# components/new_component.py
import streamlit as st

def render_new_component():
    """Render a new UI component."""
    with st.container():
        # Component implementation
        pass
```

2. **Styling:**
```python
# Use Streamlit's built-in styling
st.markdown("""
<style>
    .custom-component {
        /* Custom styles */
    }
</style>
""", unsafe_allow_html=True)
```

### Performance Improvements

1. **Caching:**
```python
@st.cache_data
def expensive_operation():
    # Cache expensive operations
    pass
```

2. **Async Operations:**
```python
import asyncio

async def async_model_call():
    # Async model calls for better performance
    pass
```

### Documentation Improvements

1. **Code Documentation:**
   - Add docstrings to all functions
   - Include type hints
   - Add inline comments for complex logic

2. **User Documentation:**
   - Update README for new features
   - Add examples and tutorials
   - Create troubleshooting guides

## 🎯 Development Setup Details

### Required Tools
- Python 3.7+
- Git
- Ollama (for testing)
- Code editor (VS Code recommended)

### Development Dependencies
```bash
# requirements-dev.txt
pytest>=7.0.0
pytest-cov>=4.0.0
flake8>=5.0.0
black>=22.0.0
mypy>=0.991
pre-commit>=2.20.0
streamlit>=1.28.0
ollama>=0.1.7
```

### IDE Configuration

#### VS Code Settings
```json
{
    "python.defaultInterpreterPath": "./ai-tutor-dev/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

#### Pre-commit Configuration
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 5.0.4
    hooks:
      - id: flake8
```

## 🔍 Code Review Process

### For Contributors
- Respond to feedback promptly
- Make requested changes
- Keep PRs focused and small
- Write clear commit messages

### For Reviewers
- Be respectful and constructive
- Focus on code quality and maintainability
- Test changes locally when possible
- Approve when ready for merge

## 🏆 Recognition

Contributors will be recognized in:
- README contributors section
- Release notes
- Special thanks in documentation

## 📞 Getting Help

### Development Questions
- GitHub Discussions
- Issue comments
- Discord/Slack (if available)

### Mentorship
New contributors can request mentorship for:
- First-time contributions
- Complex features
- Best practices guidance

## 🎉 Thank You!

Every contribution helps make AI Tutor better for learners everywhere. Whether it's a bug report, feature suggestion, or code contribution, your help is appreciated!

---

**Ready to contribute?** Start by checking our [Good First Issues](https://github.com/hari7261/AI-Tutor/labels/good%20first%20issue) label!
