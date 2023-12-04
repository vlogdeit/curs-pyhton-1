from assertpy import assert_that, soft_assertions
from locator.locators import AboutLocators
from selenium.webdriver.common.by import By


class AboutPage:
    def __init__(self, driver):
        self.driver = driver

    def goToAbout(self):
        self.driver.get("https://about.emag.ro/")  
        self.driver.maximize_window() 
        
    def verifyTitle(self):
        with soft_assertions():
            assert_that(self.driver.title).contains("Bine ai venit la eMAG")

    def verifyNavigation(self):
        navList = self.driver.find_element(*AboutLocators.navList).find_elements(*AboutLocators.navItem)
        navItems = []
        for x in navList:
            navItems.append(x.text)

        with soft_assertions():
            assert_that(navItems).contains("Grupul eMAG", "eMAG Teams", "Sustenabilitate", "Media")
