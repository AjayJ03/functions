from common_actions import Actions
from selenium.webdriver import Chrome

# from config import Config

driver=Chrome("D:\Aj Files\_pytest\chromedriver.exe")
driver.get('http://demowebshop.tricentis.com/login')
driver.maximize_window()

s=Actions(driver)
s.enter_text(("id", "Email"),value="ajaydevmsd07@gmail.com")
s.enter_text(("id", "Password"),value= "ajiihj07")
s.click_element(("xpath", "//input[@value='Log in']"))