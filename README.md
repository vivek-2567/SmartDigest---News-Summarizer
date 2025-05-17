# SmartDigest - News Summarizer 📰

<div align="center">

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B)
![License](https://img.shields.io/badge/license-MIT-green)

An intelligent news aggregation and summarization tool that uses AI to provide concise, meaningful summaries of news articles from various sources.

</div>

DEMO: The project is deployed at streamlit cloud. Anyone can access it using the link [ Demo: https://smartdigest.streamlit.app ](https://smartdigest.streamlit.app)

## 🌟 Features

### News Aggregation
- **Multiple News Sources**
  - Times of India (Business, Technology, US, NRI, World, Sports)
  - BBC News (Business, Technology)
  - Easily extensible to add more sources

### Article Management
- **Smart Content Handling**
  - Automatic article content extraction
  - Clean and formatted presentation
  - Original article summaries preserved
  - Publication dates and source tracking

### AI-Powered Summarization
- **Intelligent Summaries**
  - One-click summarization
  - Comprehensive coverage of key points
  - Clear and organized format
  - Persistent storage of summaries
  - Powered by Google's Gemini AI

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google API key for Gemini AI
- Internet connection

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vivek-2567/SmartDigest---News-Summarizer.git
   cd smartdigest
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**
   Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

### Running the Application

1. **Start the application**
   ```bash
   streamlit run main.py
   ```

2. **Access the interface**
   - Open your browser to the provided local URL (typically http://localhost:8501)
   - Select news categories
   - Browse articles
   - Click "Summarize Article" for AI-generated summaries

## 💻 Technical Architecture

### Core Components
- **Web Interface**: Streamlit-based responsive UI
- **Content Processing**: BeautifulSoup for web scraping
- **AI Engine**: Google's Gemini model for summarization
- **Data Management**: Session-based storage for efficiency

### Key Technologies
- **Frontend**: Streamlit
- **Backend**: Python
- **AI/ML**: Google Gemini AI
- **Web Scraping**: BeautifulSoup4
- **RSS Handling**: Feedparser

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| GOOGLE_API_KEY | Your Google API key for Gemini AI | Yes |

### RSS Feed Configuration
Add new RSS feeds by updating the `url_map` in `main.py`:
```python
url_map = {
    "Source Name": "RSS Feed URL",
    # Add more sources here
}
```

## 📝 Usage Examples

### Basic Usage
1. Select news categories from the dropdown
2. Browse through articles
3. Click "Summarize Article" for AI summary
4. View the generated summary below the article

### Best Practices
- Keep your API key secure
- Regularly update the application for new features
- Monitor API usage to stay within limits

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Security

- Never commit your API keys or sensitive information
- Keep your dependencies updated
- Report security vulnerabilities to the maintainers

## 📞 Support

For support, please:
1. Check the Issues section
2. Create a new issue if your problem isn't already listed
3. Provide detailed information about your problem

## 🙏 Acknowledgments

- Google for providing the Gemini AI model
- Streamlit for the web framework
- All contributors who have helped improve this project

