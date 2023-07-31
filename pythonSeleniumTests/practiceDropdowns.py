from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


service_obj = Service("/Users/betsywambui/Documents/Projects/selenium-End2EndTest/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Handling Alerts
driver.find_element(By.ID, "name").send_keys("Beth")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert "Beth" in alert.text
alert.accept()

driver.close()

# autosuggestive dynamic dropdowns
# dropdown = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "autosuggest")))
# dropdown.send_keys("In")
# countries = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
#                                                                                  "li[class='ui-menu-item'] a")))
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
# assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "basIndia"
# Dropdown
# selector = driver.find_element(By.ID, "exampleFormControlSelect1")
# dropdown = Select(selector)
# dropdown.select_by_index(1)
# driver.implicitly_wait(10000)




