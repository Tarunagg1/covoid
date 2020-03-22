from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "icon.ico",
        timeout = 5
    )
def getdata(url):
    r = requests.get(url)
    return r.text
    
if __name__ == "__main__":
  while True:
    # notifyme("tarun","this is testing")
    myhtmldata = getdata('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myhtmldata, 'html.parser')
    mydatastr = ""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
         mydatastr += tr.get_text()    
    mydatastr = mydatastr[1:]
    itemlist = mydatastr.split("\n\n")
    state = ['Delhi','Andhra Pradesh']
    for item in itemlist[0:23]:
        datalist = item.split('\n')
        # print(datalist)
        if datalist[1] in state:
            print(datalist)
            ntitle = 'cases in covid-19'
            ntext = f"State: {datalist[1]} \n indian: {datalist[2]}\nForeign National: {datalist[3]} \nDeath: {datalist[5]}"
            notifyme(ntitle,ntext) 
    time.sleep(10)
    
    