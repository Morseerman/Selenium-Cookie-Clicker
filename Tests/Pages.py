from locators import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q "

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()
    
    def does_title_match(self):
        return True if self.driver.title == "Cookie Clicker" else False
   
    
    def click_cookie(self):
        element = self.driver.find_element(*MainPageLocators.COOKIE)
        element.click()
    
    def get_num_of_cookies(self):
        element = self.driver.find_element(*MainPageLocators.COOKIE_COUNTER)
        return element.text
    
    #r    
    def drag_upgrade_button(self): 
        #element = self.driver.find_element(*MainPageLocators.POINTER)
        #element.drag()
        return True

    def doubleClick_go_button(self): 
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.doubleClick()

    def rightClick(self): 
        element = self.driver.find_element(*MainPageLocators.GRANDMA)
        element.rightClick()

    def click_go_button(self): 
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
    
class ClassicCookieClicker(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source