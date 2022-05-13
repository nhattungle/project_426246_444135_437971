from DBConnection import Connection
from ProductModel import Product

# ProductBeautifulsoup Data access object #################################
class ProductBeautifulsoupDAO:
    @staticmethod
    def createObject(result):
        rs = result
        obj = Product(rs[0], rs[1], rs[2], rs[3], rs[4],
                      rs[5], rs[6], rs[7], rs[8], rs[9])
        return obj

    @staticmethod
    def listByQuery(sql):
        listOut = []
        conn = Connection.getConnection()
        c = conn.cursor()
        c.execute(sql)
        results = c.fetchall()
        for result in results:
            listOut.append(ProductBeautifulsoupDAO.createObject(result))
        for obj in listOut:
            print(obj.toString())
        return listOut

    @staticmethod
    def listAll():
        return ProductBeautifulsoupDAO.listByQuery("SELECT * FROM product_beautifulsoup")

    @staticmethod
    def listByCondition(column, value):
        if (isinstance(value, str)):
            return ProductBeautifulsoupDAO.listByQuery(
                """SELECT * FROM product_beautifulsoup WHERE {0}='{1}'"""
                .format(column, value)
            )
        else:
            return ProductBeautifulsoupDAO.listByQuery(
                """SELECT * FROM product_beautifulsoup WHERE {0}='{1}'"""
                .format(column, str(value))
            )

    @staticmethod
    def insert(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                INSERT INTO product_beautifulsoup
                VALUES ('{0}', {1}, {2}, {3}, {4}, '{5}', '{6}','{7}', '{8}','{9}')
            """
            c.execute(sql.format(
                obj.product_title,
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            return rowcount

    @staticmethod
    def update(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                UPDATE product_beautifulsoup
                SET price_net={0},
                    price_gross={1},
                    quantity_in_stock={2}, 
                    number_of_product_in_a_package={3},
                    size='{4}',
                    status='{5}',
                    category='{6}',
                    product_url='{7}',
                    image_url='{8}'
                WHERE product_title='{9}'
            """
            c.execute(sql.format(
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url,
                obj.product_title))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            return rowcount

    @staticmethod
    def delete(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                DELETE FROM product_beautifulsoup
                WHERE product_title='{0}'
            """
            # print(sql.format(obj.product_title))
            c.execute(sql.format(obj.product_title))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            # print(rowcount)
            return rowcount

    @staticmethod
    def findOne(id):
        listObj = ProductBeautifulsoupDAO.listByQuery(
            "select * from product_beautifulsoup where product_title='{0}'".format(id))
        if (len(listObj) > 0):
            return listObj[0]
        else:
            return None

######################################################################################################

class ProductSeleniumDAO:
    @staticmethod
    def createObject(result):
        rs = result
        obj = Product(rs[0], rs[1], rs[2], rs[3], rs[4],
                      rs[5], rs[6], rs[7], rs[8], rs[9])
        return obj

    @staticmethod
    def listByQuery(sql):
        listOut = []
        conn = Connection.getConnection()
        c = conn.cursor()
        c.execute(sql)
        results = c.fetchall()
        for result in results:
            listOut.append(ProductSeleniumDAO.createObject(result))
        for obj in listOut:
            print(obj.toString())
        return listOut

    @staticmethod
    def listAll():
        return ProductSeleniumDAO.listByQuery("SELECT * FROM product_selenium")

    @staticmethod
    def listByCondition(column, value):
        if (isinstance(value, str)):
            return ProductSeleniumDAO.listByQuery(
                """SELECT * FROM product_selenium WHERE {0}='{1}'"""
                .format(column, value)
            )
        else:
            return ProductSeleniumDAO.listByQuery(
                """SELECT * FROM product_selenium WHERE {0}='{1}'"""
                .format(column, str(value))
            )

    @staticmethod
    def insert(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                INSERT INTO product_selenium(product_title, price_net, price_gross, quantity_in_stock, number_of_product_in_a_package, size, status, category, product_url, image_url)
                VALUES ('{0}','{1}', '{2}', '{3}', '{4}', '{5}', '{6}','{7}', '{8}','{9}')
            """
            print(sql.format(
                obj.product_title,
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url))
            c.execute(sql.format(
                obj.product_title,
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            return rowcount

    @staticmethod
    def update(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                UPDATE product_selenium
                SET price_net={0},
                    price_gross={1},
                    quantity_in_stock={2}, 
                    number_of_product_in_a_package={3},
                    size='{4}',
                    status='{5}',
                    category='{6}',
                    product_url='{7}',
                    image_url='{8}'
                WHERE product_title='{9}'
            """
            print(sql.format(
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url,
                obj.product_title))
            c.execute(sql.format(
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url,
                obj.product_title))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            return rowcount

    @staticmethod
    def delete(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                DELETE FROM product_selenium
                WHERE product_title='{0}'
            """
            # print(sql.format(obj.product_title))
            c.execute(sql.format(obj.product_title))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            # print(rowcount)
            return rowcount

    @staticmethod
    def findOne(id):
        listObj = ProductSeleniumDAO.listByQuery(
            "select * from product_selenium where product_title='{0}'".format(id))
        if (len(listObj) > 0):
            return listObj[0]
        else:
            return None

######################################################################################################

class ProductScrapyDAO:
    @staticmethod
    def createObject(result):
        rs = result
        obj = Product(rs[0], rs[1], rs[2], rs[3], rs[4],
                      rs[5], rs[6], rs[7], rs[8], rs[9])
        return obj

    @staticmethod
    def listByQuery(sql):
        listOut = []
        conn = Connection.getConnection()
        c = conn.cursor()
        c.execute(sql)
        results = c.fetchall()
        for result in results:
            listOut.append(ProductScrapyDAO.createObject(result))
        for obj in listOut:
            print(obj.toString())
        return listOut

    @staticmethod
    def listAll():
        return ProductScrapyDAO.listByQuery("SELECT * FROM product_scrapy")

    @staticmethod
    def listByCondition(column, value):
        if (isinstance(value, str)):
            return ProductScrapyDAO.listByQuery(
                """SELECT * FROM product_scrapy WHERE {0}='{1}'"""
                .format(column, value)
            )
        else:
            return ProductScrapyDAO.listByQuery(
                """SELECT * FROM product_scrapy WHERE {0}='{1}'"""
                .format(column, str(value))
            )

    @staticmethod
    def insert(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                INSERT INTO product_scrapy(product_title, price_net, price_gross, quantity_in_stock, number_of_product_in_a_package, size, status, category, product_url, image_url)
                VALUES ('{0}','{1}', '{2}', '{3}', '{4}', '{5}', '{6}','{7}', '{8}','{9}')
            """
            print(sql.format(
                obj.product_title,
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url))
            c.execute(sql.format(
                obj.product_title,
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            return rowcount

    @staticmethod
    def update(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                UPDATE product_scrapy
                SET price_net={0},
                    price_gross={1},
                    quantity_in_stock={2}, 
                    number_of_product_in_a_package={3},
                    size='{4}',
                    status='{5}',
                    category='{6}',
                    product_url='{7}',
                    image_url='{8}'
                WHERE product_title='{9}'
            """
            print(sql.format(
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url,
                obj.product_title))
            c.execute(sql.format(
                obj.price_net,
                obj.price_gross,
                obj.quantity_in_stock,
                obj.number_of_product_in_a_package,
                obj.size,
                obj.status,
                obj.category,
                obj.product_url,
                obj.image_url,
                obj.product_title))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            return rowcount

    @staticmethod
    def delete(obj):
        if (isinstance(obj, Product)):
            conn = Connection.getConnection()
            c = conn.cursor()
            sql = """
                DELETE FROM product_scrapy
                WHERE product_title='{0}'
            """
            # print(sql.format(obj.product_title))
            c.execute(sql.format(obj.product_title))
            rowcount = c.rowcount
            conn.commit()
            conn.close()
            # print(rowcount)
            return rowcount

    @staticmethod
    def findOne(id):
        listObj = ProductScrapyDAO.listByQuery(
            "select * from product_scrapy where product_title='{0}'".format(id))
        if (len(listObj) > 0):
            return listObj[0]
        else:
            return None

######################################################################################################

