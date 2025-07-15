import requests
from bs4 import BeautifulSoup
import csv

def main() -> None:
    """Fetch a web page and print its title and body text."""
    url = "https://bt.design/dot-with-arm-chair.html"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

      # Use `.string` instead of the deprecated `text` argument
    title = soup.find("title").string
    body_text = soup.body.get_text(separator="\n", strip=True)
    print(title)
    print(body_text)


if __name__ == "__main__":
    main()
