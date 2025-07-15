# DataScrapping

This project contains a simple Python script that fetches a web page and prints its body content. The script was originally created with Visual Studio's Python tools and comes with solution and project files. Only `DataScrapping.py` is needed to run the example.

## Requirements
- Python 3
- `requests`
- `beautifulsoup4`

Install the required packages with:

```bash
pip install requests beautifulsoup4
```

## Usage
Run the script directly with Python:

```bash
python DataScrapping.py
```

The script retrieves the page at `https://bt.design/dot-with-arm-chair.html`, parses it with BeautifulSoup, and prints the entire body of the page.

Feel free to modify the URL or expand the script to process the scraped data in a more useful way.
