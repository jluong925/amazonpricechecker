import requests
from bs4 import BeautifulSoup
import time
import smtplib

URL= input("Enter URL of Amazon Product: ")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
goodPrice = input("Enter the desired price: ")
f = open("email.txt", "r")
email_address = f.readlines()
username = email_address[0]
password = email_address[1]
f.close()

def trackPrice():
    price = int(getPrice(URL))
    if price > int(goodPrice):
        diff = price - int(goodPrice)
        print(f"It's still ${diff} too expensive!!")
    else:
        print("Its cheaper!")
        sendMail()

def getPrice(URL):
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="title_feature_div").get_text().strip()
    price = soup.find(id="unifiedPrice_feature_div").get_text().strip()[1:4]
    print(title)
    print("$",price)
    return price

def sendMail():
    subject = "Amazon Price Has Dropped!"
    mailText = "Subject:"+subject+'\n\n'+URL
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(username,password,mailText)
    print("Sent email")


if __name__ == "__main__":
    while True:
        trackPrice()
        time.sleep(21600)