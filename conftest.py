from selenium import webdriver
from selenium.webdriver.chrome.service import Service as s
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def browser():
    print('Setting up the browser ...')
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.maximize_window()
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Optional: run in headless mode
    # driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(10)
    yield driver
    print('Tearing down the browser ...')
    driver.quit()


