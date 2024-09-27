"""
Automation using Python Selenium & WebDriver Manager - GOOGLE CHROME Browser
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class david:

    def __init__(self, url):
        self.url = url
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(service=Service(r'D:\Guvi - Automation testing\Python folder\chromedriver.exe'))

    # Boot the homepage
    def homepage(self):
        # Maximize the browser window
        self.driver.maximize_window()
        # Boot the URL on the browser
        self.driver.get(self.url)

    # Display cookies
    def display_cookies(self, message):
        cookies = self.driver.get_cookies()
        print(f"{message}:")
        for cookie in cookies:
            print(cookie)
        print("\n")

    # Login to the application
    def login(self):
        # Wait for the page to load
        time.sleep(3)

        # Log in with credentials
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        # Wait for the dashboard to load
        time.sleep(3)

    # Logout from the application
    def logout(self):
        # Click the menu button (hamburger icon)
        menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()

        # Click the logout button
        logout_button = self.driver.find_element(By.ID, "logout_sidebar_link")
        logout_button.click()

        # Wait for the page to load
        time.sleep(3)

    # Shutdown method to close the web-browser after automation
    def shutdown(self):
        self.driver.close()


if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    david = david(url)
    david.homepage()
    
    # Display cookies before login
    david.display_cookies("Cookies before login")

    # Perform login
    david.login()

    # Display cookies after login
    david.display_cookies("Cookies after login")

    # Perform logout
    david.logout()

    # Display cookies after logout
    david.display_cookies("Cookies after logout")

    david.shutdown()
