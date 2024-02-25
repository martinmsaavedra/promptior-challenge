from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import json

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def scroll_infinito(url, espera=5, scrolls=5):
    driver.get(url)
    time.sleep(espera)
    for _ in range(scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(espera)

def extraer_datos_servicios():
    scroll_infinito("https://promptior.ai/#services", espera=2, scrolls=5)
    servicios = driver.find_elements(By.CLASS_NAME, 'service-text')
    servicios_list = [servicio.text for servicio in servicios]
    with open('chat-flask/data/services_data.json', 'w', encoding='utf-8') as f:
        json.dump(servicios_list, f, ensure_ascii=False, indent=4)
    
    # for servicio in servicios:
    #     print(f"Servicio: {servicio.text}")


def extraer_datos_sobre_nosotros():
    scroll_infinito("https://promptior.ai/about", espera=2, scrolls=5)
    texto_sobre_nosotros = driver.find_elements(By.CLASS_NAME, 'about-text')
    sobre_nosotros_list = [texto.text for texto in texto_sobre_nosotros] 
    with open('chat-flask/data/about_data.json', 'w', encoding='utf-8') as f:
        json.dump(sobre_nosotros_list, f, ensure_ascii=False, indent=4)
        
    # for texto in texto_sobre_nosotros:
    #     print(f"Sobre Nosotros: {texto.text}\n")

if __name__ == '__main__':
    extraer_datos_servicios()
    extraer_datos_sobre_nosotros()
    driver.quit()


