import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.tokopedia.com/catalog/51134/nintendo-switch'

headers = {
"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():
    yesterdayPrice = 4520000 #initiate price
    while (True):
        print ("Initiated Price : ",yesterdayPrice)

        page = requests.get(URL,headers= headers) 
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find("h1", {"class": "_2Ly9D0Pe"}).get_text() #Just Find the title of the product

        priceNow = soup.find("span", {"class": "_3MctVyX0"}).get_text() #Get Price (Selecting by Class)

        priceNow.strip()

        converted_priceNow = priceNow[4:13].replace(",", "", 2) #Change "comma" to "period"
        print (title)
        print ("Today's price is : ",int(converted_priceNow))

        compare(int(converted_priceNow),yesterdayPrice)

        if (int(converted_priceNow) < yesterdayPrice): #change To 
            print ("Check Email Yo, Price is dropping")
            send_mail()

        else:
            print ("Still Not Dropping")
        yesterdayPrice = int(converted_priceNow)
        print ("Waits For 12 Hours")
        time.sleep(3600*12) #Report every 12 Hours since program runs for the 1st time 
        

    
def compare(x,y):
    if (x <y):
        print ("Price is dropping !")
    else :
        print ("Still not Changing")


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
        msg

    )
    server.quit()



check_price()
