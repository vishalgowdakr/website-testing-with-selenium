from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()
driver.maximize_window()
# Open chess.com
driver.get("https://www.chess.com")

# Verify title

my_link= driver.find_element(By.LINK_TEXT, "Play")
my_link.click()
time.sleep(1)
driver.back()
my_link= driver.find_element(By.LINK_TEXT, "Watch")
my_link.click()
time.sleep(1)
driver.back()
my_link= driver.find_element(By.LINK_TEXT, "Learn")
my_link.click()
time.sleep(1)
driver.back()
my_link= driver.find_element(By.LINK_TEXT, "News")
my_link.click()
time.sleep(1)
my_link= driver.find_element(By.LINK_TEXT, "Puzzles")
my_link.click()

driver.back()
my_link= driver.find_element(By.LINK_TEXT, "Social")
my_link.click()
time.sleep(1)
try:
    element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "/friends ")))
    element.click()
except:    
  driver.back()




driver.quit()
