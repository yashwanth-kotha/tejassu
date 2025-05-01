import json
import os
from datetime import datetime

# File to store journal entries
STORAGE_FILE = "journal_entries.json"

def initialize_storage():
    """Initialize storage file if it doesn't exist."""
    if not os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "w") as f:
            json.dump([], f)

def save_entry(questions, answers):
    """Save a journal entry.
    
    Args:
        questions (list): List of questions
        answers (list): List of answers
        
    Returns:
        bool: Success status
    """
    try:
        initialize_storage()
        
        # Read existing entries
        with open(STORAGE_FILE, "r") as f:
            entries = json.load(f)
            
        # Create new entry
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "questions": questions,
            "answers": answers
        }
        
        # Add new entry
        entries.append(entry)
        
        # Save all entries
        with open(STORAGE_FILE, "w") as f:
            json.dump(entries, f, indent=2)
            
        return True
    except Exception as e:
        print(f"Error saving entry: {e}")
        return False

def get_entries(start_date=None, end_date=None):
    """Get journal entries within date range.
    
    Args:
        start_date (str): Start date (YYYY-MM-DD)
        end_date (str): End date (YYYY-MM-DD)
        
    Returns:
        list: List of entries
    """
    try:
        initialize_storage()
        
        # Read existing entries
        with open(STORAGE_FILE, "r") as f:
            entries = json.load(f)
            
        # Filter by date if needed
        if start_date or end_date:
            filtered = []
            for entry in entries:
                entry_date = entry["date"].split()[0]  # Get just the date part
                
                if start_date and entry_date < start_date:
                    continue
                    
                if end_date and entry_date > end_date:
                    continue
                    
                filtered.append(entry)
                
            return filtered
        
        return entries
    except Exception as e:
        print(f"Error getting entries: {e}")
        return []