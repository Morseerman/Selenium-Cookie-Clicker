import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys



#Setup
PATH  = "D:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s)

driver.get("https://orteil.dashnet.org/cookieclicker/")

bigCookie = driver.find_element_by_id('bigCookie')
cookies = driver.find_element_by_id('cookies')
products = [driver.find_element_by_id('product' + str(i)) for i in range(16, -1, -1)]
productPrices = [driver.find_element_by_id('productPrice' + str(i)) for i in range(16, -1, -1)]

#Basic functions

def removeCommas(word):
    word = word.replace(",","")
    return word

def wordToNumber(word):
    if word.find(" ") != -1:
        splitWord = word.split(" ")
        newWord = splitWord[0].replace(".", "")

        if splitWord[1] == "million":
            return int(newWord) * 100000
        if splitWord[1] == "billion":
            return int(newWord) * 100000000
        if splitWord[1] == "trillion":
            return int(newWord) * 100000000000
    return word

def clickCookie():
    bigCookie.click()   

def buyUpgrades(num_of_cookies):
    for j in range(len(products)):         
        if (productPrices[j].text) != '': 
            print(removeCommas(productPrices[j].text))               
            if num_of_cookies > int(wordToNumber(removeCommas(productPrices[j].text))): products[j].click() 
    

#start 
print("\n\n-----------Trest----------\n\n")
time.sleep(10)


#for i in range(10000):
while(True):
    num_of_cookies = int(removeCommas(cookies.text.split(' ')[0]))           
 
    clickCookie()   
    
    #buyUpgrades(num_of_cookies)    
    
    if num_of_cookies > int(removeCommas(productPrices[len(productPrices) - 1].text)) - 6: buyUpgrades(num_of_cookies)  
   

#time.sleep(10)
#driver.quit()


