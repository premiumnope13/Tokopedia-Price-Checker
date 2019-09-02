import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.tokopedia.com/catalog/51134/nintendo-switch'

headers = {
"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price_today():
    check_price()

    while (True):
        print ("Sleeping........")
        time.sleep(3600 * 24)
        print ("OK Here We Go!1!!1!!1!1")
        




def check_price():


    page = requests.get(URL,headers= headers) 
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", {"class": "_2Ly9D0Pe"}).get_text() #Just Find the title of the product

    priceNow = soup.find("span", {"class": "_3MctVyX0"}).get_text() #Get Price (Selecting by Class)

    priceNow.strip()

    converted_priceNow = priceNow[4:13].replace(",", "", 2) #Change "comma" to "period"
    print (title)
    print ("Today's price is : ",int(converted_priceNow))
    

    if (int(converted_priceNow) > 4540000): #change To abbre
        print ("Check Email Yo, Price is dropping")
        send_mail()

    else:
        print ("Still Not Dropping")
   
   

def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login ('@gmail.com','')

    subject = "Price Change !!"

    body = 'Check here https://www.tokopedia.com/catalog/51134/nintendo-switch'

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        '@gmail.com', #from
        '..h@gmail.com',#to
        msg #payload

    )
    server.quit()


check_price_today()

