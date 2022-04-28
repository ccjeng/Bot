import sys
import os
import random
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import datetime


count=1200

target="https://ibackup1230.pixnet.net/blog"
timeout=100 
stay=5
def req(proxy_url,target_url,timeo,stay_time):
 r=requests.get(proxy_url)
 soup=BeautifulSoup(r.content,'html.parser')
 list = soup.find(class_='table table-striped table-bordered')
 list1 = list.findAll('td')
 iplist=[]
 portlist=[]
 codelist=[]
 countrylist=[]
 j=0
 while(j<(8*count)):
  try:
   a=str(list1[j].contents[0])
   iplist.append(a)
   j=j+8
  except:
   break
 j=1
 while(j<(8*count)):
  try:
   a=str(list1[j].contents[0])
   portlist.append(a)
   j=j+8
  except:
   break
 j=2
 while(j<(8*count)):
  try:
   a=str(list1[j].contents[0])
   codelist.append(a)
   j=j+8
  except:
   break
 j=3
 while(j<(8*count)):
  try:
   a=str(list1[j].contents[0])
   countrylist.append(a)
   j=j+8
  except:
   break
 counter=0   
 for index in range (0,(len(iplist)-1)): 
  try:   
   PROXY=iplist[index]+":"+portlist[index]
   #if codelist[index]=="TH" or codelist[index]=="SG" or codelist[index]=="HK" or codelist[index]=="CN" or codelist[index]=="IN" or codelist[index]=="IR" or codelist[index]=="ID" or codelist[index]=="JP":
   counter=counter+1
   print("\033[1;32;40m"+"#"+str(counter)+" "+str(datetime.datetime.now())+" Trying From "+str(PROXY)+" ("+countrylist[index]+")")
   webdriver.DesiredCapabilities.FIREFOX['proxy']={"httpProxy":PROXY,"sslProxy":PROXY,"proxyType":"MANUAL"}
   driver=webdriver.Firefox()
   driver.set_page_load_timeout(timeo)
   driver.get(target_url)
   time.sleep(stay_time)
   driver.close()
  except Exception as e: 
    driver.close()

#target=input("\033[1;33;40mEnter The Target URL(Ex: https://www.google.com) :")
timeout=int(input("\033[1;33;40mEnter The Time Out(In Seconds)(Recommended 100) :"))
#stay=int(input("\033[1;33;40mEnter The Stay Time(In Seconds) :"))
urllist=["https://www.sslproxies.org","https://free-proxy-list.net/anonymous-proxy.html","https://free-proxy-list.net","https://www.socks-proxy.net","https://us-proxy.org","https://free-proxy-list.net/uk-proxy.html"]

print("\n\033[1;32;40mTarget Site: "+target+", Timeout: "+str(timeout)+"\n") 
for purl in urllist:
 req(purl,target,timeout,stay)
 print("\033[1;32;40mSleeping For 3 Seconds")
 time.sleep(3)
 
