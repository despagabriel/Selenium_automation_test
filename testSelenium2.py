from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

wait = WebDriverWait(driver, 10)
driver.get("https://www.youtube.com/")

agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button")))
agree_button.click()
time.sleep(10)

search_element = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")))
search_element.send_keys("Python Selenium")
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon")))
search_button.click()
time.sleep(10)


height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    time.sleep(1.5)
    New_height = driver.execute_script("return document.documentElement.scrollHeight")
    if  New_height==height:
        break
    height=New_height

new_list = []
class_access = driver.find_elements(By.ID, "dismissible")
for detail in class_access:
    title = detail.find_element(By.ID, "video-title")
    title_1 = title.text
    if title_1 !='':
        new_list.append(title_1)


print(len(new_list))
for x,y in enumerate(new_list):
    print(x, "---->",y)

driver.close()

