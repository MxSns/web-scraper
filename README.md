## WEB SCRAPER

This project is a Python script that recursively scrapes HTML pages from a specified domain.
It crawls pages within the domain, extracts internal links for futher crawling, saves the HTML content of each page in a structured folder, and lists external links.
The script uses argparse to accept a domain via the command line and displays results with formatted output using rich library

Table of Contents
- Features (#features)
- Prerequisites (#prerequisites)
- Installation (#installation)
- Usage (#usage)
- Command-Line Arguments (#command-line-arguments)
- Output Structure (#output-structure)

## Features :

- Recursive crawling : visits all pages within a domain by following internal links
- link extraction : identifies internal and external links
- HTML saving : Stores the HTML 
- Fragment handling : ignores URL fragments

Prerequisites :

- Required Python libraries :
request, rich

- Standard modules :
argparse, sys, re, shutil, time, os, urllib.parse

## Installation :

Clone or download the repo :

git clone https://github.com/your-username/your-repo.git
cd your-repo

Optional :
Create a virtual environment :

python -m venv venv
source venv/bin/activate

Install the dependencies :
pip install -r requirements.txt

## Usage :

Run the script via the command line using the main file (scraper.py), use the -d argument to specify the domain to craw.

python3 scraper.py -d <domain>


