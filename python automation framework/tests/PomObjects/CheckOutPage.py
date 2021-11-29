from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']/div/h4")
    items = (By.XPATH, "//div[@class='card h-100']/div/h4")
    # driver.find_element(By.XPATH, "//div[@class='card-footer']/button")
    add_button = (By.XPATH, "//div[@class='card-footer']/button")
    check_out = (By.XPATH, "//ul[@class='navbar-nav ml-auto']")

    def items_gadgets(self):
        return self.driver.find_elements(*CheckOutPage.items)

    def card_footer(self):
        return self.driver.find_element(*CheckOutPage.add_button)

    def checkOut(self):
        return self.driver.find_element(*CheckOutPage.check_out)