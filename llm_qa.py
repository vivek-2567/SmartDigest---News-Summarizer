from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

def create_summarizer():
    """
    Create a summarization model using Google's Gemini
    
    Returns:
        ChatGoogleGenerativeAI: LLM model for summarization
    """
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3  # Lower temperature for more focused summaries
    )

def summarize_article(title: str, content: str) -> str:
    """
    Summarize an article using the LLM
    
    Args:
        title (str): Article title
        content (str): Article content
        
    Returns:
        str: Generated summary
    """
    llm = create_summarizer()
    
    prompt = f"""You are a professional news article summarizer. Your task is to provide a comprehensive summary of the following news article.
    
    Give the answer only using text and bullet points. If required, you can bold out some of the text. don't give any other type of symbol that may break the writing style of st.write

    Guidelines for the summary:
    1. Focus on the main points, key facts, and important details
    2. Maintain a clear and organized structure
    3. Include all significant information but in a condensed form
    4. Highlight the most important events or developments
    5. Keep the language clear and professional
    6. Ensure the summary is easy to read and understand
    
    Article Title: {title}
    Article Content: {content}
    
    Please provide a detailed summary following the above guidelines:"""
    
    response = llm.invoke(prompt)
    return response.content
