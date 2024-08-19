from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

# Abre a página de busca de CEP dos Correios
driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

def busca_cep(valor_busca):
    # Localiza o campo de busca e insere o valor
    campo_busca = driver.find_element(By.NAME, "endereco")
    campo_busca.clear()
    campo_busca.send_keys(valor_busca)
    
    # Seleciona o tipo de busca "Por Localidade/Logradouro"
    campo_tipo = driver.find_element(By.NAME, "tipoCEP")
    campo_tipo.send_keys("Localidade/Logradouro")
    
    # Clica no botão de busca
    botao_busca = driver.find_element(By.ID, "btn_pesquisar")
    botao_busca.click()
    
    # Aguarda a página carregar os resultados
    time.sleep(2)

    # Extrai os resultados da busca
    resultados = driver.find_elements(By.XPATH, "//td")
    for resultado in resultados:
        print(resultado.text)

# Cenário 1: Buscar o CEP "69005-040"
print("Cenário 1: Buscando o CEP 69005-040")
busca_cep("69005-040")

# Cenário 2: Buscar por "Lojas Bemol"
print("\nCenário 2: Buscando por Lojas Bemol")
busca_cep("Lojas Bemol")

# Fecha o navegador
driver.quit()