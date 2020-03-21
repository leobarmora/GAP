from selenium import webdriver


class ToolBox:

    def __init__(self, webBrowser):
        self.driver = webBrowser
        self.driver.set_page_load_timeout(5)

    def go_to_url(self, url):
        self.driver.get(url)
        print("Page open on: " + url)

    def click_on(self, element):
        self.driver.find_element_by_xpath(element).click()
        print("Click on: " + element)

    def end_quit(self):
        self.driver.quit()
        print("Close driver")

    def assert_element_by_value(self, element, value):
        element = self.driver.find_element_by_xpath(element)
        print("Element Text Value: "+element.text)
        assert element.text == value

    def clean_input(self, element):
        self.driver.find_element_by_xpath(element).clear()

    def type_value(self, element, value):
        self.driver.find_element_by_xpath(element).send_keys(value)

    def assert_element_by_attribute(self, element, attribute, value):
        element = self.driver.find_element_by_xpath(element)
        v_attribute = element.get_attribute(attribute)
        print("Got Element Attribute: " + v_attribute)
        assert v_attribute.__str__() == value.__str__()

    def assert_element_present(self, element):
        displaying = self.driver.find_element_by_xpath(element).is_displayed()
        if displaying:
            assert True
