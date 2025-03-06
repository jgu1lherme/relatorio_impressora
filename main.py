from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time
import os

PATH = "C:\\Users\\joao.guilherme.ALTERNATIVA1\\Downloads\\edgedriver_win64\\msedgedriver.exe"

options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")

# Criar um diretório temporário para evitar conflitos
user_data_dir = os.path.join(os.getcwd(), "selenium_profile")
options.add_argument(f"--user-data-dir={user_data_dir}")

service = Service(executable_path=PATH)

driver = webdriver.Edge(service=service, options=options)

driver.get("https://192.168.15.205/rui/login_manager.html")

wait = WebDriverWait(driver, 20)
campo_senha = wait.until(
    EC.visibility_of_element_located((By.ID, "passdataScreen_1030"))
)

campo_senha.send_keys("KLPF57350")

botao_ok = driver.find_element(By.ID, "submitScreen_1030")
botao_ok.click()

time.sleep(7)

opcao_utilitarios = driver.find_element(By.ID, "Top01Screen_1000")
opcao_utilitarios.click()

time.sleep(5)

opcao_impressao = driver.find_element(By.ID, "List00Screen_5000")
opcao_impressao.click()

time.sleep(5)

botao_sim = driver.find_element(By.ID, "YNBtn00Screen_5010")
botao_sim.click()

time.sleep(7)

driver.quit()
