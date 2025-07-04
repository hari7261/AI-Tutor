"""
AI Tutor - Local AI Study Buddy

A privacy-focused AI tutoring application that runs entirely on your local machine.
Provides personalized explanations and generates custom quizzes across multiple subjects.

Author: Hariom Kumar
License: MIT
Repository: https://github.com/hari7261/AI-Tutor
"""

import streamlit as st
import ollama
import random
from typing import List, Optional
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to get available models
@st.cache_data
def get_available_models():
    try:
        models_response = ollama.list()
        model_names = []
        
        # Handle the ListResponse object from ollama
        if hasattr(models_response, 'models'):
            for model in models_response.models:
                # Each model has a 'model' attribute with the name
                if hasattr(model, 'model'):
                    model_names.append(model.model)
                elif isinstance(model, dict):
                    # Fallback for dict format
                    name = model.get('name') or model.get('model') or model.get('id')
                    if name:
                        model_names.append(name)
                elif isinstance(model, str):
                    model_names.append(model)
        elif isinstance(models_response, dict) and 'models' in models_response:
            # Fallback for older API format
            for model in models_response['models']:
                if isinstance(model, dict):
                    name = model.get('name') or model.get('model') or model.get('id')
                    if name:
                        model_names.append(name)
                elif isinstance(model, str):
                    model_names.append(model)
        
        # Prioritize models - check for exact matches and partial matches
        preferred_order = ['gemma3:latest', 'gemma3', 'gemma2:2b', 'gemma2', 'llama3', 'mistral', 'deepseek-coder']
        ordered_models = []
        
        # First, add exact matches from preferred list
        for preferred in preferred_order:
            if preferred in model_names:
                ordered_models.append(preferred)
        
        # Then add any other models not in preferred list
        for model in model_names:
            if model not in ordered_models:
                ordered_models.append(model)
                
        return ordered_models
    except Exception as e:
        # Show more detailed error for debugging
        st.error(f"Error connecting to Ollama: {str(e)}")
        st.info("Make sure Ollama is running: `ollama serve`")
        return []

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# App title
st.title("🎓 Local AI Study Buddy")

# Sidebar for settings
with st.sidebar:
    st.header("🎯 Learning Preferences")
    
    # Education level dropdown
    education_level = st.selectbox(
        "Select your education level",
        ["School", "High School", "Graduate", "PG/PhD"],
        index=1
    )
    
    # Subject dropdown
    subject = st.selectbox(
        "Choose a subject",
        ["Math", "History", "Computer Science", "Physics", "Biology", "Chemistry"],
        index=2
    )
    
    # Mode selection (Explanation vs. Quiz)
    mode = st.radio(
        "Select mode",
        ["Explain a Topic", "Generate a Quiz"],
        index=0
    )
    
    # Model selection - only show available models
    available_models = get_available_models()
    if available_models:
        model_name = st.selectbox(
            "AI Model",
            available_models,
            index=0,
            help="Gemma3 is recommended for better performance"
        )
        # Show model info
        if 'gemma3' in model_name.lower():
            st.success("✅ Using Gemma3 - Excellent choice!")
        elif 'deepseek-coder' in model_name.lower():
            st.success("✅ Using DeepSeek Coder - Great for coding tasks!")
        elif available_models and not any('gemma3' in m.lower() for m in available_models):
            st.info("💡 Install Gemma3 for better performance: `ollama pull gemma3`")
    else:
        st.error("⚠️ No Ollama models found.")
        st.markdown("**Install Gemma3 (recommended):**")
        st.code("ollama pull gemma3", language="bash")
        st.markdown("**Or other models:**")
        st.code("ollama pull llama3\nollama pull deepseek-coder", language="bash")
        model_name = None
    
    st.markdown("---")
    st.markdown("🔒 **100% Private** – No data leaves your device.")

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input(f"Ask a {subject} question..."):
    if not model_name:
        st.error("Please install an Ollama model first!")
        st.stop()
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Customize prompt based on mode
        if mode == "Explain a Topic":
            custom_prompt = f"""
            You are a {education_level}-level {subject} tutor. 
            Explain the following in a structured, step-by-step manner: 
            "{prompt}"
            
            - Break down complex concepts.
            - Use examples if helpful.
            - Keep explanations clear and concise.
            """
        else:  # Quiz mode
            custom_prompt = f"""
            Generate a {education_level}-level {subject} quiz question with:
            - 1 clear question
            - 4 multiple-choice options (A, B, C, D)
            - The correct answer marked with [CORRECT]
            - A brief explanation
            
            Topic: {prompt}
            """
        
        try:
            # Stream response from Ollama
            response = ollama.generate(
                model=model_name,
                prompt=custom_prompt,
                stream=True
            )
            
            for chunk in response:
                full_response += chunk["response"]
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
        except ollama.ResponseError as e:
            error_msg = f"❌ Model '{model_name}' not found. Please install it using: `ollama pull {model_name}`"
            message_placeholder.markdown(error_msg)
            full_response = error_msg
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            message_placeholder.markdown(error_msg)
            full_response = error_msg
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})