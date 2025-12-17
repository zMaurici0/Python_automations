from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1 - Acessando o site

browser = webdriver.Edge()
browser.get("https://registro.br/")
time.sleep(5)

# 2 - Buscando elemento

barraPesquisa = browser.find_element(By.ID, "is-avail-field")
barraPesquisa.clear()
barraPesquisa.send_keys("botscompython.com.br")
barraPesquisa.send_keys(Keys.ENTER)
time.sleep(5)
browser.save_screenshot("Automação com Selenium/dominio.png")

# 3 - Buscando informações 

results = browser.find_elements(By.TAG_NAME, "strong")
# import pdb
# pdb.set_trace()
print(f"Domínio {results[1].text} está {results[2].text}")