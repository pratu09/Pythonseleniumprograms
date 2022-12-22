from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://demo.guru99.com/test/newtours/register.php")

drpCountry = Select(driver.find_element(By.NAME,"country"))

drpCountry.select_by_visible_text("BAHRAIN")
time.sleep(3)
drpCountry.select_by_value("ANTARCTICA")#we use this three methods for selection
time.sleep(3)
drpCountry.select_by_index(3)
# Selecting Items in a multiple select elements

driver.get("http://jsbin.com/osebed/2")

fruits = Select(driver.find_element(By.ID,"fruits"))

assert fruits.is_multiple###very imp

fruits.select_by_visible_text("Banana")
time.sleep(3)
fruits.deselect_by_visible_text("Banana")
time.sleep(3)
fruits.deselect_by_visible_text("Apple")
time.sleep(3)
fruits.select_by_index(2)
time.sleep(3)
driver.quit()

