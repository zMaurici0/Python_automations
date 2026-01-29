from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv
import os

load_dotenv(override=True)
usuario = os.environ.get('login_kroton')
senha = os.environ.get('senha')

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    pag = navegador.new_page()
    pag.goto("https://login.kroton.com.br/")
    print(pag.title())
    pag.get_by_test_id("login-input").fill(usuario)
    pag.get_by_test_id("submit-button").click()
    pag.get_by_test_id("login-pass").fill(senha)
    pag.get_by_test_id("submit-button").click()
    time.sleep(5)
    navegador.close()