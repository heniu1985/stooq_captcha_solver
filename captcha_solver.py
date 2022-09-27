import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from twocaptcha import TwoCaptcha

from api_key import API_KEY

url = "https://stooq.pl/db/h/"

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get(url)
driver.maximize_window()

driver.implicitly_wait(5)

cookie_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")
cookie_button.click()

driver.implicitly_wait(15)

download_link = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[5]/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[3]/a")
download_link.click()

driver.implicitly_wait(15)

captcha_img = driver.find_element(By.ID, "cpt_cd")

with open("captcha.png", "wb") as captcha:
    captcha.write(captcha_img.screenshot_as_png)

solver = TwoCaptcha(API_KEY)

captcha_solve = solver.normal("captcha.png")

id = solver.send(file = "captcha.png")
time.sleep(30)

code = solver.get_result(id)

captcha_text = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[5]/tbody/tr/td/div[1]/div[1]/table/tbody/tr/td/table/tbody/tr[5]/td/input")
captcha_text.send_keys(code)

captcha_button = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[5]/tbody/tr/td/div[1]/div[1]/table/tbody/tr/td/table/tbody/tr[6]/td/input")
captcha_button.click()

driver.implicitly_wait(15)

download_button = driver.find_element(By.ID, "cpt_gt")
download_button.click()

# driver.close()