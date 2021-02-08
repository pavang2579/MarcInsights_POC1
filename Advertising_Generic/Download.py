import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


df = pd.read_csv("countrywise copy.csv")
List = df["name-href"].to_list()

urls = []

for i in range(len(List)):
    url = List[i]
    urls.append(url)
print(urls)

from selenium import webdriver
download_dir = "/Users/shivaneeprajapati/Downloads/Stats"  # for linux/*nix, download_dir="/usr/Public"
options = webdriver.ChromeOptions()
profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],  # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf",
               "download.prompt_for_download": False, "plugins.always_open_pdf_externally": True}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome('/Users/shivaneeprajapati/Downloads/chromedriver',chrome_options=options)





for i in range(len(List)):
    driver.get(List[i])
    time.sleep(2)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                            '//*[@id="csv-version"]'))))

    #wait = WebDriverWait(self.driver, 10)
    #element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="csv-version"]')))
    #element.click()

    
    #driver.find_element_by_id("csv-version").click()