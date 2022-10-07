from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./shopping_mall_selenium/chromedriver")

driver.get("https://smartstore.naver.com/patthedog_official/products/6103543743")
driver.implicitly_wait(10)