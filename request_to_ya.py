import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set path to driver.exe
driver = webdriver.Chrome('C:\\Users\\fon9\\OneDrive\\Документы\\Python\\chromedriver.exe')
driver.get("https://ya.ru")

# Locate the search box and request key-word
search = driver.find_element_by_xpath('//*[@id="text"]')
testword = input("Enter the testword: ")
search.send_keys(testword)

# Proceed search by locating and activating button
startsearch = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/div[2]/button')
startsearch.click()

# Verifying search results on page
resultpage = driver.find_elements_by_css_selector('#links > div')
assert len(resultpage) > 0

# Verifying the presence of the search word in at least one query
xpath = f"//div[@id='links']//*[contains(text(), '{testword}')]"
finalresult = driver.find_elements_by_xpath(xpath)
assert len(finalresult) > 0

# Wait & exit
time.sleep(10)
driver.quit()
