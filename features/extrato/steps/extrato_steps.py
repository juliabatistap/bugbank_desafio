import json
import re
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.login.steps.login_steps import realiza_login

def formatar_valor_transf(value):
    return f"-R$ {abs(value)},00" if value < 0 else f"R$ {value},00"

def coletar_transferencias(context):
    WebDriverWait(context.driver, 15).until(EC.url_contains("/bank-statement"))
    cards = context.driver.find_elements(By.ID,"__next")

    linhas = cards[0].text.strip().split("\n")

    grupos = []
    grupo = []

    for linha in linhas:
        grupo.append(linha)
        # Verificar se a linha é uma data (assumindo que todas as datas terminam com "/2024")
        if linha.endswith("/2024"):
            grupos.append(grupo)
            grupo = []
    if grupo:
        grupos.append(grupo)
    return grupos

def transferencias_registradas():
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    return storage_data

@given('Eu quero verificar meu extrato')
def step_extrato(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.get('https://bugbank.netlify.app')

@when('o usuário faz login com as credenciais de {usuario} e {senha} e acesso a página de extrato')
def step_verifica_extrato(context, usuario, senha):
    #sobe os itens do local storage
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    for key, value in storage_data.items():
        context.driver.execute_script(f"window.localStorage.setItem('{key}', JSON.stringify({value}));")

    #realiza login pra poder fazer os seguintes passos
    realiza_login(context, usuario, senha)

    #entra em extrato
    btn_extrato = context.driver.find_element(By.ID, "btn-EXTRATO")
    btn_extrato.click()

    context.usuario = usuario

    #salvar local storage
    local_storage_data = context.driver.execute_script("return JSON.stringify(localStorage);")
    local_storage_dict = json.loads(local_storage_data)
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    # Atualiza ou adiciona novos itens
    storage_data.update(local_storage_dict)
    with open('storage.json', 'w') as file:
        json.dump(storage_data, file, indent=4)


@then('o usuário deve visualizar suas transferências enviadas')
def step_valida_extrato_enviados(context):

    #coleta todas as transferencias primeiro da tela e depois do local storage pra comparação
    grupos_transferencias = coletar_transferencias(context)
    transferencias_armazenamento = transferencias_registradas()


    #verifica se todos que estão no armazenamento local foram apresentadas na tela pro cliente
    for item in transferencias_armazenamento:
        if item != context.usuario:
            continue
        conteudo = json.loads(transferencias_armazenamento[item])
        for content in conteudo:
            if isinstance(content, dict) and 'transferValue' in content:
                valor_formatado = formatar_valor_transf(content['transferValue'])
                found = any(valor_formatado in group for group in grupos_transferencias)
            if isinstance(content, dict) and 'type' in content:
                if not found and content['type'] == 'withdrawal':
                    print(f"O valor {valor_formatado} não foi encontrado em tela.")
                    erros = 1
                    break
            else:
                erros = 0
                print("Todos os valores em armazenamento local foram encontrados em tela.")



    assert erros < 1, "Erros encontrados no extrato"



@then('o usuário deve visualizar suas transferências recebidas')
def step_valida_extrato_recebidos(context):
    #coleta todas as transferencias primeiro da tela e depois do local storage pra comparação
    grupos_transferencias = coletar_transferencias(context)
    transferencias_armazenamento = transferencias_registradas()

    #verifica se todos que estão no armazenamento local foram apresentadas na tela pro cliente
    for item in transferencias_armazenamento:
        if item != context.usuario:
            continue
        conteudo = json.loads(transferencias_armazenamento[item])
        for content in conteudo:
            if isinstance(content, dict) and 'transferValue' in content:
                valor_formatado = formatar_valor_transf(content['transferValue'])
                found = any(valor_formatado in group for group in grupos_transferencias)

            if isinstance(content, dict) and 'type' in content:
                if not found and content['type'] == 'input':
                    print(f"O valor {valor_formatado} não foi encontrado em tela.")
                    erros = 1
                    break
            else:
                erros = 0
                print("Todos os valores em armazenamento local foram encontrados em tela.")

    assert erros < 1, "Erros encontrados no extrato"
