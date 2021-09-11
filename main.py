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

sold_out_count = 6
sold_out_string = 'Sold Out'

coming_soon_count = 2
coming_soon_string = 'Coming Soon'

sold_out_count3080 = 13
sold_out_string3080 = 'Sold Out'

coming_soon_count3080 = 1
coming_soon_string3080 = 'Coming Soon'

while True:
    res = requests.get(r'https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&sc=Global&st=3070&type=page&usc=All%20Categories',
                       headers={'User-agent': 'Mozilla/5.0'})

    time.sleep(30 + (random.random() * 10))

    res3080 = requests.get(
        r'https://www.bestbuy.com/site/searchpage.jsp?st=3080&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys',
        headers={'User-agent': 'Mozilla/5.0'})


    # file = open("html.txt", "w")
    # file.write(res.text)
    # html = open('html.txt', 'r')
    soup3070 = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')

    buttons3070 = soup3070.find_all('button')

    equals_name_count = 0
    equals_name_count3080 = 0

    for button in buttons3070:
        if button.text == sold_out_string or button.text == coming_soon_string:
            equals_name_count += 1

    soup3080 = BeautifulSoup(res3080.content, 'lxml', from_encoding='utf-8')

    buttons3080 = soup3080.find_all('button')

    for button in buttons3080:
        if button.text == sold_out_string3080 or button.text == coming_soon_string3080:
            equals_name_count3080 += 1

    text_bool3070 = True if equals_name_count != 12 else False
    text_bool3080 = True if equals_name_count3080 != 14 else False

    if text_bool3070:
        message = client.messages \
                        .create(
                             body="3070 3070 CHANGE ON BEST BUY.com HURRY GO BUY",
                             from_='+13074639542',
                             to='+your phone number'
                         )

        print(message.sid)

        raise Exception('program done')

    if text_bool3080:
        message = client.messages \
                        .create(
                             body="3080 3080 CHANGE ON BEST BUY.com HURRY GO BUY",
                             from_='+13074639542',
                             to='+your phone number'
                         )

        print(message.sid)

        raise Exception('program done')

    time.sleep(60 + (random.random() * 10))
