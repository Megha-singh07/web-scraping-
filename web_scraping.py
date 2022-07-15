# perform web scrapping using python on an e-commerce website
from bs4 import BeautifulSoup
import time 
import cloudscraper
import requests
def find_earbuds():
    html_text=requests.get("https://www.amazon.in/s?k=earbuds+bluetoot+wireless&crid=3EZKR5V8MB2IJ&sprefix=%2Caps%2C438&ref=nb_sb_ss_recent_1_0_recent").text
    print(html_text)
    soup=BeautifulSoup(html_text,'lxml')
    ear_buds=soup.find_all('div',class_='sg-col-inner').text
    #print(ear_buds)
    for ear_bud in ear_buds:
        bud_brand = ear_bud.find('h2',class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2').text
        rating = ear_bud.find('i',class_='a-icon a-icon-star-small a-star-small-4 aok-align-bottom').text
        price = ear_bud.find('span',class_ = 'a-price-whole').text
        print(f''' Earbud Name {bud_brand} ''')
        print(f''' rating {rating}''')
        print(f''' price {price}''')
        print('')
    
if __name__ == '__main__':
    while True:
        find_earbuds
        time_wait = 10
        print(f' waiting time {time_wait} minutes...')
        time.sleep(time_wait * 60)
        