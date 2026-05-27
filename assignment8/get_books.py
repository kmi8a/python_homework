## Task 3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

URL = ('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')

driver.get(URL)

sleep(2)

results = []

search_results = driver.find_elements(By.CSS_SELECTOR, '.results li')

for entry in search_results:

    try:
        title = entry.find_element(By.CLASS_NAME, 'title-content').text
    except NoSuchElementException:
        continue

    try:
        author_data = entry.find_elements(By.CLASS_NAME, 'author-link')
        author = [x.text for x in author_data]
        author = ';'.join(author)
    except NoSuchElementException:
        author = 'N/A'

    try:
        format_year = entry.find_element(By.CLASS_NAME, 'display-info-primary').text
    except NoSuchElementException:
        format_year = 'N/A'

    result = {
        'Title':title,
        'Author':author,
        'Format-Year':format_year,
    }

    results.append(result)

driver.quit()

results_df = pd.DataFrame(results)
print(results_df)

## Task 4

results_df.to_csv('get_books.csv', index=False)
results_df.to_json('get_books.json', orient='records', indent=4)