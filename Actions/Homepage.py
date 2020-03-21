from selenium.webdriver.common.keys import Keys

from ToolBox import ToolBox


class Homepage:
    header_title = "//a[contains(text(),'QA Playground')]"
    main_title = "//h1[contains(text(),'Welcome')]"
    input_search = "//header//input[@class='search-field']"

    def __init__(self,browser, url):
        self.App = ToolBox(browser)
        self.url = url

    def go_to_homepage(self):
        self.App.go_to_url(self.url)

    def validate_page(self):
        self.App.assert_element_present(self.header_title)
        self.App.assert_element_present(self.main_title)
        self.App.assert_element_present(self.input_search)

    def type_on_search_field(self, value):
        self.App.type_value(self.input_search, value)
        self.App.type_value(self.input_search, Keys.ENTER)
