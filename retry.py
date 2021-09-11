from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time
import random


sid = 'sid here'
authtoken = 'auth here'

account_sid = sid
auth_token = authtoken
client = Client(account_sid, auth_token)


def newegg_3070():
    res = requests.get(
        r'https://www.newegg.com/p/pl?d=rtx+3070&LeftPriceRange=400+900',
        headers={'User-agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')

    text = soup.get_text()

    if 'Add to cart' in text:
        print('True')
        return 'newegg_3070  https://www.newegg.com/p/pl?d=rtx+3070&LeftPriceRange=400+900'
    else:
        print('Item not found')


def newegg_3080():
    res = requests.get(
        r'https://www.newegg.com/p/pl?d=rtx+3080&LeftPriceRange=650+1100',
        headers={'User-agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')

    text = soup.get_text()

    if 'Add to cart' in text:
        print('True')
        return 'newegg_3080  https://www.newegg.com/p/pl?d=rtx+3080&LeftPriceRange=650+1100'
    else:
        print('Item not found')


def newegg_ryzen5600():
    res = requests.get(
        r'https://www.newegg.com/p/pl?d=5600x',
        headers={'User-agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')

    text = soup.get_text()

    if 'Add to cart' in text:
        print('True')
        return 'newegg_ryzen5600  https://www.newegg.com/p/pl?d=5600x'
    else:
        print('Item not found')


def bestbuy_3070():
    res = requests.get(
        r'https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&sc=Global&st=3070&type=page&usc=All%20Categories',
        headers={'User-agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')

    text = soup.get_text()

    if 'Add to Cart' in text:
        print('True')
        return 'bestbuy_3070  https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&sc=Global&st=3070&type=page&usc=All%20Categories'
    else:
        print('Item not found')


def all_3070():
    res = requests.get(
        r'https://www.nowinstock.net/computers/videocards/nvidia/rtx3070/')

    soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')

    text = soup.get_text()

    available_index = text.count('In Stock')

    if available_index > 4:
        print('True')
        return '3070all  ' + 'https://www.nowinstock.net/computers/videocards/nvidia/rtx3070/'
    else:
        print('Item not found')


def all_3080():
    url = r'https://www.nowinstock.net/computers/videocards/nvidia/rtx3080/'
    res = requests.get(
        url)

    soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')

    text = soup.get_text()

    available_index = text.count('In Stock')

    if available_index > 11:
        print('True')
        return '3080all  ' + url
    else:
        print('Item not found')


def text(message):
    message = client.messages \
        .create(
        body=message,
        from_='+13074639542',
        to='+1your phone number'
    )

    print(message.sid)


def main(scraper_list):
    message = None
    while True:
        for scraper in scraper_list:
            message = None
            print('using scraper at: ' + str(scraper))
            try:
                message = scraper()
            except requests.exceptions.ConnectionError:
                print('exception: connection error')
                time.sleep(60)
            time.sleep(1)

            if message is not None:
                text(message)

        print('sleeping 30')
        time.sleep(30)





if __name__ == '__main__':
    scraper_list = [newegg_ryzen5600]

    main(scraper_list)