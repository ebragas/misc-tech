# pylint: disable=invalid-name
# pylint: disable=C0111

import requests
from bs4 import BeautifulSoup

def getProfile(url):
    """
    Input: url, url of Tesla Supercharger profile page
    Returns dictionary of available data points
    """
    print(url)  # testing
    data = {}

    # Request profile and check for success
    r = requests.get(url)
    if r.status_code == 200:

        # Parse response
        soup = BeautifulSoup(r.text, 'lxml')

        # Coming soon
        if soup.find('span', {'class': 'coming-soon'}):
            data['coming_soon'] = soup.find('span', {'class': 'coming-soon'}).text
        else:
            data['coming_soon'] = 'Open'

        print(data['coming_soon'])

        # Name
        h1 = soup.find_all('h1')
        data['name'] = h1[-1].text
        print(data['name'])  # testing

        # Address name
        data['address_name'] = soup.find('span', {'class': 'common-name'}).text
        print(data['address_name']) # testing

        # Street address
        data['street_address'] = soup.find('span', {'class': 'street-address'}).text
        print(data['street_address']) # testing

        # Extended address
        data['extended_address'] = soup.find('span', {'class': 'extended-address'}).text
        print(data['extended_address']) # testing

        # Locality
        data['locality'] = soup.find('span', {'class': 'locality'}).text
        print(data['locality']) # testing

        

    # Exit gracefully
    else:
        print("Request:", url, "failed with code:", r.status_code)

    return {}


profile_urls = [r'https://www.tesla.com/findus/location/supercharger/athensalsupercharger',
                r'https://www.tesla.com/findus/location/supercharger/paysonsupercharger',
                r'https://www.tesla.com/findus/location/supercharger/elcentrosupercharger']

for url in profile_urls:
    getProfile(url)
