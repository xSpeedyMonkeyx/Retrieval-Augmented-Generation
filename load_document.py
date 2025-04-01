import requests
from bs4 import BeautifulSoup

def load_vulture_article(url):
    """
    Fetches the article from the given URL, extracts and cleans text from the web page.
    
    Parameters:
        url (str): The URL of the Vulture article.
    
    Returns:
        str: A cleaned string containing the article text.
    """
    # Fetch the web page
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page. Status code: {response.status_code}")
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract text from all <p> tags, which generally contain the main content
    paragraphs = soup.find_all("p")
    
    # Clean and join the extracted text
    cleaned_text = "\n\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
    return cleaned_text

# URL of the Vulture article featuring an interview with Jack White
article_url = "https://www.vulture.com/2022/07/interview-jack-white-best-worst-superlatives.html"

# Load and clean the article text
article_text = load_vulture_article(article_url)

# Output the cleaned text for further processing
print(article_text)
