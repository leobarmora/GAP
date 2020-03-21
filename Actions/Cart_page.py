from ToolBox import ToolBox


class CartPage:
    product = "//tr[1]//td[@class='product-name']//a"
    qty_value = "//input[@type='number']"
    price_value = "//td[@class='product-subtotal']//span"

    def __init__(self, web_browser, url):
        self.App = ToolBox(web_browser)
        self.url = url

    def go_to_page(self):
        self.App.go_to_url(self.url+"/cart")

    def validate_product(self, p_name, p_price, p_qty):
        self.App.assert_element_by_value(self.product, p_name)
        subtotal = round(p_price*p_qty, 2)
        print(subtotal)
        self.App.assert_element_by_value(self.price_value, "$"+subtotal.__str__())
        self.App.assert_element_by_attribute(self.qty_value, "value", p_qty)