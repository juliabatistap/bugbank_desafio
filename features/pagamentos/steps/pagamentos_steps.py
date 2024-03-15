import json
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.login.steps.login_steps import realiza_login

@given('Eu quero verificar pagamentos')
def step_pagamentos(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.get('https://bugbank.netlify.app')

@when('o usuário insere os seguintes dados de {usuario} e {senha} para acessar a sua conta')
def step_verifica_pagamentos(context, usuario, senha):
    #sobe os itens do local storage
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    #realiza login pra poder fazer os seguintes passos
    realiza_login(context, usuario, senha)

    btn_pagamentos = context.driver.find_element(By.ID, "btn-PAGAMENTOS")
    btn_pagamentos.click()

    #salvar local storage
    local_storage_data = context.driver.execute_script("return JSON.stringify(localStorage);")
    local_storage_dict = json.loads(local_storage_data)
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    # Atualiza ou adiciona novos itens
    storage_data.update(local_storage_dict)
    with open('storage.json', 'w') as file:
        json.dump(storage_data, file, indent=4)


@then('o usuário receber uma mensagem impedindo de entrar no menu de pagamentos')
def step_valida_mensagem(context):
    page_source = context.driver.page_source
    search_text = "Funcionalidade em desenvolvimento"
    assert search_text in page_source, "Texto de erro não encontrado."
