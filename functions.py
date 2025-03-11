from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class definedFunctions:
    def __init__(self, driver):
        self.driver = driver

    def click_on_button(self, xpath):
        click = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].click();", click)

    def send_keys_by_xpaths(self, xpath, key):
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(key)

    def clear_text_field(self, xpath):
        text_field = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        text_field.clear()

    def click_by_xpath(self, xpath):
        element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def double_click_by_xpath(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        print("Element found:", element.is_displayed())
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).double_click().perform()
        except:
            print("Double-click failed, using JavaScript workaround.")
            self.driver.execute_script(
                "var evt = new MouseEvent('dblclick', {bubbles: true, cancelable: true, view: window}); arguments[0].dispatchEvent(evt);",
                element)

    def right_click_by_xpath(self, xpath):
        element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).context_click(element).perform()  # Right-click action

    def assert_text_by_xpath(self, xpath, expected_text):
        element = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, xpath)))
        actual_text = element.text.strip()  # Get and clean the text
        assert actual_text == expected_text, f"Assertion Failed: Expected '{expected_text}', but got '{actual_text}'"

    def upload_image(self, xpath, file_path):
        try:
            # Locate the file input element
            click = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, xpath)))

            # Upload the image file
            click.send_keys(file_path)

            print(f"Successfully uploaded: {file_path}")
        except Exception as e:
            print(f"Error uploading file: {e}")

