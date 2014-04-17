#!/usr/bin/env python
# Author: Aaron Nech
# Description: Scrapes a sub directory of http://www.indiabix.com
#  And extracts question and answers in json format.

import os, sys
import argparse
import requests
import urllib2
import FileDate
from bs4 import BeautifulSoup

URL = 'http://developer.google.com'

# Main declaration for console use
if __name__ == '__main__':
    imgCount = 0

    visited = set()
    # Domain to base requests off of

    # command line setup
    parser = argparse.ArgumentParser(description='Scrapes a sub directory of http://www.developer.google.com for IO codes')
    parser.add_argument('dir', help="The input website directory starting with '/'")
    arguments = parser.parse_args()

    links = [arguments.dir]
    visited.add(arguments.dir)

    while links:
        print "Visited: " + str(len(visited))
        print "To Do: " + str(len(links))
        link = links.pop()
        try:
            response = urllib2.urlopen(URL + link)
            soup = BeautifulSoup(response.read())
            if 'last-modified' not in response.headers.dict or FileDate.modified(response.headers.dict['last-modified'], 30):
                imgCount = 0
                for tag in soup.find_all('img'):
                    if tag.has_attr('src'):
                        if tag['src'].startswith('/') and (tag['src'].endswith('png') or tag['src'].endswith('svg') or tag['src'].endswith('jpg')):
                            try:
                                parts = tag['src'].split('/')
                                path = 'img/'+ parts[len(parts) - 1]
                                if not os.path.isfile(path):
                                    f = open(path, 'wb')
                                    image = urllib2.urlopen(URL + tag['src'])
                                    f.write(image.read())
                                    f.close()
                                    imgCount += 1
                            except:
                                    # print "404 error?"
                                    continue
            # print "Page " + link + " has " + str(imgCount) + " new images!"

            # Find each link in the page
            for tag in soup.find_all('a'):
                if tag.has_attr('href'):
                    if tag['href'].startswith('/') and '?' not in tag['href'] and tag['href'] not in visited:
                        links.insert(0, tag['href'])
                        visited.add(tag['href'])
                        # print "Adding " + tag['href'] + " to the queue..."
        except:
            continue

