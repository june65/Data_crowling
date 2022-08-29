from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("크롤링 할 주소 입력")
driver.implicitly_wait(3)