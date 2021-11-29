from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Softwares\\geckodriver-v0.30.0-win64\\geckodriver.exe")
driver.get("http://amazon.in")
print(driver.current_url)
print(driver.title)
