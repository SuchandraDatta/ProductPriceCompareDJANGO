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
	#MY ACTUAL USER-AGENT
	#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36

	#url5='https://www.google.com/search?q=mouse+logitech+M337'
	#url5='https://www.google.com/search?q=amazon+keyboard+MK345'
	#url5='https://duckduckgo.com/?q=amazon+mouse+M377'
	userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
	urlToOpen='https://www.google.com/search?q='+siteName+itemName+companyName+modelNumber
	obj=urllib.request.Request(urlToOpen, headers={'User-Agent': userAgent})
	with urllib.request.urlopen(obj) as response:
		whatWeGetFromPage=response.read()
	objForHtmlParsing=BeautifulSoup(whatWeGetFromPage, 'lxml')
	allTheAnchors=objForHtmlParsing.find_all("a")
	#allTheAnchors=['<a class="sXtWJb" href="https://www.amazon.in/LG-Fully-Automatic-Loading-Washing-FHT1207SWL-ALSPEIL/dp/B07DFT4J86" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.amazon.in/LG-Fully-Automatic-Loading-Washing-FHT1207SWL-ALSPEIL/dp/B07DFT4J86&amp;ved=2ahUKEwjUnaTs2o_mAhWzyDgGHc8KBN8QFjACegQIEBAI&amp;usg=AOvVaw0VxXTjiSiyQbY0DX12HFqK" oncontextmenu="google.ctpacw.cm(this)"><span class="S3Uucc">LG 7 kg Inverter Fully-Automatic Front Loading Washing Machine (FHT1207SWL.ALSPEIL, Silver, Inbuilt Heater): Amazon.in: Home &amp; Kitchen</span></a>']
	count=0
	for eachLink in allTheAnchors:
				something=re.findall(r'href=\"https://www\.amazon\.in/[^\"]*', str(eachLink))
				if(len(something)==0):
					something=re.findall(r'href=\"https://www\.flipkart\.com/[^\"]+', str(eachLink))
				if(len(something)==0):
					something=re.findall(r'href=\"https://www\.ebay\.com/[^\"]*', str(eachLink))
				
				if(len(something)>0):
					print(something)
					
				#	count=count+1
				#if(count==1 and siteName!='ebay'):
				#		break
					count=count+1
					if(count==2):
						break
	something=str(something[0][6:len(something[0])])
	#something='\''+something+'\''
	return something
		#print(objForHtmlParsing)

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
 print(priceList)
 return priceList