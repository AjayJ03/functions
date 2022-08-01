from selenium.webdriver import Chrome
driver=Chrome(r"D:\Aj Files\_selenium\chromedriver.exe")
driver.get(r'D:\Aj Files\New folder (2)\files\demo.html')
driver.maximize_window()

options=driver.find_elements_by_xpath("//input[@name='download']")

for option in options:   # [selecting all checkboxes by using for loop]
    option.click()

for option in options[::-1]:   # [selecting all checkboxes from bottom to top]
    option.click()   