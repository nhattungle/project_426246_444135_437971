'''
The scraping of data is done on the basis of scrapy framework.
This file supports the transfer of data from the "product_details.csv" file into the database in preparation for further evaluation steps.
'''

from ProductModel import Product
from ProductDAO import *

try:
    with open("scrapy_project/product_details.csv", "rt") as f:
        lines = [url.strip() for url in f.readlines()][1:]
        for line in lines:
            #category,image_url,number_of_product_in_a_package,price_gross,price_net,product_title,product_url,quantity_in_stock,size,status
            try:
                data = line.split(",")
                category = "" + data[0]
                image_url = "" + data[1]
                number_of_product_in_a_package = int("0"+data[2])
                price_gross= data[3].replace("\"", "")+"."+data[4].replace("\"", "")
                price_gross = price_gross.replace(",", ".")
                price_net = data[5].replace("\"", "")+"."+data[6].replace("\"", "")
                price_net = price_net.replace(",", ".")
                product_title= "" + data[7]
                product_url = "" + data[8]
                quantity_in_stock= int("0" +data[9])
                size = "" + data[10]
                status= data[11] + ""
               
                product = Product(product_title, price_net, price_gross, quantity_in_stock, number_of_product_in_a_package,
                                          size, status, category, product_url, image_url)

                print(product.toString())
                poduct_check_exit = ProductScrapyDAO.findOne(
                    product_title)

                if(poduct_check_exit is None):
                    ProductScrapyDAO.insert(product)
                else:
                    ProductScrapyDAO.update(product)
            except Exception as e:
                print(e)
except Exception as e:
    print(e)
