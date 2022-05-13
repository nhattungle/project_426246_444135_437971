# set limit number of products to be scraped
limit = True
number_of_limit = 100
#############################################

from dataclasses import replace
from xml.dom.minidom import Element
from boto import BUCKET_NAME_RE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os
from ProductModel import Product
from ProductDAO import *


driver = webdriver.Chrome()

# sending file to professor
listCategories = ['https://e-roberto.eu/product-category/obuwie-damskie/botki/',
                  'https://e-roberto.eu/product-category/obuwie-damskie/sneakersy/']

for url in listCategories:
    for page in range(1, 101):
        try:
            url_product_page = url+"page/"+str(page)+"/"
            driver.get(url_product_page)
            time.sleep(2)

            error_404 = False
            try:
                driver.find_element(By.XPATH, '//section[@class="error-404 not-found mt mb"]')
                error_404 = True
            except:
                error_404 = False
            
            print(error_404)

            if (error_404 == False):
                # Get all a link product has class cotains 'woocommerce-LoopProduct-link woocommerce-loop-product__link'
                a_tags = driver.find_elements_by_xpath(
                    '//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]')
                
                list_link_product_details = []
                for atag in a_tags:
                    list_link_product_details.append(atag.get_attribute('href'))

                print(list_link_product_details)

                for link_product_detail in list_link_product_details:
                    # check limit and exit if count > number_of_limit
                    count = count + 1
                    if(limit):
                        if(count > number_of_limit):
                            driver.quit()
                            exit()

                    # scraping product detail
                    driver.get(link_product_detail)
                    time.sleep(2)

                    # Product Title
                    try:
                        product_title = driver.find_element(By.XPATH, '//h1').text
                        product_title = (product_title.rstrip()).lstrip()
                    except Exception as e:
                        product_title = ''

                    # Price Net
                    try:
                        price_net = float((driver.find_element(By.XPATH, '//span[@id="gianet"]').text).replace("," , '.'))
                    except Exception as e:
                        price_net = 0

                    # Price Gross
                    try:
                        price_gross = float((driver.find_element(By.XPATH, '//span[@id="giabrut"]').text).replace("," , '.'))
                    except Exception as e:
                        price_gross = 0

                    # Qquantity in stock
                    try:
                        string_quantity_in_stock = driver.find_element(By.XPATH, '//p[@class="stock in-stock"]').text
                        array_quantity_in_stock = string_quantity_in_stock.split(
                            " ", 1)
                        quantity_in_stock = int(array_quantity_in_stock[0])
                    except Exception as e:
                        quantity_in_stock = 0

                    # Number of product in a package
                    try:
                        number_of_product_in_a_package = int(driver.find_element(By.XPATH, '//span[@id="paczka"]').text)
                    except Exception as e:
                        number_of_product_in_a_package = 0

                    # Size
                    try:
                        size = driver.find_element(By.XPATH, '//span[@id="size"]').text
                    except Exception as e:
                        size = ''

                    # Category
                    try:
                        category = driver.find_element(By.XPATH, '//nav[@class="woocommerce-breadcrumb breadcrumbs uppercase"]').text
                    except Exception as e:
                        category = ''                        

                    # Status
                    try:
                        status = driver.find_element(By.XPATH, '//span[@id="XXC"]/following-sibling::*[1]').text
                    except Exception as e:
                        status = ''

                    # Product Url
                    product_url = link_product_detail

                    # Image Url
                    try:
                        image_url = driver.find_element(By.XPATH, '//img[@class="wp-post-image skip-lazy"]').get_attribute('src')
                    except Exception as e:
                        image_url = ''


                    # Insert or Update Product to Database
                    try:
                        product = Product(product_title, price_net, price_gross, quantity_in_stock, number_of_product_in_a_package,
                                          size, status, category, product_url, image_url)

                        poduct_check_exit = ProductSeleniumDAO.findOne(
                            product_title)

                        if(poduct_check_exit is None):
                            ProductSeleniumDAO.insert(product)
                        else:
                            ProductSeleniumDAO.update(product)
                    except Exception as e:
                        print(e)
            else:
                break
        except Exception as e:
            print(e)
            print("error")
driver.quit()