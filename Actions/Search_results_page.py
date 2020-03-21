from ToolBox import ToolBox


def  result(value):
    return "//h2[text()='"+value+"']"


class Search_Result_Page:
    main_title = "//h1[contains(text(),'Search results')]"

    def __init__(self, web_browser):
        self.App = ToolBox(web_browser)

    def validate_page_result_hoodies(self):
        self.App.assert_element_present(self.main_title)
        self.App.assert_element_present(result("Hoodie"))
        self.App.assert_element_present(result("Hoodie with Zipper"))
        self.App.assert_element_present(result("Hoodie with Logo"))
        self.App.assert_element_present(result("Hoodie with Pocket"))

    def click_on_result(self, value):
        self.App.click_on(result(value))
