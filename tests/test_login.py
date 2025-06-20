import pytest


from pages.login_page import Login_Page
from utils.config import CONFIG

@pytest.mark.parametrize('username, password', [(CONFIG['login_email'], CONFIG['login_password'])])
def test_login(browser, username, password):
    browser.get(CONFIG['base_url'])
    login_page = Login_Page(browser)
    login_page.set_username(username)
    login_page.set_password(password)
    login_page.click_login()
    print(browser.title)
    assert 'Piiink Admin Panel' == browser.title