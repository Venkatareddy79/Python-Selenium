from selenium.webdriver.common.by import By


class Confirmation_Page:

    def __init__(self, driver):
        self.driver = driver
    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    conf_checkout = (By.XPATH, "//button[@class='btn btn-success']")
    # driver.find_element(By.ID, "country")
    send_country = (By.ID, "country")
    # driver.find_element(By.LINK_TEXT, "India")
    click_india = (By.LINK_TEXT, "India")
    ele_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # driver.find_element(By.XPATH, "//input[@type='submit']")
    submit = (By.XPATH, "//input[@type='submit']")
    # driver.find_element(By.CSS_SELECTOR, "[class*='alert']")
    taking_alert = (By.CSS_SELECTOR, "[class*='alert']")

    def confirmation_checkout(self):
        return self.driver.find_element(*Confirmation_Page.conf_checkout)

    def send_Country(self):
        return self.driver.find_element(*Confirmation_Page.send_country)

    def click_India(self):
        return self.driver.find_element(*Confirmation_Page.click_india)

    def ele_Checkbox(self):
        return  self.driver.find_element(*Confirmation_Page.ele_checkbox)

    def Submit(self):
        return self.driver.find_element(*Confirmation_Page.submit)

    def get_Alert(self):
        return self.driver.find_element(*Confirmation_Page.taking_alert)
