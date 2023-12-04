from selenium.webdriver.common.by import By

class HomeLocators:
    logo = (By.CSS_SELECTOR, ".navbar-brand > img")

class AboutLocators:
    navList = (By.XPATH, "//*[@id='site-header']/div[1]/div/div[2]/ul")
    navItem = (By.TAG_NAME, "li")

