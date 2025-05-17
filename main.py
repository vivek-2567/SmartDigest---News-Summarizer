import streamlit as st
from consume_rss_feed import parse_rss_feed, fetch_article_content
from llm_qa import summarize_article

st.title("Smartdigest - News Summarizer")

# Initialize session states
if 'article_summaries' not in st.session_state:
    st.session_state.article_summaries = {}
if 'article_contents' not in st.session_state:
    st.session_state.article_contents = {}

# Expanded URL map with multiple RSS feeds
url_map = {
    "Times of India Business": "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",
    "Times of India Technology": "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    "Times of India US": "https://timesofindia.indiatimes.com/rssfeeds/30359486.cms",
    "Times of India NRI": "https://timesofindia.indiatimes.com/rssfeeds/7098551.cms",
    "Times of India World":"https://timesofindia.indiatimes.com/rssfeeds/296589292.cms",
    "Times of India Most Recent": "https://timesofindia.indiatimes.com/rssfeedmostrecent.cms",
    "Times of India Top Stories": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "Times of India Sports":"https://timesofindia.indiatimes.com/rssfeeds/4719148.cms",
    "BBC Business":"https://feeds.bbci.co.uk/news/business/rss.xml",
    "BBC Technology":"https://feeds.bbci.co.uk/news/technology/rss.xml",
}

# Create multiselect for feed categories
selected_categories = st.multiselect(
    "Select News Categories",
    options=list(url_map.keys()),
    default=None,
    help="Choose one or more news categories to display",
    key="news_category_selector"
)

if selected_categories:
    # Create tabs for each selected category
    category_tabs = st.tabs(selected_categories)
    
    # Process each selected feed in its respective tab
    for tab, category in zip(category_tabs, selected_categories):
        with tab:
            feed_url = url_map[category]
            feed_data = parse_rss_feed(feed_url)
            
            # Display feed information
            st.markdown(f"**Description:** {feed_data['feed_info']['description']}")
            st.markdown(f"**Last Updated:** {feed_data['feed_info']['updated']}")
            st.markdown("---")
            
            # Display entries in expanders
            st.markdown("### Latest Articles")
            for entry in feed_data['entries']:
                with st.expander(entry['title']):
                    st.markdown(f"**Published:** {entry['published']}")
                    st.markdown(f"**Link:** {entry['link']}")
                    st.markdown("**Summary:**")
                    st.markdown(entry['summary'])
                    
                    # Check if summary already exists
                    if entry['id'] not in st.session_state.article_summaries:
                        if st.button("Summarize Article", key=f"summarize_{entry['id']}"):
                            with st.spinner("Fetching and summarizing article..."):
                                # Check if we already have the article content
                                if entry['id'] not in st.session_state.article_contents:
                                    article_content = fetch_article_content(entry['link'])
                                    st.session_state.article_contents[entry['id']] = article_content
                                else:
                                    article_content = st.session_state.article_contents[entry['id']]
                                
                                # Generate summary using the dedicated summarization function
                                summary = summarize_article(entry['title'], article_content)
                                st.session_state.article_summaries[entry['id']] = summary
                    
                    # Display summary if available
                    if entry['id'] in st.session_state.article_summaries:
                        st.markdown("### AI-Generated Summary")
                        st.write(st.session_state.article_summaries[entry['id']])
