from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura o driver do Firefox
driver = webdriver.Firefox()

# Abre o site do Trivago
driver.get("https://www.trivago.com.br")

# Função para automatizar o fluxo
def automatizar_fluxo_trivago():
    # Espera o campo de busca aparecer e insere a cidade Manaus
    wait = WebDriverWait(driver, 10)
    campo_busca = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))
    campo_busca.send_keys("Manaus")
    
    # Clica na primeira sugestão que aparece (normalmente a cidade correspondente)
    primeira_sugestao = wait.until(EC.element_to_be_clickable((By.XPATH, "//mark[contains(text(),'Manaus')]")))
    primeira_sugestao.click()

    # Aguarda o carregamento da página de resultados
    time.sleep(5)  # Pode ajustar esse tempo dependendo da conexão

    # Ordena por "Avaliações e Sugestões"
    filtro_ordenacao = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='sorting-filter-button']")))
    filtro_ordenacao.click()
    
    # Seleciona "Avaliações e Sugestões" na lista
    ordenar_por_avaliacoes = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Avaliações e Sugestões')]")))
    ordenar_por_avaliacoes.click()

    # Aguarda a atualização dos resultados
    time.sleep(5)

    # Verifica o primeiro hotel da lista, sua avaliação e preço
    primeiro_hotel = driver.find_element(By.XPATH, "(//div[@data-testid='item-name'])[1]").text
    avaliacao_hotel = driver.find_element(By.XPATH, "(//span[@data-testid='rating'])[1]").text
    valor_hotel = driver.find_element(By.XPATH, "(//strong[@data-testid='price'])[1]").text

    # Imprime os resultados
    print(f"Primeiro Hotel: {primeiro_hotel}")
    print(f"Avaliação: {avaliacao_hotel}")
    print(f"Valor: {valor_hotel}")

# Executa a função para automatizar o fluxo
automatizar_fluxo_trivago()

# Fecha o navegador
driver.quit()
