from selenium import webdriver

from Tests.TestCases import TestCases


driver = webdriver.Chrome("../GAP/drivers/chromedriver.exe")
test_auto = TestCases(driver, "http://34.205.174.166/")
test_auto.test1()
test_auto.test2()
driver.quit()
