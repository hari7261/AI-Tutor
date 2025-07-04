# 🛠️ Installation Guide

This guide provides detailed installation instructions for the AI Tutor application across different operating systems.

## System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **RAM**: 8GB (16GB recommended for optimal performance)
- **Storage**: 10GB free space (for models and dependencies)
- **Python**: 3.7 or higher

### Recommended Requirements
- **RAM**: 16GB or higher
- **Storage**: 20GB+ SSD for faster model loading
- **GPU**: Optional, but improves performance with compatible models

## Installation Steps

### 1. Install Python

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and check "Add Python to PATH"
3. Verify installation: `python --version`

#### macOS
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Install Ollama

#### Windows
1. Download from [ollama.ai](https://ollama.ai/download)
2. Run the installer
3. Ollama will start automatically

#### macOS
```bash
# Using Homebrew
brew install ollama

# Or download from ollama.ai
```

#### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 3. Clone and Setup AI Tutor

```bash
# Clone the repository
git clone https://github.com/hari7261/AI-Tutor.git
cd AI-Tutor

# Create virtual environment (recommended)
python -m venv ai-tutor-env

# Activate virtual environment
# Windows:
ai-tutor-env\Scripts\activate
# macOS/Linux:
source ai-tutor-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Install AI Models

#### Quick Setup (Recommended)
```bash
# Install Gemma3 (best for education)
ollama pull gemma3

# Start Ollama (if not running)
ollama serve
```

#### Advanced Setup
```bash
# For programming and computer science
ollama pull deepseek-coder

# Alternative general model
ollama pull llama3

# Lightweight option for slower systems
ollama pull gemma2:2b
```

### 5. Verify Installation

```bash
# Check Ollama is running
ollama list

# Start the application
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`

## Platform-Specific Notes

### Windows
- **Windows Defender**: May flag Ollama during installation - add exception
- **PowerShell**: Use PowerShell or Command Prompt for commands
- **Path Issues**: Ensure Python and pip are in your PATH

### macOS
- **Apple Silicon**: Ollama has native M1/M2 support
- **Xcode**: May need Command Line Tools: `xcode-select --install`
- **Permissions**: Allow Ollama in Security & Privacy settings

### Linux
- **Dependencies**: Install build essentials: `sudo apt install build-essential`
- **NVIDIA GPU**: Install CUDA for GPU acceleration (optional)
- **Firewall**: Ensure port 11434 is accessible for Ollama

## Docker Installation (Alternative)

### Prerequisites
- Docker installed and running
- Docker Compose (optional but recommended)

### Using Docker Compose

1. Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    
  ai-tutor:
    build: .
    ports:
      - "8501:8501"
    depends_on:
      - ollama
    environment:
      - OLLAMA_HOST=ollama:11434

volumes:
  ollama_data:
```

2. Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

3. Run with Docker Compose:
```bash
docker-compose up -d
```

## Troubleshooting Installation

### Common Issues

#### "Python not found"
- **Windows**: Reinstall Python with "Add to PATH" checked
- **macOS/Linux**: Use `python3` instead of `python`

#### "pip not found"
- Install pip: `python -m ensurepip --upgrade`
- Or use: `python -m pip` instead of `pip`

#### "Ollama connection failed"
- Check if Ollama is running: `ollama list`
- Restart Ollama: `ollama serve`
- Check port 11434 is not blocked

#### "Model not found"
- Verify model installation: `ollama list`
- Reinstall model: `ollama pull gemma3`
- Check available models: `ollama list`

#### Memory issues
- Use smaller models: `ollama pull gemma2:2b`
- Close other applications
- Increase virtual memory/swap

### Performance Optimization

#### For Better Speed
1. Use SSD storage for model files
2. Increase system RAM
3. Use smaller models for faster response
4. Close unnecessary applications

#### For Better Quality
1. Use larger models (gemma3, llama3)
2. Ensure adequate RAM (16GB+)
3. Use GPU acceleration if available

## Next Steps

After successful installation:

1. **Read the Usage Guide**: [docs/usage.md](usage.md)
2. **Try Example Queries**: Start with simple questions
3. **Customize Settings**: Adjust education level and subjects
4. **Explore Features**: Try both explanation and quiz modes

## Getting Help

If you encounter issues during installation:

1. **Check Troubleshooting**: [docs/troubleshooting.md](troubleshooting.md)
2. **GitHub Issues**: [Report a bug](https://github.com/hari7261/AI-Tutor/issues)
3. **Discussions**: [Community help](https://github.com/hari7261/AI-Tutor/discussions)

---

**Success!** 🎉 You should now have AI Tutor running locally on your machine.
