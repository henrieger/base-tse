from os import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

import time
import sys

state = sys.argv[1]
year = sys.argv[2]

driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.get("https://sig.tse.jus.br/ords/dwtse/f?p=2001:104:::NO:::")

# wait = WebDriverWait(driver, 10)

driver.find_element(by=By.ID, value='P0_SLS_ANO_ELEFP').send_keys(year)
time.sleep(0.5)

driver.find_element(by=By.ID, value='P0_SLS_MES_ELEFP').send_keys("Maio")
time.sleep(0.5)

driver.find_element(by=By.ID, value='P0_SLS_ABRANGENCIA_ELEFP').send_keys("Município")
time.sleep(0.5)

driver.find_element(by=By.ID, value='P0_SLS_UF_MUN_ELEFP').send_keys(state)
time.sleep(0.5)

driver.find_elements(by=By.LINK_TEXT, value='PESQUISAR')[0].click()
time.sleep(0.5)

driver.find_elements(by=By.LINK_TEXT, value='Exportar dados')[0].click()
time.sleep(2)

driver.close()