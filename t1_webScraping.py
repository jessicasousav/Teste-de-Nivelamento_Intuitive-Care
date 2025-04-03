from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from time import sleep

import wget

from zipfile import ZipFile

# Acessando o site
service = Service(executable_path="chromedriver.exe")
navegador = webdriver.Chrome(service=service)
navegador.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')

# Caso tenha página de cookies (aceita os cookies automaticamente):
if navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]'):
    navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]').click()

# Salvando o url da página original
original_window = navegador.current_window_handle


# ANEXO 1
# clicando no link do pdf 
navegador.find_element(By.XPATH, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]').click()

# trocando foco do selenium para nova aba
for window_handle in navegador.window_handles:
    if window_handle != original_window:
        navegador.switch_to.window(window_handle)
        break

# download do Anexo 1
print("\nFazendo download do Anexo 1 no seu computador...")

linkAnexo1 = navegador.current_url
wget.download(linkAnexo1, "Anexo1.pdf")

print("\nDownload do Anexo 1 feito com sucesso! Fechando guia...")
sleep(2)

# fechando guia Anexo 1 após download
navegador.close()
navegador.switch_to.window(original_window)
sleep(1)


# ANEXO 2
navegador.find_element(By.XPATH, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a').click()

for window_handle in navegador.window_handles:
    if window_handle != original_window:
        navegador.switch_to.window(window_handle)
        break

# download do Anexo 2
print("\nFazendo download do Anexo 2 no seu computador...")

linkAnexo2 = navegador.current_url
wget.download(linkAnexo2, "Anexo2.pdf")

print("\nDownload do Anexo 2 feito com sucesso! Fechando guia...")
sleep(2)

# fechando guia Anexo 2 após download
navegador.close()
navegador.switch_to.window
sleep(2)

# Fechando janela aberta
navegador.quit()


# COMPACTANDO ARQUIVOS
print("\nCompactando seus arquivos...")

with ZipFile("Anexos.zip", "w") as zip:
    zip.write("Anexo1.pdf")
    zip.write("Anexo2.pdf")
sleep(1)
print("Arquivos compactados com sucesso!\n")