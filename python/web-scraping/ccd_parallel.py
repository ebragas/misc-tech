# pylint: disable=invalid-name

# break down the profile page parsing into a single function

import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from multiprocessing import Pool

# constants
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) ' +
                         'AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 ' +
                         'Safari/600.1.4'}


# retrieves data from a park profile page
def profile_get(url):
    """
    url: string url for the concretedisciples page to parse
    Returns a dictionary of the fields and values available on the profile.
    """

    # print("Requesting...", url)
    r = requests.get(url)

    if r.status_code == 200:
        print("Processing...", url)
        soup = BeautifulSoup(r.text, 'lxml')
        r.close()

        field_tags = soup.select(".jrFieldLabel")
        value_tags = soup.select(".jrFieldValue ")

        fields = []
        values = []

        for t in field_tags:
            fields.append(t.text.strip())

        for t in value_tags:
            values.append(t.text.strip())

        data = dict(zip(fields, values))

        return data

    else:
        print(r.status_code)
        r.close()

    print("Done!")


# Retrieves a list of URLs from a listings page
def urllist_get(url, page, limit):
    """
    ...
    """
    params = {'page': page, 'limit': limit}
    print("Retrieving URLs...", url + "/?page=" + str(page) + "&limit=" + str(limit))
    r = requests.get(url, params=params)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        r.close()

        urllist = []
        for tag in soup.select(".jrContentTitle"):
            urllist.append(url + tag.a['href'])

        return urllist

    else:
        print(r.status_code)
        r.close()


domain = 'https://www.concretedisciples.com'

fieldnames = ['Skatepark Name', 'Lights', 'Riding Surface?', 'Address', 'Postal Code', 'City',
              'Directions', 'Size (square footage, no comma)', 'Open / Closed', 'Free or Pay',
              'Inside or Outside', 'Managment', 'BMX', 'Are Pads Required?',
              'Is there a pro shop on site?', 'Phone Number', 'Website', 'Email', 'Restrooms',
              'Designer', 'Builder', 'Opening Date', 'Extra Info']

filename = 'C:/data/skateparks1.csv'

# with open(filename, 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()

data = []

for i in range(1, 2):
    url_list = urllist_get(domain, i, 50)



for row in data:
    print(row)
