from lib2to3.pgen2 import driver
from webbrowser import Chrome
from selenium import webdriver
driver=webdriver.Chrome(r"D:\Aj Files\_selenium\chromedriver.exe")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
driver.find_element_by_xpath('//a[@class="ico-register"]').click()