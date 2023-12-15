# Importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# For arrange all acknowledge, creating a class
class Twitter:
    
    # For launching to class, adding init method
    def __init__ (self, username, password, word):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.word = word
    
    # Visiting site which want
    def logIn(self):
        url = "https://twitter.com/"
        login = self.browser.get(url)
        time.sleep(5)
        Twitter.log_ID(self)
    
    # Login username
    def log_ID(self):
        log = self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span").click()
        time.sleep(3)
        input_name = self.browser.find_element(By.NAME,"text")
        input_name.send_keys(self.username)
        time.sleep(2)
        input_name.send_keys(Keys.ENTER)
        time.sleep(4)
        Twitter.log_pass(self)
    
    # Login password 
    def log_pass(self):
        input_pass = self.browser.find_element(By.NAME,"password")
        input_pass.send_keys(self.password)
        input_pass.send_keys(Keys.ENTER)
        time.sleep(10)
        Twitter.search(self)
        
    # Seeking word which want and Creating a list for words
    def search(self):
        searc = self.browser.get("https://twitter.com/explore")
        time.sleep(5)
        sear = self.browser.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-aqfbo4.r-gtdqiz.r-1gn8etr.r-1g40b8q > div:nth-child(1) > div > div > div > div > div > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1pi2tsx.r-1777fci > div.css-175oi2r.r-1awozwy.r-18u37iz.r-16y2uox.r-1wbh5a2.r-4amgru.r-itp27i > div > div > div > form > div.css-175oi2r.r-1wbh5a2 > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > input")
        sear.send_keys(self.word)
        sear.send_keys(Keys.ENTER)
        time.sleep(5)
        
        results = []
        
        list_twette = self.browser.find_elements(By.XPATH,"//div[@data-testid='cellInnerDiv']")
        time.sleep(3)
        print("count:"+ str(len(list_twette)))
        
        for i in list_twette:
            results.append(i.text)
        
        # Adjusting slidebar 
        loop_counter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loop_counter > 3:
                break
            
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            
            if last_height == new_height:
                break
            
            last_height = new_height
            loop_counter += 1
            list_twette = self.browser.find_elements(By.XPATH,"//div[@data-testid='cellInnerDiv']")
            time.sleep(3)
            print("count:"+ str(len(list_twette)))
            
            for i in list_twette:
                results.append(i.text)
            
        list_twette = self.browser.find_elements(By.XPATH,"//div[@data-testid='cellInnerDiv']")
        time.sleep(3)
        print("count:" + str(len(list_twette)))
        
        count = 1
        for i in list_twette:
            print(f"{count}-{i.text}")
            count += 1
        
        # Opening a folder and registered of data    
        with open("data_words", "w", encoding="UTF-8") as file:
            for item in results:
                file.write(f"************* \n")
                file.write(f"{count}-{item}\n")
                count += 1
        
twitter = Twitter("your username","your password","indicate a word")
twitter.logIn()