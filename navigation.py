from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Firefox()
driver.maximize_window()
# Open chess.com
driver.get("https://www.chess.com")

# Verify title

if (my_link:= driver.find_element(By.LINK_TEXT, "Play"),
my_link.click()):
  print("visited the play site succesfully")
  time.sleep(1)
  driver.back()
else:
    print("Try again!!")   
if(my_link:= driver.find_element(By.LINK_TEXT, "Watck"),
my_link.click()):
   print("visited the watch site succesfully")
   time.sleep(1)
   driver.back()
else:
   print("Try again!!")     
if(my_link:= driver.find_element(By.LINK_TEXT, "Learn"),
my_link.click()):
  print("visited the learn site succesfully") 
  time.sleep(1)
  driver.back()
else:
    print("Try again!!") 
if(my_link:= driver.find_element(By.LINK_TEXT, "News"),
my_link.click()):
    print("visited the News site succesfully")
    time.sleep(1)
    driver.back()
else:
    print("Try again!!")     
if(my_link:= driver.find_element(By.LINK_TEXT, "Puzzles"),
my_link.click()):
    print("visited the puzzle site succesfully")   
    time.sleep(1)
    driver.back()
else:
    print("Try again!!") 
if(my_link:= driver.find_element(By.LINK_TEXT, "Social"),
my_link.click()):
    print("visited the Socials site succesfully")
    time.sleep(1)
    try:
       element=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "/friends ")))
       element.click()
    except:    
       driver.back()
else:
    print("Try again!!") 



driver.quit()
