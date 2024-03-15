import json
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.login.steps.login_steps import realiza_login
from features.extrato.steps.extrato_steps import transferencias_registradas


@given('Eu quero conferir meu saldo')
def step_saldo(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.get('https://bugbank.netlify.app')

@when('o usuário insere os seguintes dados de {usuario} e {senha} para acessar a conta')
def step_verifica_saldo(context, usuario, senha):
    #sobe os itens do local storage
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    #realiza login pra poder fazer os seguintes passos
    realiza_login(context, usuario, senha)


    key_transaction = 'transaction:' + usuario
    transferencias_armazenamento = transferencias_registradas()
    transferencias = json.loads(transferencias_armazenamento[key_transaction])
    context.saldo_inicial = 0

    # Procurar pela descrição específica e retornar o valor de 'transferValue'
    for transacao in transferencias:
        if transacao['description'] == "Saldo adicionado ao abrir conta":
            context.saldo_inicial = transacao['transferValue']

    valores_transferencias = [item['transferValue'] for item in transferencias if item['type'] in ['input', 'withdrawal']]
    context.valores_totais_transferencias = sum(valores_transferencias)

    context.saldo_disponível = context.driver.find_element(By.ID, "textBalance")

    #salvar local storage
    local_storage_data = context.driver.execute_script("return JSON.stringify(localStorage);")
    local_storage_dict = json.loads(local_storage_data)
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    # Atualiza ou adiciona novos itens
    storage_data.update(local_storage_dict)
    with open('storage.json', 'w') as file:
        json.dump(storage_data, file, indent=4)


@then('o usuário deve visualizar o saldo atualizado')
def step_valida_saldo(context):
    valores_totais_transferencias = context.valores_totais_transferencias
    saldo_inicial = context.saldo_inicial
    saldo_disponível = context.saldo_disponível

    saldo_disponivel = saldo_disponível.text.strip().split("Saldo em conta R$ ")
    saldo_disponivel = saldo_disponivel[1].split(",00")[0]

    assert int(saldo_disponivel) == saldo_inicial + valores_totais_transferencias, "Saldo não corresponde as entradas e saídas"
