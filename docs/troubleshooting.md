# 🔧 Troubleshooting Guide

This guide helps you resolve common issues with AI Tutor. Most problems have simple solutions!

## Quick Diagnosis

### 🚨 Emergency Checklist
Before diving into specific issues, verify these basics:

- [ ] Ollama is installed and running
- [ ] At least one AI model is downloaded
- [ ] Python dependencies are installed
- [ ] Port 8501 and 11434 are not blocked
- [ ] Sufficient system resources (RAM/Storage)

## Common Issues and Solutions

### 1. "No Ollama models found"

#### Symptoms
- Error message in sidebar: "⚠️ No Ollama models found"
- Model dropdown is empty
- Cannot start conversations

#### Diagnosis
Check if Ollama is running and models are installed:
```bash
# Check if Ollama is running
ollama list

# If command fails, Ollama isn't running
ollama serve
```

#### Solutions

**Solution A: Install Models**
```bash
# Install recommended model
ollama pull gemma3

# Verify installation
ollama list
```

**Solution B: Restart Ollama**
```bash
# Stop Ollama (if running)
pkill ollama

# Start Ollama
ollama serve

# In new terminal, test
ollama list
```

**Solution C: Check Ollama Installation**
```bash
# Reinstall Ollama (if needed)
# Windows: Download from ollama.ai
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. Connection Errors

#### Symptoms
- "Error connecting to Ollama"
- "Connection refused" messages
- App hangs when starting conversation

#### Diagnosis
```bash
# Test Ollama connection
curl http://localhost:11434/api/version

# Check if port is in use
netstat -an | grep 11434
```

#### Solutions

**Solution A: Port Conflict**
```bash
# Find process using port 11434
lsof -i :11434  # macOS/Linux
netstat -ano | findstr :11434  # Windows

# Kill conflicting process and restart Ollama
ollama serve
```

**Solution B: Firewall Issues**
- **Windows**: Allow Ollama through Windows Defender
- **macOS**: System Preferences → Security → Allow Ollama
- **Linux**: Configure iptables or ufw to allow port 11434

**Solution C: Service Issues**
```bash
# Restart Ollama service
# Windows: Restart from Services (services.msc)
# macOS: brew services restart ollama
# Linux: systemctl restart ollama
```

### 3. Model Performance Issues

#### Symptoms
- Very slow responses
- App becomes unresponsive
- High CPU/RAM usage

#### Diagnosis
Check system resources:
```bash
# Check RAM usage
free -h  # Linux
top  # macOS/Linux
taskmgr  # Windows

# Check available models and their sizes
ollama list
```

#### Solutions

**Solution A: Use Smaller Models**
```bash
# Remove large models
ollama rm llama3

# Install smaller alternatives
ollama pull gemma2:2b
ollama pull deepseek-coder
```

**Solution B: Optimize System**
- Close unnecessary applications
- Increase virtual memory/swap
- Use SSD for better I/O performance

**Solution C: Adjust Model Settings**
```python
# In app.py, modify the generate call
response = ollama.generate(
    model=model_name,
    prompt=custom_prompt,
    stream=True,
    options={
        'num_ctx': 2048,  # Reduce context window
        'temperature': 0.7,  # Adjust creativity
    }
)
```

### 4. Streamlit Issues

#### Symptoms
- "Streamlit command not found"
- App won't start
- Browser doesn't open automatically

#### Diagnosis
```bash
# Check Streamlit installation
pip list | grep streamlit

# Test Streamlit
streamlit hello
```

#### Solutions

**Solution A: Reinstall Dependencies**
```bash
# Activate virtual environment
source ai-tutor-env/bin/activate  # macOS/Linux
ai-tutor-env\Scripts\activate  # Windows

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

**Solution B: Python Path Issues**
```bash
# Check Python installation
which python  # macOS/Linux
where python  # Windows

# Use full path if needed
/usr/bin/python -m streamlit run app.py
```

**Solution C: Port Conflicts**
```bash
# Use different port
streamlit run app.py --server.port 8502

# Or specify in config
mkdir -p ~/.streamlit
echo "[server]" > ~/.streamlit/config.toml
echo "port = 8502" >> ~/.streamlit/config.toml
```

### 5. Model Loading Errors

#### Symptoms
- "Model not found" errors
- Specific model won't work
- Model switches unexpectedly

#### Diagnosis
```bash
# Check exact model names
ollama list

# Test specific model
ollama run gemma3 "Hello, how are you?"
```

#### Solutions

**Solution A: Model Name Mismatch**
```python
# Check model names in app.py
# Ensure they match exactly with `ollama list` output
preferred_order = ['gemma3:latest', 'deepseek-coder:latest']
```

**Solution B: Corrupted Model**
```bash
# Remove and reinstall model
ollama rm gemma3
ollama pull gemma3
```

