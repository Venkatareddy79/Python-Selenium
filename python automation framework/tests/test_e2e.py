import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from tests.PomObjects.CheckOutPage import CheckOutPage
from tests.PomObjects.ConfirmationPage import Confirmation_Page
from tests.PomObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_one(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        homePage.shopitem().click()
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        items_l = CheckOutPage(self.driver)
        items_list = items_l.items_gadgets()
        for item in items_list:
            if item.text == 'Blackberry':
                items_l.card_footer().click()
                break
        items_l.checkOut().click()
        check_click = Confirmation_Page(self.driver)
        check_click.confirmation_checkout().click()
        check_click.send_Country().send_keys("Ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        check_click.click_India().click()
        check_click.ele_Checkbox().click()
        check_click.Submit().click()
        result = check_click.get_Alert().text
        assert "Success" in result
        self.driver.get_screenshot_as_file("screen.png")
