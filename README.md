Image Scraper
================

This is a image web scraper written in python.

How To Use:
================
Edit scrape.py BASE_URL to be the base url of the website you wish to crawl. Also change AGE to the allowed number of days for the image age.
<<<<<<< HEAD
=======

start.txt: Contains all of the starting relative points on the website

Run with: python scrape.py [start_relative_link]

(Parallel) Run with: cat start.txt | parallel --gnu ./scrape.py {}

Stop with: pkill -9 Python
>>>>>>> FETCH_HEAD
