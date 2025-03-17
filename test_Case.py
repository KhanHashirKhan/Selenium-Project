import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from functions import definedFunctions
from locators import Locators
from data import form


@pytest.fixture(scope="class")
def setup(request):
    """Setup WebDriver once per class"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/webtables")

    request.cls.driver = driver  # Assign WebDriver to the test class
    yield  # Run tests
    driver.quit()  # Close browser after all tests finish


@pytest.mark.usefixtures("setup")
class TestNew:

    def test_text_box(self):

        elm = definedFunctions(self.driver)  # self.driver is now assigned
        lc = Locators
        data = form

        elm.click_on_button(lc.add_btn)
        elm.click_on_button(lc.submit_btn)
        elm.send_keys_by_xpaths(lc.firstName, data.First_NAME)
        time.sleep(2)
        elm.send_keys_by_xpaths(lc.lastName, data.Last_NAME)
        time.sleep(2)
        elm.send_keys_by_xpaths(lc.Email, data.invalid_email)
        time.sleep(1)
        elm.send_keys_by_xpaths(lc.age, data.invalidAge)
        time.sleep(1)
        elm.send_keys_by_xpaths(lc.salary, data.validsalary)
        time.sleep(2)
        elm.send_keys_by_xpaths(lc.department, data.Department_name)
        time.sleep(2)
        elm.clear_text_field(lc.Email)
        time.sleep(2)
        elm.send_keys_by_xpaths(lc.Email, data.valid_email)
        time.sleep(2)
        elm.clear_text_field(lc.age)
        time.sleep(2)
        elm.send_keys_by_xpaths(lc.age, data.validAge)
        time.sleep(2)
        elm.click_on_button(lc.submit_btn)
        time.sleep(2)
        elm.send_keys_by_xpaths(lc.search, data.invalid_Search_name)
        time.sleep(1)
        elm.clear_text_field(lc.search)
        time.sleep(1)
        elm.send_keys_by_xpaths(lc.search, data.valid_Search_name)
        time.sleep(1)
        elm.click_on_button(lc.edit_btn)
        time.sleep(1)
        elm.clear_text_field(lc.salary)
        time.sleep(1)
        elm.send_keys_by_xpaths(lc.salary, data.edit_salary)
        time.sleep(4)
        elm.click_on_button(lc.submit_btn)
        time.sleep(2)
        elm.click_on_button(lc.delete)
        time.sleep(2)
        elm.clear_text_field(lc.search)
        elm.send_keys_by_xpaths(lc.search, data.valid_Search_name)
        time.sleep(2)

    def test_Clic_Button(self):

        elm = definedFunctions(self.driver)
        lc = Locators
        data = form

        elm.click_on_button(lc.side_button)
        elm.double_click_by_xpath(lc.double_btn)
        elm.assert_text_by_xpath(lc.dobuble_btn_text, data.dobuble_text)
        time.sleep(2)
        elm.right_click_by_xpath(lc.right_click_btn)
        elm.assert_text_by_xpath(lc.right_click_btn_text, data.right_click_text)
        time.sleep(2)
        elm.click_on_button(lc.click_me_btn)
        elm.assert_text_by_xpath(lc.click_me_btn_text, data.click_me_text)
        time.sleep(2)


    # def test_Clic_Button(self):
    # 
    #     elm = definedFunctions(self.driver)
    #     lc = Locators
    #     data = form
    #
    #     elm.click_on_button(lc.upload_image)
    #     elm.upload_image(lc.file_btn, data.file_path)
    #     time.sleep(4)