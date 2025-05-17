import feedparser
from bs4 import BeautifulSoup
import requests

def clean_html_text(html_text: str) -> str:
    """
    Remove HTML tags from text and clean the content
    
    Args:
        html_text (str): Text containing HTML tags
        
    Returns:
        str: Clean text without HTML tags
    """
    if not html_text:
        return 'N/A'
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text().strip()

def parse_rss_feed(feed_url: str) -> dict:
    """
    Parse RSS feed and store data in a structured dictionary
    
    Args:
        feed_url (str): URL of the RSS feed
        
    Returns:
        Dict containing feed metadata and entries
    """
    feed = feedparser.parse(feed_url)
    feed_data = {
        'feed_info': {
            'title': feed.feed.title if hasattr(feed.feed, 'title') else 'N/A',
            'description': feed.feed.description if hasattr(feed.feed, 'description') else 'N/A',
            'link': feed.feed.link if hasattr(feed.feed, 'link') else 'N/A',
            'updated': feed.feed.updated if hasattr(feed.feed, 'updated') else 'N/A'
        },
        'entries': []
    }
    
    for entry in feed.entries:
        entry_data = {
            'title': entry.title if hasattr(entry, 'title') else 'N/A',
            'link': entry.link if hasattr(entry, 'link') else 'N/A',
            'published': entry.published if hasattr(entry, 'published') else 'N/A',
            'summary': clean_html_text(entry.summary) if hasattr(entry, 'summary') else 'N/A',
            'id': entry.id if hasattr(entry, 'id') else 'N/A',
        }
        feed_data['entries'].append(entry_data)
    
    return feed_data

def fetch_article_content(url: str) -> str:
    """
    Fetch and clean the full content of an article from its URL
    
    Args:
        url (str): URL of the article
        
    Returns:
        str: Cleaned article content
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted elements
        for element in soup.find_all(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
            
        # Try to find the main article content
        article_content = soup.find('article') or soup.find('main') or soup.find('div', class_=['content', 'article', 'story'])
        
        if article_content:
            return clean_html_text(str(article_content))
        else:
            return clean_html_text(str(soup.find('body')))
            
    except Exception as e:
        return f"Error fetching article content: {str(e)}"