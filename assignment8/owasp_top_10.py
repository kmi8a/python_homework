from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

URL = ('https://owasp.org/www-project-top-ten/')

driver.get(URL)

sleep(2)

current_data = driver.find_element(By.CSS_SELECTOR, value='.page-body a')
current_data.click()

sleep(2)

current_data = driver.find_elements(By.CSS_SELECTOR, value='.md-content__inner ol li a')

owasp_list = []

for item in current_data:
    title = item.text
    link = item.get_attribute('href')

    list_item = {
        'title':title,
        'link':link,
    }

    owasp_list.append(list_item)

print(owasp_list)

owasp_df = pd.DataFrame(owasp_list)

owasp_df.to_csv('owasp_top_10.csv', index=False)