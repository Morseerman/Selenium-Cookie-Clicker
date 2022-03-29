from lib2to3.pgen2 import driver
from re import search
import time
from pip import main
from selenium import webdriver
import unittest
import Pages

class Testing (unittest.TestCase):

    def setUp(self):

        PATH  = "D:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        print("title: " + self.driver.title)

    def test_cookie_counter(self):
        mainPage = Pages.MainPage(self.driver)  
        time.sleep(3)
        mainPage.click_cookie()
        time.sleep(1)       
        assert True if mainPage.get_num_of_cookies().split(' ')[0] == "1" else False

       
    def test_page_title(self):
        mainPage = Pages.MainPage(self.driver) 
        assert mainPage.does_title_match()
        

    def test_upgrading_cookie(self):
        mainPage = Pages.MainPage(self.driver) 
        assert mainPage.drag_upgrade_button()

    def tearDown(self):
        self.driver.close()

unittest.main()