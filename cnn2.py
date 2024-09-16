import requests
from bs4 import BeautifulSoup

# URL to scrape
CNN_URL = 'https://www.cnn.com/'

# Function to scrape headlines from CNN using beautiful soup
def scrape_cnn_headlines():
    response = requests.get(CNN_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = []

        # Find all headline tags (e.g., h1, h2, h3)
        for tag in ['h1', 'h2', 'h3']:
            for item in soup.find_all(tag):
                # Get the text of each headline and strip unnecessary spaces
                text = item.get_text(strip=True)
                if text:
                    headlines.append(text)

        return headlines
    else:
        raise Exception(f"Failed to retrieve CNN page. Status code: {response.status_code}")

def main():
    print("Scraping CNN headlines...")
    try:
        headlines = scrape_cnn_headlines()
        print("\nCNN Headlines:")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
