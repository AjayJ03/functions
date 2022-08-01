import imp
from selenium import webdriver
driver=webdriver.Chrome('./chromedriver')
driver.get(r"D:\Aj Files\New folder (2)\files\demo.html")
driver.maximize_window()
# a=driver.find_element_by_xpath("//td[text()='Ruby']/..//input[@name='download']")
# a.click()
# b=driver.find_element_by_xpath("//td[text()='C#']/..//input[@name='download']")
# b.click()

languages=['Ruby', 'Python', 'Java', 'C#', 'JavaScript']
for language in languages:
    driver.find_element_by_xpath(f"//td[text()='{language}']/..//input[@name='download']").click()

# c=driver.find_element_by_xpath("//td[text()='Windows']/..//a[text()='Download']")
# c.click()