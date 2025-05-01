import openai
from .base import AIProvider

class OpenAIProvider(AIProvider):
    """OpenAI GPT implementation"""
    
    def __init__(self, api_key=None):
        super().__init__(api_key)
        self.client = openai.OpenAI(api_key=self.api_key)
        self.model = "gpt-3.5-turbo"
        
    def generate_text(self, prompt, max_tokens=500, temperature=0.7):
        """Generate text using OpenAI.
        
        Args:
            prompt (str): Input prompt
            max_tokens (int): Maximum tokens in response
            temperature (float): Creativity level (0.0-1.0)
            
        Returns:
            str: Generated text
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error with OpenAI: {e}")
            return None