from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://stooq.pl/db/h/"

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(url)
driver.maximize_window()

cookie_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")
cookie_button.click()

driver.implicitly_wait(5)

download_link = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[5]/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[3]/a")
download_link.click()

driver.implicitly_wait(10)

captcha_img = driver.find_element(By.ID, "cpt_cd")

with open("captcha.png", "wb") as captcha:
    captcha.write(captcha_img.screenshot_as_png)

driver.close()