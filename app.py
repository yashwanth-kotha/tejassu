import streamlit as st
import os
from datetime import datetime
import json
from dotenv import load_dotenv

load_dotenv()

# Import our modules
from ai_sdk.fallback import FallbackProvider
from utils.questions import get_daily_questions
from utils.storage import save_entry, get_entries
from utils.analysis import format_entries_for_context, get_recent_entries

# Page configuration
st.set_page_config(
    page_title="Tejassu - AI Journal",
    page_icon="📔",
    layout="centered"
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "journal"  # Options: journal, analysis, history

# Load API keys from environment or .env file
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "")
openai_api_key = os.getenv("OPENAI_API_KEY", "")

# Initialize AI provider
@st.cache_resource
def get_ai_provider():
    return FallbackProvider(
        primary_provider="anthropic",
        anthropic_api_key=anthropic_api_key,
        openai_api_key=openai_api_key
    )

ai_provider = get_ai_provider()

# App header
st.title("📔 Tejassu")
st.subheader("Your AI-Enhanced Journal")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Journal", "Analysis", "History"],
    key="nav"
)
st.session_state.page = page.lower()

# Journal page
if st.session_state.page == "journal":
    st.header("Today's Journal")
    
    # Get today's questions
    questions = get_daily_questions(num_questions=5)
    
    # Create form for journal entry
    with st.form("journal_form"):
        answers = []
        
        for i, question in enumerate(questions):
            st.write(f"**Q{i+1}: {question}**")
            answer = st.text_area(f"Answer {i+1}", key=f"answer_{i}", height=100, label_visibility="collapsed")
            answers.append(answer)
            st.divider()
            
        submitted = st.form_submit_button("Save Journal Entry")
        
        if submitted:
            if all(answer.strip() for answer in answers):
                success = save_entry(questions, answers)
                if success:
                    st.success("Journal entry saved successfully!")
                else:
                    st.error("Failed to save journal entry")
            else:
                st.warning("Please answer all questions")

# Analysis page
elif st.session_state.page == "analysis":
    st.header("Journal Analysis")
    
    # Get all entries
    entries = get_entries()
    
    if not entries:
        st.info("No journal entries found. Start journaling to see analysis.")
    else:
        # Analysis options
        analysis_type = st.selectbox(
            "Select Analysis Type",
            ["Sentiment Analysis", "Summary", "Ask a Question"]
        )
        
        # Date range selection
        date_range = st.selectbox(
            "Time Period",
            ["Last 7 Days", "Last 30 Days", "All Time"]
        )
        
        if date_range == "Last 7 Days":
            filtered_entries = get_recent_entries(entries, days=7)
        elif date_range == "Last 30 Days":
            filtered_entries = get_recent_entries(entries, days=30)
        else:
            filtered_entries = entries
            
        if not filtered_entries:
            st.info(f"No journal entries found for the selected period ({date_range}).")
        else:
            # Prepare context from entries
            context = format_entries_for_context(filtered_entries)
            
            if analysis_type == "Sentiment Analysis":
                st.subheader("Sentiment Analysis")
                
                if st.button("Analyze Sentiment"):
                    with st.spinner("Analyzing sentiment..."):
                        result = ai_provider.analyze_sentiment(context)
                        st.json(result)
                        
            elif analysis_type == "Summary":
                st.subheader("Journal Summary")
                
                if st.button("Generate Summary"):
                    with st.spinner("Generating summary..."):
                        summary = ai_provider.summarize_text(context, max_length=300)
                        st.write(summary)
                        
            elif analysis_type == "Ask a Question":
                st.subheader("Ask About Your Journal")
                
                question = st.text_input("Enter your question")
                
                if question and st.button("Get Answer"):
                    with st.spinner("Finding answer..."):
                        answer = ai_provider.answer_question(question, context)
                        st.write(answer)

# History page
elif st.session_state.page == "history":
    st.header("Journal History")
    
    # Get all entries
    entries = get_entries()
    
    if not entries:
        st.info("No journal entries found. Start journaling to see history.")
    else:
        # Sort entries by date (newest first)
        entries.sort(key=lambda x: x["date"], reverse=True)
        
        for entry in entries:
            with st.expander(f"Entry: {entry['date']}"):
                for i, (question, answer) in enumerate(zip(entry['questions'], entry['answers'])):
                    st.write(f"**Q: {question}**")
                    st.write(f"A: {answer}")
                    st.divider()