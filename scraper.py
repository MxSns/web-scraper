# Script : scraper.py
# Author : mxn

import argparse, requests, sys, re, shutil, time, os
from rich.console import Console
from urllib.parse import urljoin

console = Console()

width = shutil.get_terminal_size().columns

parser = argparse.ArgumentParser(description='Web scraper script to recursively visit pages within a specified domain, logging crawled URLs and external references and scrapes the html code.\nRun with: python3 web_crawler.py --domain <URL>')
parser.add_argument('-d', '--domain', required=True, help='the domain to crawl in')
args = parser.parse_args()

dmn = args.domain
to_crawl = [dmn]
crawled = []
external = []

title = "\t\tWEB SCRAPER\n"

# Creates a variable to define the folder name + the path to it
folder_name = re.sub(r'http://', "", dmn)
scrape_path = "scraped" + os.sep + folder_name + "-" + str(int(time.time()))

if not os.path.exists(scrape_path):
    os.makedirs(scrape_path)
else:
    print(f"{scrape_path} already exists, please wait.")

# Function to create the folder :
def get_storage_info(url):
    stripped_url = re.sub(dmn, "", url)
    path = scrape_path + re.sub(os.sep, "/", stripped_url)
    directory = os.path.dirname(path)
    if not os.path.dirname(directory):
        os.makedirs(directory)
    return path

# Request a webpage and return the html text
def fetch_page(url):
    
    try:
        response = requests.get(url)

    except requests.exceptions.RequestException as e:
        sys.exit(e)
    # Remove the url if it is in the to_crawl list
    if url in to_crawl:
        to_crawl.remove(url)
    # Add the url to the crawled list
    crawled.append(url)

    # Save the webpage here without the domain link :
    if dmn is not url:    
        storage_path = get_storage_info(url)
        with open(storage_path, "w") as html:
            html.write(response.text)

    return response.text

# Parse the HTML for links, decide which needs to be visited
def get_linked_pages(html):

    pattern = r'<a\s+href=\"?([^\">\s]+).*?([a-z0-9: ]+)</a>'

    links = re.findall(pattern, html, re.I)
        
    for link in links:

        # Access the URL in match group 0.
        this_url = link[0]
        this_url = this_url.split("#")[0]
        page = urljoin(dmn, this_url)

        # Check if the domain is in the current URL
        inDomain = re.search(dmn, page, re.I)
        if inDomain:
            if page not in crawled and page not in to_crawl:
                to_crawl.append(page)
        
        elif page not in external:
             external.append(page)
        
print("=" * width + "\n")
print(title)
print("\n" + "=" * width )
print(f"\nEnumerating links form {args.domain} ...\n")

# Loopin to_crawl until list is empty
while to_crawl:
    for url in to_crawl:
        html = fetch_page(url)
        get_linked_pages(html)

print("\nCrawled URLs:\n" + "\n".join(crawled))
if not external:
    console.print(f"\nNo external links were found in {dmn}", style="red")
else:
    print("\nExternal URLs:\n" + "\n".join(external))
