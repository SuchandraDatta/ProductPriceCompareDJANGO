**PRODUCT PRICE COMPARISON USING URLLIB, BEAUTIFULSOUP AND DJANGO**

![screen2](https://user-images.githubusercontent.com/41965125/70683460-7c241d80-1cc8-11ea-954b-c8b713168510.png)
An attempt is made to create an application which prompts the user to input a product's name, company and model number. Based on these
inputs web scraping is performed to extract the price of the named product from e-commerce sites. 
The first step is to obtain the links to the product. For that we use google library for Python as it's better and safer to use the API. 
Once links are obtained we get the HTML for the page using urllib which is slow so better to use other libraries like resposne or something similar. Once the HTML is obtained we quickly parse it using BeautifulSoup's lxml parser. We can use methods 
to extract terms like div and CSS classes explicitly. Once the required elements are parsed we apply regex to extract the price. 
The entire application is showcased using Django Python framework, taking input via a Django form.
![screen1](https://user-images.githubusercontent.com/41965125/70683596-ef2d9400-1cc8-11ea-8006-3f5e959478c9.png)

Libraries and installations needed-->
1. Python 3.6.8
2. Django(pip install django)
3. Urllib
4. BeautifulSoup4
5. googlesearch library to query Gooogle(pip install google)
6. crispy_forms for forms for styling
7. django_widget_tweaks(pip install django-widget-tweaks)
