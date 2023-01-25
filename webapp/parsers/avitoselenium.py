import requests
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions



def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f=ASgBAQICAUSSA8YQAUDKCKSKWZqsAZisAZasAZSsAYhZhlmEWYJZgFk")
    apartments = driver.find_elements(By.CLASS_NAME, "items-items-kAJAg")

    wait = WebDriverWait(driver, 5)
    link = apartments[0].find_element(By.CLASS_NAME, "iva-item-root-_lk9K")
    print(link.get_attribute('href'))
    link = wait.until(expected_conditions.element_to_be_clickable(link))
    print(link.get_attribute('href'))
    link.click()

    driver.switch_to.window(driver.window_handles[-1])
    #image = driver.find_element(By.CLASS_NAME, "css-1qr5gpo")

    #НАЙТИ ЭЛЕМЕНТ ИЗОБРАЖЕНИЯ
    image = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "css-1qr5gpo")))

    # ПОЛУЧИТЬ URL из документа
    image_url = image.get_attribute('src')

    img_data = requests.get(image_url).content
    filename = uuid.uuid4().hex
    with open(f'photos/{filename}.jpg', 'wb') as handler:
        handler.write(img_data)

    #image_wrapper = apartment.find_element(By.CLASS_NAME, "css-1qr5gpo")
    #image = image_wrapper.find_element(By.TAG_NAME, 'img')

    driver.close()

if __name__ == '__main__':
    main()


