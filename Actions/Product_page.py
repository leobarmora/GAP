from ToolBox import ToolBox


class ProductPage:
    main_title = "//h1[@class='product_title entry-title']"
    priceValue = "//p[@class='price']//span"
    input_qty = "//input[@type='number']"
    button_add = "//button[@name='add-to-cart']"

    def __init__(self, web_browser, url):
        self.App = ToolBox(web_browser)
        self.url = url

    def go_to_page(self):
        self.App.go_to_url(self.url)

    def validate_page(self, name, price):
        self.App.assert_element_by_value(self.main_title, name)
        self.App.assert_element_by_value(self.priceValue, price)

    def increase_qty(self, qty_value):
        self.App.clean_input(self.input_qty)
        self.App.type_value(self.input_qty, qty_value)

    def click_add_button(self):
        self.App.click_on(self.button_add)
