from nturl2path import url2pathname
from selenium import webdriver

url = "https://stooq.pl/db/h/"

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(url)
driver.implicitly_wait(5)

driver.close()