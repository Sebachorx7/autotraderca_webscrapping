from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
# import undetected_chromedriver as uc
import time
#Installed undetected_chromedriver, setuptools
#Esto es para que el navegador inicie sin necesidad de que abra una nueva ventana. Abrira la ventana y ejecutara todo el codigo, pero no la mostrara ni comprometera recursos del pc
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Activa el modo sin ventana moderno
chrome_options.add_argument("--window-size=1920,1080")  # Define un tamaño de pantalla virtual obligatorio
chrome_options.add_argument("--disable-gpu")  # Optimización recomendada para entornos headless


driver = webdriver.Chrome(options=chrome_options)
driver.delete_all_cookies()
driver.get("https://www.autotrader.ca/")

#Variables
text_make = "GMC"
text_postal_code = "L1N1Y8"

actions = ActionChains(driver)
select_make = driver.find_element(By.NAME, "make")
select = Select(select_make)
select.select_by_visible_text(text_make)
postal_code = driver.find_element(By.ID, "location")
actions.move_to_element(postal_code).click().perform()
postal_code.clear()
actions.send_keys(text_postal_code).send_keys(Keys.TAB).perform()
waiting = WebDriverWait(driver,10)
detected_location = waiting.until(EC.text_to_be_present_in_element_value((By.ID,"location"), ","))
button_search = driver.find_element(By.ID, "search-mask-search-cta")
button_search.click()


car_name = driver.find_element(By.CSS_SELECTOR, "span[class='ListItem_title_bold__iQJRq']")
car_price_clean = driver.find_element(By.XPATH, '//p[@data-testid="regular-price"]')
car_price = driver.execute_script("return arguments[0].textContent;", car_price_clean)
car_mileage = driver.find_element(By.CSS_SELECTOR, "span[class='VehicleDetailTable_item__4n35N']")
car_description = driver.find_element(By.CSS_SELECTOR, "div[class='ListItem_vehicle_description__6VHh9']")
car_location = driver.find_element(By.CSS_SELECTOR, "span[class='SellerInfo_name__nR9JH']")

#Yquiero ver todos los de esta primera pantalla sus valores marcas y modelos en la terminal, para imprimirlos en un documento, debo usar loop

print(car_name.text)
print(car_price.strip()) # .strip() limpia espacios en blanco innecesarios
print(car_mileage.text)
print(car_location.text)

# time.sleep(5)
driver.quit()
