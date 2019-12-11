
**PRODUCT PRICE COMPARISON USING URLLIB, BEAUTIFULSOUP AND DJANGO**

![screen1](https://user-images.githubusercontent.com/41965125/70607794-1af73e00-1c25-11ea-878b-c5c29f6494a9.png)

An attempt is made to create an application which prompts the user to input a product's name, company and model number. Based on these
inputs web scraping is performed to extract the price of the named product from e-commerce sites. 
The first step is to obtain the links to the product. Urllib allows us to perform this however, it is very slow so it is better to use other
libraries like response. Once links are obtained we get the HTML for the page and quickly parse it using BeautifulSoup. We can use methods 
to extract terms like div and CSS classes explicitly. Once the required elements are parsed we apply regex to extract the price. 
The entire application is showcased using Django Python framework, taking input via a Django form.

![screen2](https://user-images.githubusercontent.com/41965125/70607834-2c404a80-1c25-11ea-812a-3518c224f804.png)
