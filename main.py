from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
chrome_driver = '/home/blood/Downloads/chromedriver'
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(service=Service(chrome_driver), options=options, service_args=[
                          '--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
driver.maximize_window()
driver.get('https://orteil.dashnet.org/cookieclicker/')
# link=driver.find_element(By.CLASS_NAME,"mw-disambig")
sleep(10)
lang = driver.find_element(By.ID, "langSelect-EN")
lang.click()
search = driver.find_element(By.ID, "bigCookie")
while True:
    search.click()
# # driver.quit()
