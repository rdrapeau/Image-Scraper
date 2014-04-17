Image Scraper
================

This is a image web scraper written in python.

How To Use:
================

start.txt: Contains all of the starting relative points on the website

Run with: cat start.txt | parallel --gnu ./scrape.py {}
Stop with: pkill -9 Python
