## Web Scraping Amazon Prodcut Details using Scrapy Framework
## Libraries used
- scrapy
- ipython
- virtualenv
- scrapeops-scrapy
## Project Structure
```bash
amazon_scraper/
│── venv/
│── amazon_scraper/               # Project module
│   ├── spiders/                # Spider definitions
│   │   ├── __init__.py
│   │   ├── amazon.py        # Custom spider
│   ├── __init__.py
│   ├── items.py                # Define scraped data structure
│   ├── middlewares.py          # Custom middlewares
│   ├── pipelines.py            # Data processing pipelines
│   ├── settings.py             # Scrapy settings
│── scrapy.cfg                  # Scrapy configuration file
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation

```bash
## to create virtual env
python -m venv venv
python venv\Scripts\activate
## to create project
scrapy startproject amazon_scraper
## go the spider folder
scrapy genspider amazon '##paste webpage url'
## to activate scrapy shell
scrapy shell
```
### Load API Key from Environment Variables
- Uses dotenv to load API_KEY from a .env file.
- This key is used to access ScrapeOps Proxy API, which helps bypass Amazon’s anti-scraping measures.
### Define Proxy URL Helper Function (get_scrapeops_url)
- Takes a URL as input and returns a modified proxy URL using ScrapeOps API.
- Ensures requests go through a rotating proxy to prevent blocking.
###  Start Requests (start_requests)
- Defines a keyword list (['pendrive']).
- Iterates through pages 1 to 9 of Amazon search results.
- Generates a URL for each page and sends requests via ScrapeOps Proxy.
### Extract Product Links (parse)
- Uses XPath to find product links from search result pages.
- Modifies relative URLs to absolute (https://www.amazon.in) and follows each link.
###  Extract Product Details (parse_product)
- Scrapes detailed product information:
- Name, Price, Brand, Memory Storage Capacity, Hardware Interface, Features, Write Speed
- Stores data in an AmazonScraperItem object and yields it.
## Potential Enhancements
- Implement pagination detection instead of hardcoding page numbers.
- Add error handling for cases where product details are missing.
- Store scraped data in JSON/CSV using Scrapy’s feed exports.

