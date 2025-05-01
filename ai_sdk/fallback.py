from .anthropic import AnthropicProvider
from .openai import OpenAIProvider

class FallbackProvider:
    """Provider with fallback capability."""
    
    def __init__(self, primary_provider="anthropic", 
                 anthropic_api_key=None, openai_api_key=None):
        """Initialize fallback provider.
        
        Args:
            primary_provider (str): Primary provider to use ("anthropic" or "openai")
            anthropic_api_key (str): Anthropic API key
            openai_api_key (str): OpenAI API key
        """
        self.providers = {
            "anthropic": AnthropicProvider(api_key=anthropic_api_key),
            "openai": OpenAIProvider(api_key=openai_api_key)
        }
        self.primary = primary_provider
        self.secondary = "openai" if primary_provider == "anthropic" else "anthropic"
        
    def generate_text(self, prompt, max_tokens=500, temperature=0.7):
        """Generate text with fallback.
        
        Args:
            prompt (str): Input prompt
            max_tokens (int): Maximum tokens in response
            temperature (float): Creativity level (0.0-1.0)
            
        Returns:
            str: Generated text
        """
        # Try primary provider
        result = self.providers[self.primary].generate_text(
            prompt, max_tokens, temperature
        )
        
        # If primary fails, try secondary
        if result is None:
            print(f"Falling back to {self.secondary} provider")
            result = self.providers[self.secondary].generate_text(
                prompt, max_tokens, temperature
            )
            
        return result
    
    def analyze_sentiment(self, text):
        """Analyze sentiment with fallback."""
        # Use the appropriate provider's method
        primary_provider = self.providers[self.primary]
        result = primary_provider.analyze_sentiment(text)
        
        # If primary fails, try secondary
        if result is None:
            secondary_provider = self.providers[self.secondary]
            result = secondary_provider.analyze_sentiment(text)
            
        return result
    
    def summarize_text(self, text, max_length=150):
        """Summarize text with fallback."""
        # Use the appropriate provider's method
        primary_provider = self.providers[self.primary]
        result = primary_provider.summarize_text(text, max_length)
        
        # If primary fails, try secondary
        if result is None:
            secondary_provider = self.providers[self.secondary]
            result = secondary_provider.summarize_text(text, max_length)
            
        return result
    
    def answer_question(self, question, context):
        """Answer question with fallback."""
        # Use the appropriate provider's method
        primary_provider = self.providers[self.primary]
        result = primary_provider.answer_question(question, context)
        
        # If primary fails, try secondary
        if result is None:
            secondary_provider = self.providers[self.secondary]
            result = secondary_provider.answer_question(question, context)
            
        return result