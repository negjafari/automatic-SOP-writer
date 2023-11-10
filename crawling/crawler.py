import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import clipboard


# https://app.gomoonbeam.com/headstart/clgf4vbyo0002jj08laxecbo3/details


driver = "\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Neg\\AppData\\Local\\Google\\Chrome\\User Data")
options.page_load_strategy = 'normal'
page = webdriver.Chrome(executable_path=driver,chrome_options=options)

# page 1
page.get("https://app.gomoonbeam.com/headstart/clgf3pioy0000mj08sfzcs1ll/details")

sleep(30)

page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
page.implicitly_wait(5)


title = page.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[2]/div')
title.send_keys('computer science')

input1 = page.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div')
input1.send_keys('university')

input2 = page.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[4]/div')
input2.send_keys('student')

wait = WebDriverWait(page, 10)
generate_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/button')))
generate_btn.click()

# page 2 
sleep(50)

# page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# page.implicitly_wait(8)

wait2 = WebDriverWait(page, 10)
create_points_btn = wait2.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/button')))


create_points_btn.click()

# page 3
sleep(50)

# page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# page.implicitly_wait(5)

wait3 = WebDriverWait(page, 10)
final_btn = wait3.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/button[2]')))
final_btn.click()

# page 4
sleep(70)

actions = ActionChains(page)
text = page.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div')
text.send_keys(Keys.CONTROL, 'a')
ActionChains(page).context_click(text).perform()
ActionChains(page).move_to_element(text).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# ActionChains(page).send_keys(Keys.DOWN).send_keys(Keys.RETURN).perform()

copied = clipboard.paste()

print(copied)



sleep(1000)

