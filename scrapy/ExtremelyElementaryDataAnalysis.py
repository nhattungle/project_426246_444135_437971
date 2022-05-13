from itertools import product
import pandas as pd
import matplotlib.pyplot as plt
from ProductModel import Product
from ProductDAO import *


list_product_selenium = ProductSeleniumDAO.listAll()
list_product_scrapy = ProductScrapyDAO.listAll()

# Histogram based on product price net (from table Product BeautifulSoup)
list_product_beautifulsoup =  ProductBeautifulsoupDAO.listAll()
data_price_net_product_beautifulsoup = []
for product in list_product_beautifulsoup:
    data_price_net_product_beautifulsoup.append(product.price_net)

# define window size, output and axes
fig, ax = plt.subplots(figsize=[8,6])
# set plot title
ax.set_title("Histogram based on product price net (from table Product BeautifulSoup)")
# set x-axis name
ax.set_xlabel("Price Net")
# set y-axis name
ax.set_ylabel("Quantity")
# create histogram within output
N, bins, patches = ax.hist(data_price_net_product_beautifulsoup) 
plt.show()


# Histogram based on product price net (from table Product BeautifulSoup)
list_product_selenium =  ProductSeleniumDAO.listAll()
data_price_net_product_selenium = []
for product in list_product_selenium:
    data_price_net_product_selenium.append(product.price_net)

# define window size, output and axes
fig, ax = plt.subplots(figsize=[8,6])
# set plot title
ax.set_title("Histogram based on product price net (from table Product Selenium)")
# set x-axis name
ax.set_xlabel("Price Net")
# set y-axis name
ax.set_ylabel("Quantity")
# create histogram within output
N, bins, patches = ax.hist(data_price_net_product_beautifulsoup) 
plt.show()

# Histogram based on product price net (from table Product BeautifulSoup)
list_product_scrapy =  ProductScrapyDAO.listAll()
data_price_net_product_scrapy= []
for product in list_product_scrapy:
    data_price_net_product_scrapy.append(product.price_net)

# define window size, output and axes
fig, ax = plt.subplots(figsize=[8,6])
# set plot title
ax.set_title("Histogram based on product price net (from table Product Scrapy)")
# set x-axis name
ax.set_xlabel("Price Net")
# set y-axis name
ax.set_ylabel("Quantity")
# create histogram within output
N, bins, patches = ax.hist(data_price_net_product_beautifulsoup) 
plt.show()

