class Product:
    # Constructor
    def __init__(self="", product_title="", price_net=0, price_gross=0,
                 quantity_in_stock=0, number_of_product_in_a_package=0,
                 size="", status="", category="", product_url="", image_url=""):
        self.product_title = product_title
        self.price_net = price_net
        self.price_gross = price_gross
        self.quantity_in_stock = quantity_in_stock
        self.number_of_product_in_a_package = number_of_product_in_a_package
        self.size = size
        self.status = status
        self.category = category
        self.product_url = product_url
        self.image_url = image_url

    def printMe(self):
        strMe = """product_title: {0}, price_net: {1}, price_gross: {2},
        quantity_in_stock: {3}, number_of_product_in_a_package: {4}, size: {5},
        status: {6}, category: {7}, product_url: {8}, image_url: {9}
        """.format(
            self.product_title,
            self.price_net,
            self.price_gross,
            self.quantity_in_stock,
            self.number_of_product_in_a_package,
            self.size,
            self.status,
            self.category,
            self.product_url,
            self.image_url)
        print(strMe)

    def toString(self):
        strMe = """product_title: {0}, price_net: {1}, price_gross: {2},
        quantity_in_stock: {3}, number_of_product_in_a_package: {4}, size: {5},
        status: {6}, category: {7}, product_url: {8}, image_url: {9}
        """.format(
            self.product_title,
            self.price_net,
            self.price_gross,
            self.quantity_in_stock,
            self.number_of_product_in_a_package,
            self.size,
            self.status,
            self.category,
            self.product_url,
            self.image_url)
        return strMe


# Test
# obj = Product("A", 10,10,10,10,"M", "OK", "UR1", "URL2")
# obj.printMe()
