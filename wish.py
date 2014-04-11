#writing a site scraper

import scrapy

#prompt the user for his name and keep it in a variable called name
name = raw_input('Well, howdy. What is your name? ')

#prompt the user for the webpage where we're scraping records from
webpage = raw_input('What page do you wanna scrape?')

#scrape all records from the webpage that contain the user's name

#dump the results to screen
