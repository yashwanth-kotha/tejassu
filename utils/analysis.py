from datetime import datetime, timedelta

def format_entries_for_context(entries):
    """Format entries for context.
    
    Args:
        entries (list): List of entries
        
    Returns:
        str: Formatted entries for context
    """
    context = ""
    
    for entry in entries:
        context += f"Date: {entry['date']}\n"
        
        for i, (question, answer) in enumerate(zip(entry['questions'], entry['answers'])):
            context += f"Q{i+1}: {question}\n"
            context += f"A{i+1}: {answer}\n"
            
        context += "\n---\n\n"
        
    return context

def get_recent_entries(entries, days=7):
    """Get entries from the last N days.
    
    Args:
        entries (list): All entries
        days (int): Number of days to look back
        
    Returns:
        list: Recent entries
    """
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    
    recent = []
    for entry in entries:
        entry_date = entry["date"].split()[0]  # Get just the date part
        if entry_date >= cutoff:
            recent.append(entry)
            
    return recent