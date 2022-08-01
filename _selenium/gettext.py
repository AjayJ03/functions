from selenium.webdriver import Chrome
driver=Chrome(r"D:\Aj Files\_selenium\chromedriver.exe")
driver.get(r'https://www.python.org/')
driver.maximize_window()

links=driver.find_elements_by_xpath("//a")

# for link in links:
#     print(link.get_attribute("href"))   # [getting attribute value (links)]

for link in links:
    alllinks=link.text
    if "Python" in alllinks:    # [getting all texts if the 'Python' is matched]
        print(alllinks)
print(len(alllinks))