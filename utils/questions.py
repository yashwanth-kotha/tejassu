import random
from datetime import datetime

# List of journal prompts
QUESTIONS = [
    "What made you smile today?",
    "What was the most challenging part of your day?",
    "What are you grateful for today?",
    "What did you learn today?",
    "How did you take care of yourself today?",
    "What is something you accomplished today?",
    "What would you like to improve tomorrow?",
    "What is something that surprised you today?",
    "What is something you're looking forward to?",
    "How did you help someone today?",
    "What was a moment of joy today?",
    "What is something you'd like to remember about today?",
    "What did you do today that was meaningful?",
    "How did your mood change throughout the day?",
    "What is something you're proud of today?",
    "What is something you wish you had done differently?",
    "What is something that made you laugh today?",
    "What is something that made you think deeply today?",
    "What is a small win you had today?",
    "How did you connect with others today?"
]

def get_daily_questions(num_questions=5, seed=None):
    """Get a set of daily questions.
    
    Args:
        num_questions (int): Number of questions to return
        seed (any): Seed for random selection (defaults to today's date)
        
    Returns:
        list: List of questions
    """
    if seed is None:
        # Use today's date as seed for consistent daily questions
        today = datetime.now().strftime("%Y-%m-%d")
        random.seed(today)
    else:
        random.seed(seed)
    
    # Select a subset of questions
    if num_questions > len(QUESTIONS):
        num_questions = len(QUESTIONS)
        
    selected = random.sample(QUESTIONS, num_questions)
    
    # Reset random seed
    random.seed(None)
    
    return selected