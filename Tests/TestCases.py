from Actions.Homepage import Homepage
from Actions.Product_page import ProductPage
from Actions.Cart_page import CartPage
from Actions.Search_results_page import Search_Result_Page


class TestCases:

    def __init__(self, browser, url):
        self.product_page = ProductPage(browser, url+"/product/leonardo/")
        self.driver = browser
        self.cart_page = CartPage(browser, url)
        self.homepage = Homepage(browser, url)
        self.search_results = Search_Result_Page(browser)

    def test1(self):
        print("Run for Automated Test Case 1")
        try:
            product_name = "Leonardo"
            product_price = 19.99
            product_qty = 7
            self.product_page.go_to_page()
            self.product_page.validate_page(product_name, "$"+product_price.__str__())
            self.product_page.increase_qty("7")
            self.product_page.click_add_button()
            self.cart_page.go_to_page()
            self.cart_page.validate_product(product_name, product_price, product_qty)
            print("Test Passed Successfully\n")

        except AssertionError:
            print("Error: Assertion Error")
            print("Test Failed\n")

    def test2(self):
        print("Run for Automated Test Case 2")
        try:
            search_value = "Hoodie"
            product_name = "Hoodie with Pocket"
            product_price = "45.00"

            self.homepage.go_to_homepage()
            self.homepage.validate_page()
            self.homepage.type_on_search_field(search_value)
            self.search_results.validate_page_result_hoodies()
            self.search_results.click_on_result(product_name)
            self.product_page.validate_page(product_name, "$"+product_price)

            print("Test Passed Successfully")

        except AssertionError:
            print("Error: Assertion Error")
            print("Test Failed")
