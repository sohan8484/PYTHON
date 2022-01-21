from time import sleep

from selenium.webdriver import Chrome

driver=Chrome("./chromedriver.exe")
driver.get("https://www.google.com/")
sleep(5)
driver.close()