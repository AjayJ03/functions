from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver= webdriver.Chrome()
driver.get(f"file:///D:/selewebsites/loading.html")
driver.maximize_window()

class _visibility_of_element_located(visibility_of_element_located):
    
    def __init__(self, locator):
        super().__init__(locator)  # initializing parent class constructor
    
    def __call__(self,driver):
#         """over riding __call__ method of parent class for
#         checking whether the element is enabled or not"""
        res=super().__call__(driver)
        if isinstance (res, WebElement):
            return res.is_enabled()
        else:
            return False
        

w=WebDriverWait(driver,10)
v=_visibility_of_element_located(("name", "fname"))
w.until(v)
driver.find_element("name", "fname").send_keys("hello")