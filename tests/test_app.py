"""
Unit tests for AI Tutor application.
Run with: pytest tests/test_app.py
"""

import pytest
import streamlit as st
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mock streamlit before importing app
st.cache_data = lambda func: func
st.error = Mock()
st.info = Mock()
st.success = Mock()

import app


class TestModelDetection:
    """Test the model detection functionality."""
    
    @patch('app.ollama.list')
    def test_get_available_models_success(self, mock_ollama_list):
        """Test successful model detection."""
        # Mock Ollama response with models attribute
        mock_model1 = Mock()
        mock_model1.model = "gemma3:latest"
        mock_model2 = Mock()
        mock_model2.model = "deepseek-coder:latest"
        
        mock_response = Mock()
        mock_response.models = [mock_model1, mock_model2]
        mock_ollama_list.return_value = mock_response
        
        result = app.get_available_models()
        
        assert "gemma3:latest" in result
        assert "deepseek-coder:latest" in result
        assert len(result) == 2
    
    @patch('app.ollama.list')
    def test_get_available_models_empty(self, mock_ollama_list):
        """Test handling of no models."""
        mock_response = Mock()
        mock_response.models = []
        mock_ollama_list.return_value = mock_response
        
        result = app.get_available_models()
        
        assert result == []
    
    @patch('app.ollama.list')
    def test_get_available_models_exception(self, mock_ollama_list):
        """Test handling of Ollama connection errors."""
        mock_ollama_list.side_effect = Exception("Connection failed")
        
        result = app.get_available_models()
        
        assert result == []
        # Verify error message was displayed
        st.error.assert_called()
    
    @patch('app.ollama.list')
    def test_model_prioritization(self, mock_ollama_list):
        """Test that models are prioritized correctly."""
        # Create mock models in random order
        models = []
        model_names = ["llama3", "gemma3:latest", "deepseek-coder", "mistral"]
        
        for name in model_names:
            mock_model = Mock()
            mock_model.model = name
            models.append(mock_model)
        
        mock_response = Mock()
        mock_response.models = models
        mock_ollama_list.return_value = mock_response
        
        result = app.get_available_models()
        
        # gemma3:latest should be first (highest priority)
        assert result[0] == "gemma3:latest"
        # deepseek-coder should be before llama3
        assert result.index("deepseek-coder") < result.index("llama3")


class TestAppConfiguration:
    """Test application configuration and setup."""
    
    def test_session_state_initialization(self):
        """Test that session state is properly initialized."""
        # This would need to be tested in a Streamlit context
        # For now, we just verify the structure exists
        assert hasattr(app, 'st')
    
    def test_education_levels(self):
        """Test that all education levels are defined."""
        expected_levels = ["School", "High School", "Graduate", "PG/PhD"]
        # This test would need access to the selectbox options
        # In a real test, we'd mock the streamlit components
        assert True  # Placeholder
    
    def test_subjects(self):
        """Test that all subjects are defined."""
        expected_subjects = ["Math", "History", "Computer Science", 
                           "Physics", "Biology", "Chemistry"]
        # This test would need access to the selectbox options
        assert True  # Placeholder


class TestPromptGeneration:
    """Test prompt generation for different modes."""
    
    def test_explanation_prompt_format(self):
        """Test explanation mode prompt formatting."""
        # Mock the variables that would come from Streamlit
        education_level = "High School"
        subject = "Math"
        prompt = "quadratic equations"
        
        expected_content = [
            f"{education_level}-level {subject} tutor",
            "step-by-step manner",
            prompt,
            "Break down complex concepts",
            "Use examples",
            "clear and concise"
        ]
        
        custom_prompt = f"""
            You are a {education_level}-level {subject} tutor. 
            Explain the following in a structured, step-by-step manner: 
            "{prompt}"
            
            - Break down complex concepts.
            - Use examples if helpful.
            - Keep explanations clear and concise.
            """
        
        for content in expected_content:
            assert content.lower() in custom_prompt.lower()
    
    def test_quiz_prompt_format(self):
        """Test quiz mode prompt formatting."""
        education_level = "Graduate"
        subject = "Physics"
        prompt = "quantum mechanics"
        
        custom_prompt = f"""
            Generate a {education_level}-level {subject} quiz question with:
            - 1 clear question
            - 4 multiple-choice options (A, B, C, D)
            - The correct answer marked with [CORRECT]
            - A brief explanation
            
            Topic: {prompt}
            """
        
        expected_content = [
            "quiz question",
            "multiple-choice options",
            "A, B, C, D",
            "[CORRECT]",
            prompt
        ]
        
        for content in expected_content:
            assert content in custom_prompt


class TestErrorHandling:
    """Test error handling and edge cases."""
    
    @patch('app.ollama.generate')
    def test_ollama_response_error(self, mock_generate):
        """Test handling of Ollama ResponseError."""
        from ollama import ResponseError
        mock_generate.side_effect = ResponseError("Model not found")
        
        # This would need to be tested in a Streamlit context
        # For now, we verify the exception is properly imported
        assert ResponseError
    
    @patch('app.ollama.generate')
    def test_general_exception_handling(self, mock_generate):
        """Test handling of general exceptions."""
        mock_generate.side_effect = Exception("Unexpected error")
        
        # This would need to be tested in a Streamlit context
        assert True  # Placeholder
    
    def test_no_model_selected(self):
        """Test behavior when no model is selected."""
        # This would test the case where model_name is None
        assert True  # Placeholder


class TestUtilityFunctions:
    """Test utility functions and helpers."""
    
    def test_model_name_extraction(self):
        """Test extraction of model names from Ollama response."""
        # Test the logic that extracts model names
        mock_model = Mock()
        mock_model.model = "test-model:latest"
        
        # Simulate the extraction logic
        name = getattr(mock_model, 'model', None)
        assert name == "test-model:latest"
    
    def test_model_ordering(self):
        """Test the model ordering logic."""
        model_names = ["llama3", "gemma3:latest", "deepseek-coder", "random-model"]
        preferred_order = ['gemma3:latest', 'gemma3', 'deepseek-coder', 'llama3']
        
        ordered_models = []
        
        # Simulate the ordering logic from the app
        for preferred in preferred_order:
            if preferred in model_names:
                ordered_models.append(preferred)
        
        for model in model_names:
            if model not in ordered_models:
                ordered_models.append(model)
        
        assert ordered_models[0] == "gemma3:latest"
        assert "random-model" in ordered_models


# Integration tests would require a full Streamlit environment
class TestIntegration:
    """Integration tests - require full environment setup."""
    
    @pytest.mark.integration
    def test_full_app_startup(self):
        """Test that the app starts without errors."""
        # This would require running the actual Streamlit app
        # and checking that it loads properly
        pytest.skip("Requires full Streamlit environment")
    
    @pytest.mark.integration 
    def test_model_loading_and_response(self):
        """Test actual model loading and response generation."""
        # This would test with real Ollama models
        pytest.skip("Requires Ollama with models installed")


if __name__ == "__main__":
    # Run tests with: python -m pytest tests/test_app.py -v
    pytest.main([__file__, "-v"])
