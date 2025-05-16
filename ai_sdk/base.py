class AIProvider:
    """Base class for AI providers."""
    
    def __init__(self, api_key=None):
        self.api_key = api_key
        
    def generate_text(self, prompt, max_tokens=500, temperature=0.7):
        """Generate text based on prompt
        
        Args:
            prompt (str): Input prompt
            max_tokens (int): Maximum tokens in response
            temperature (float): Creativity level (0.0-1.0)
            
        Returns:
            str: Generated text
        """
        raise NotImplementedError("Subclasses must implement this method")
        
    def analyze_sentiment(self, text):
        """Analyze sentiment of text.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Sentiment analysis results
        """
        prompt = f"""Analyze the sentiment of the following journal entry. 
        Provide a score from -1.0 (very negative) to 1.0 (very positive),
        and identify the key emotions expressed.
        
        Journal entry: {text}
        
        Response format:
        {{
            "score": <float>,
            "emotions": ["emotion1", "emotion2", ...],
            "summary": "<brief summary>"
        }}
        """
        result = self.generate_text(prompt)
        return result
    
    def summarize_text(self, text, max_length=150):
        """Summarize text.
        
        Args:
            text (str): Text to summarize
            max_length (int): Maximum summary length
            
        Returns:
            str: Summarized text
        """
        prompt = f"""Summarize the following journal entry in no more than {max_length} characters:
        
        {text}
        """
        return self.generate_text(prompt)
    
    def answer_question(self, question, context):
        """Answer a question based on context.
        
        Args:
            question (str): Question to answer
            context (str): Context to use for answering
            
        Returns:
            str: Answer
        """
        prompt = f"""Answer the following question based only on the provided journal entries:
        
        Journal entries:
        {context}
        
        Question: {question}
        """
        return self.generate_text(prompt)