**Solution C: Version Conflicts**
```bash
# Update Ollama
# Windows: Download latest from ollama.ai
# macOS: brew upgrade ollama
# Linux: curl -fsSL https://ollama.ai/install.sh | sh
```

### 6. UI and Display Issues

#### Symptoms
- Broken layout
- Missing sidebar
- Text formatting issues

#### Solutions

**Solution A: Browser Cache**
- Clear browser cache and cookies
- Try incognito/private mode
- Use different browser

**Solution B: Streamlit Cache**
```bash
# Clear Streamlit cache
streamlit cache clear
```

**Solution C: Browser Compatibility**
- Use Chrome, Firefox, or Safari
- Ensure JavaScript is enabled
- Disable browser extensions that might interfere

### 7. Memory and Resource Issues

#### Symptoms
- Out of memory errors
- System becomes sluggish
- App crashes randomly

#### Diagnosis
```bash
# Check system resources
htop  # Linux
Activity Monitor  # macOS
Task Manager  # Windows
```

#### Solutions

**Solution A: Increase Virtual Memory**
- **Windows**: Settings → System → About → Advanced system settings → Performance → Advanced → Virtual memory
- **macOS**: No manual swap configuration needed
- **Linux**: Create swap file or increase existing swap

**Solution B: Model Management**
```bash
# Remove unused models
ollama list
ollama rm unused-model-name

# Use lightweight models
ollama pull gemma2:2b  # Only 1.4GB
```

**Solution C: System Optimization**
- Close unnecessary applications
- Restart system to clear memory
- Use task manager to kill memory-heavy processes

## Platform-Specific Issues

### Windows

#### Common Issues
- PowerShell execution policy
- Windows Defender false positives
- Path length limitations

#### Solutions
```powershell
# Fix execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Add Windows Defender exclusion for Ollama
Add-MpPreference -ExclusionPath "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama"
```

### macOS

#### Common Issues
- Gatekeeper blocking Ollama
- Apple Silicon compatibility
- Permission issues

#### Solutions
```bash
# Allow Ollama in System Preferences
# System Preferences → Security & Privacy → General → Allow apps downloaded from: App Store and identified developers

# For Apple Silicon, ensure native version
arch -arm64 ollama serve
```

### Linux

#### Common Issues
- Missing dependencies
- Service management
- File permissions

#### Solutions
```bash
# Install missing dependencies
sudo apt update
sudo apt install curl build-essential

# Fix permissions
sudo chown -R $USER:$USER ~/.ollama
chmod +x ~/.local/bin/ollama
```

## Advanced Troubleshooting

### Debug Mode

Enable debug logging to get more information:

1. **Add debug to app.py:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

2. **Run with verbose output:**
```bash
streamlit run app.py --logger.level debug
```

### Log Analysis

#### Ollama Logs
```bash
# Find Ollama logs
# Windows: %USERPROFILE%\.ollama\logs
# macOS: ~/.ollama/logs
# Linux: ~/.ollama/logs

# View recent logs
tail -f ~/.ollama/logs/server.log
```

#### Streamlit Logs
```bash
# Streamlit outputs logs to terminal
# Look for error messages and stack traces
streamlit run app.py 2>&1 | tee debug.log
```

### Network Debugging

#### Test API Endpoints
```bash
# Test Ollama API
curl http://localhost:11434/api/tags
curl -X POST http://localhost:11434/api/generate -d '{"model":"gemma3","prompt":"Hello"}'

# Test with different hosts
curl http://127.0.0.1:11434/api/tags
```

#### Proxy Issues
If behind corporate firewall:
```bash
# Set proxy for pip
pip install --proxy http://proxy.company.com:8080 -r requirements.txt

# Set environment variables
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
```

## Getting Additional Help

### 1. Gather Information
Before seeking help, collect:
- Operating system and version
- Python version (`python --version`)
- Ollama version (`ollama --version`)
- Error messages (exact text)
- Steps to reproduce the issue

### 2. Check Resources
- [Ollama Documentation](https://ollama.ai/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [GitHub Issues](https://github.com/hari7261/AI-Tutor/issues)

### 3. Report Issues
When reporting bugs:
- Use the issue template
- Include system information
- Provide error logs
- Describe expected vs actual behavior

### 4. Community Support
- [GitHub Discussions](https://github.com/hari7261/AI-Tutor/discussions)
- Stack Overflow (tag: ai-tutor)
- Reddit communities

## Maintenance Tips

### Regular Maintenance
```bash
# Update models monthly
ollama pull gemma3

# Clear old cache
streamlit cache clear

# Update dependencies
pip install -r requirements.txt --upgrade
```

### Performance Monitoring
- Monitor system resources regularly
- Keep logs for pattern analysis
- Update software components

---

## Still Having Issues?

If none of these solutions work:

1. **Create a minimal test case**
2. **Check the FAQ** in discussions
3. **Open a GitHub issue** with full details
4. **Join the community** for real-time help

Remember: Most issues are simple configuration problems that can be solved quickly! 🔧
