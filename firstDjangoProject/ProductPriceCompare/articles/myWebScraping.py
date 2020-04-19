import urllib.request
import requests
from bs4 import BeautifulSoup
import re
priceList=[]
def forAmazon(objForHtmlParsing):
	allID=objForHtmlParsing.find_all(id="priceblock_dealprice")#returning as a list priceblock_dealprice
	print(allID)
	if(len(allID)==0):
		allID=objForHtmlParsing.find_all(id="priceblock_ourprice")
		print(allID)
	if(len(allID)==0):
		allID=objForHtmlParsing.find_all("span")
	price=re.findall(r'₹[\s]*[0-9]+\,*[0-9]+\.[0-9]+', str(allID))
	priceList.append(price[0][2:])
	print("Price on Amazon: ₹" ,price[0][2:])

def forFlipkart(objForHtmlParsing):
	allTheText=objForHtmlParsing.div.get_text()
	price=re.findall(r'₹[0-9]+\,*[0-9]*₹', str(allTheText))
	priceList.append(price[0][:-1])
	print("Price on FLipkart: ", price[0][:-1])

def forebay(objForHtmlParsing):
	#print(objForHtmlParsing.find_all("span"))
	allTheSpans=objForHtmlParsing.find_all("span")
	if(len(allTheSpans)==0):
		allTheSpans=objForHtmlParsing.find_all("class=display-price")
	#print(allTheSpans)
	price=re.findall(r'INR\s+[0-9]+\,*[0-9]+\.[0-9]+', str(allTheSpans))
	priceList.append(price[0])
	print("Price on ebay: ", price[0])

def generateUrl(siteName, itemName,companyName, modelNumber):
	urlToOpen=siteName+itemName+companyName+modelNumber
	retrievedLinks=[]
	from googlesearch import search
	for j in search(urlToOpen, tld="com", lang='en',num=10, start=0, stop=1, pause=5):
		retrievedLinks.append(j)
	something=re.findall(r'https://www\.amazon\.in/[^\"]*', str(retrievedLinks[0]))
	if(len(something)==0):
		something=re.findall(r'https://www\.flipkart\.com/[^\"]+', str(retrievedLinks[0]))
	if(len(something)==0):
		something=re.findall(r'https://www\.ebay\.com/[^\"]*', str(retrievedLinks[0]))
	if(len(something)>0):
		print("We got", str(something[0]))
	#something=str(something[0][6:len(something[0])])
	#something='\''+something+'\''
	return str(something[0])

def startScraping(itemName, companyName, modelNumber):
 userAgent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

 urlList=[]

 urlList.append(generateUrl('amazon', itemName, companyName, modelNumber))
 urlList.append(generateUrl('flipkart', itemName, companyName, modelNumber))
 urlList.append(generateUrl('ebay', itemName, companyName, modelNumber))
 print(urlList)
 print(type(urlList[0]))
#generateUrl()
#urlList.append(url2)
#urlList.append(url4)
#urlList.append(url1)
#urlList=generateUrl()
#print(urlList)
#urlList.append(generateUrl())
 for url in urlList:
  obj=urllib.request.Request(url, headers={'User-Agent': userAgent})
  try:
  	with urllib.request.urlopen(obj) as response:
   		whatWeGetFromPage=response.read()
  	objForHtmlParsing=BeautifulSoup(whatWeGetFromPage, 'lxml')
  	if(re.findall(r'/www.amazon.in/', url)):
   		forAmazon(objForHtmlParsing)
  	elif(re.findall(r'/www.flipkart.com/', url)):
   		forFlipkart(objForHtmlParsing)
   		print("We doing flipkart")
  	elif(re.findall(r'/www.ebay.com/', url)):
   		forebay(objForHtmlParsing)
  except:
	print("Connection error")
  print(priceList)
 return priceList
