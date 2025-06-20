from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_Page:
    def __init__(self,driver):
        self.driver = driver
        self.username_field = (By.NAME , 'email' )
        self.password_field = (By.NAME, 'password')
        self.login_button = (By.XPATH, '//button[@type = "submit"]')

    def set_username(self,username):
        WebDriverWait(self.driver, timeout = 10 ).until(
            EC.visibility_of_element_located(self.username_field)
        ).send_keys(username)


    def set_password(self, password):
        WebDriverWait(self.driver, timeout = 10).until(
            EC.visibility_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(self.login_button)
        ).click()


