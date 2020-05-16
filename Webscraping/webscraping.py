import csv

import numpy as np
from requests import get
from bs4 import BeautifulSoup
from time import sleep, time
from random import randint
from IPython.core.display import clear_output

# parses and stores all reviews and ratings from one request page
# usually ~20 reviews
def singlePageParse(url):
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    # finds and prints number of reviews on page
    review_containers = html_soup.find_all('div', class_ = 'lister-item mode-detail imdb-user-review collapsable')

    for container in review_containers:
        # filter out reviews without a numerical user rating
        if container.find('div', class_='ipl-ratings-bar') is not None:
            rating = container.find('span', class_ = 'rating-other-user-rating').text
            # some text parsing for the user rating
            split = rating.split('\n')
            rating = split[6]

            review = container.find('div', class_= 'text show-more__control').text
            review = review.replace('\n', ' ')

            # opens file and appends rating and review, creates the file if first time
            with open('out8.csv', 'a', encoding="utf-8") as outCSV:
                outCSV.write(rating + '\t' + review + '\n')



# 1-55130 are lines with 1000+ user reviews
# uses titles.csv with the sorted IMDB titles by number of reviews
def parseTitlesCSV():
    titles = []
    with open('titles.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        over1000 = True
        while (over1000):
            for row in readCSV:
                try:
                    title = row[0]
                    titles.append(title)
                    if (int(row[2]) < 1000):
                        over1000 = False
                        break
                except ValueError:
                    print('')



        print('Done parsing titles with len: ' + str(len(titles)))

    return titles



titles = parseTitlesCSV()
print(titles)

# use for getting samples from each rating 1-10
oneToTen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_time = time()
requests = 0

# goes through movies list from most-least number of total reviews and
# sends HTML request for all ratings for each
# sleeps random times in between each request to not overload the IMDB server
for i in range(len(titles)):
    # Use to start from a particular movie
    # if i > 5000 :
        # send request for new movie to scrape
        for j in range(len(oneToTen)):
            # get reviews from each rating for this movie
            url = 'https://www.imdb.com/title/' + titles[i] + '/reviews?sort=helpfulnessScore&dir=desc&ratingFilter=' + str(oneToTen[j])
            # url = 'https://www.imdb.com/title/' + titles[i] + '/reviews?ref_=tt_ov_rt'
            singlePageParse(url)
            requests += 1
            sleep(randint(1,3))
            current_time = time()
            elapsed_time = current_time - start_time
            print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
clear_output(wait = True)

