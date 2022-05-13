# set limit number of products to be scraped
limit = True
number_of_limit = 100
#############################################

from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
from ProductModel import Product
from ProductDAO import *

listCategories = ['https://e-roberto.eu/product-category/obuwie-damskie/botki/',
                  'https://e-roberto.eu/product-category/obuwie-damskie/sneakersy/']

# count scaped products
count = 0

for c in listCategories:
    for page in range(1, 101):
        # create link of product page
        url_product_page = c+"page/"+str(page)+"/"
        # print(url_product_page)
        try:
            html = request.urlopen(url_product_page)
            bs = BS(html.read(), 'html.parser')

            # check page is exits
            # check the span has 404: page not found
            check_404 = ''
            try:
                check_404 = bs.find('span', string='404').txt
            except:
                check_404 = ''

            # print("check_404: " + check_404)
            if(check_404 == ''):
                # Get all a link product
                link_temp_list = []
                a_tags = bs.find_all(
                    'a', {'class': 'woocommerce-LoopProduct-link woocommerce-loop-product__link'})

                for link_product_detail in a_tags:
                    # check limit and exit if count > number_of_limit
                    count = count + 1
                    if(limit):
                        if(count > number_of_limit):
                            exit()

                    # scraping product detail
                    html = request.urlopen(link_product_detail['href'])
                    bs = BS(html.read(), 'html.parser')

                    # Product Title
                    try:
                        product_title = bs.find('h1').text
                        product_title = (product_title.rstrip()).lstrip()
                    except Exception as e:
                        product_title = ''

                    # Price Net
                    try:
                        price_net = bs.find('span', {'id': 'gianet'}).text
                    except Exception as e:
                        price_net = ''

                    # Price Gross
                    try:
                        price_gross = bs.find(
                            'span', {'id': 'giabrut'}).text
                    except Exception as e:
                        price_gross = ''

                    # Quantity in stock
                    try:
                        string_quantity_in_stock = bs.find(
                            'p', {'class': 'stock in-stock'}).text
                        array_quantity_in_stock = string_quantity_in_stock.split(
                            " ", 1)
                        quantity_in_stock = array_quantity_in_stock[0]
                    except Exception as e:
                        quantity_in_stock = 0

                    # Number of product in a package
                    try:
                        number_of_product_in_a_package = bs.find(
                            'span', {'id': 'paczka'}).text
                    except Exception as e:
                        number_of_product_in_a_package = 0

                    # Size
                    try:
                        size = bs.find(
                            'span', {'id': 'size'}).text
                    except Exception as e:
                        size = 0

                    # Status
                    try:
                        status = bs.find(
                            'span', {'id': 'XXC'}).next_sibling.next_sibling.text
                    except Exception as e:
                        status = 0

                    # Category
                    try:
                        category = bs.find(
                            'nav', {'class': 'woocommerce-breadcrumb breadcrumbs uppercase'}).text
                    except Exception as e:
                        category = ''

                    # Product Url
                    try:
                        product_url = link_product_detail['href']
                    except Exception as e:
                        product_url = ''

                    # Image Url
                    try:
                        image_url = bs.find(
                            'img', {'class': 'wp-post-image skip-lazy'})['src']
                    except Exception as e:
                        image_url = ''

                    # Insert or Update Product to Database
                    try:
                        product = Product(product_title, price_net, price_gross, quantity_in_stock, number_of_product_in_a_package,
                                          size, status, category, product_url, image_url)

                        poduct_check_exit = ProductBeautifulsoupDAO.findOne(
                            product_title)

                        if(poduct_check_exit is None):
                            ProductBeautifulsoupDAO.insert(product)
                        else:
                            ProductBeautifulsoupDAO.update(product)
                    except Exception as e:
                        print(e)

        except Exception as e:
            print(e)
