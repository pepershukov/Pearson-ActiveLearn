import seleniumbase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import urllib
import os
from dotenv import dotenv_values
config = dotenv_values(".env")

with seleniumbase.SB() as driver:
    driver.get("https://pearsonactivelearn.com/app/login?redirect=/app/library")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username")))
    
    if "USERNAME" in config:
        driver.find_element(By.ID, "username").send_keys(config['USERNAME'])
        driver.find_element(By.ID, 'password').send_keys(config['PASSWORD'])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'submitBttn'))).click()
        input("Load a book, then press Enter")
    else:
        input("- Login with your credentials\n- Load the ebook, then press Enter")

    driver.switch_to_newest_tab()
    driver.switch_to_frame("#ebookPlayer")
    driver.switch_to_frame("#iframe0")
    images_path = driver.get_attribute('img', "src")

    cookies = driver.get_cookies()

requests_cookies = {i['name']: i['value'] for i in cookies}
image_prefix = os.path.split(images_path)[1].split('-')[0]

save_dir = config["SAVE_DIR"] if "SAVE_DIR" in config else input("Enter absolute path where to store pictures: ")
os.makedirs(save_dir, exist_ok=True)

counter = 1
while True:
    try:
        filename = f"{image_prefix}-{counter:03d}.jpg"
        image_url = urllib.parse.urljoin(images_path, filename)
        response = requests.get(image_url, cookies=requests_cookies, stream=True)

        if response.status_code == 200:
            save_path = os.path.join(save_dir, filename)
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=65536):
                    file.write(chunk)
            print(f"Downloaded picture #{counter}")
            counter += 1
        elif response.status_code == 404:
            print("Received HTTP 404")
            break
        else:
            print(f"Unexpected response: {response.status_code}")
            break
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        break