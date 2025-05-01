import anthropic
from .base import AIProvider

class AnthropicProvider(AIProvider):
    """Anthropic Claude implementation"""
    
    def __init__(self, api_key=None):
        super().__init__(api_key)
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = "claude-3-sonnet-20240307"
        
    def generate_text(self, prompt, max_tokens=500, temperature=0.7):
        """Generate text using Anthropic Claude.
        
        Args:
            prompt (str): Input prompt
            max_tokens (int): Maximum tokens in response
            temperature (float): Creativity level (0.0-1.0)
            
        Returns:
            str: Generated text
        """
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Error with Anthropic: {e}")
            return None