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
		link = links.pop()
		response = urllib2.urlopen(URL + link)
		soup = BeautifulSoup(response.read())

		for tag in soup.find_all('img'):
			if tag.has_attr('src'):
				if tag['src'].startswith('/') and (tag['src'].endswith('png') or tag['src'].endswith('svg') or tag['src'].endswith('jpg')):
					parts = tag['src'].split('/')
					path = 'img/' + str(imgCount) + '.' + parts[len(parts) - 1]
					f = open(path, 'wb')
					f.write(urllib2.urlopen(URL + tag['src']).read())
					f.close()
					if not FileDate.modified_recently(path, 7):
						os.remove(path)
						print "removed :)"

		# Find each link in the page
		for tag in soup.find_all('a'):
			if tag.has_attr('href'):
				if tag['href'].startswith('/') and '?' not in tag['href'] and tag['href'] not in visited:
					links.insert(0, tag['href'])
					visited.add(tag['href'])
					print tag['href']




