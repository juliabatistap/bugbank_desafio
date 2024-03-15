import json
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.login.steps.login_steps import realiza_login


def filtrar_contas(data, span_element):
    contas_filtradas = []
    for key, value in data.items():
        if "@" in key and "accountNumber" in value:
            account_data = json.loads(value)
            if account_data['accountNumber'] != span_element:
                contas_filtradas.append(account_data['accountNumber'])
    return contas_filtradas

@given('Eu quero realizar uma transferência')
def step_transferencia(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(15)
    context.driver.get('https://bugbank.netlify.app')

@when('o usuário faz login com as credenciais de {usuario} e {senha} e transfere um {valor} e {descricao}')
def step_realizar_transferencia(context, usuario, senha, valor, descricao):
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    for key, value in storage_data.items():
        context.driver.execute_script(f"window.localStorage.setItem('{key}', JSON.stringify({value}));")

    realiza_login(context, usuario, senha)

    span_element = context.driver.find_element(By.ID, "textAccountNumber")
    span_text = (span_element.text).split("Conta digital: ")[1]

    btn_transf = context.driver.find_element(By.ID, "btn-TRANSFERÊNCIA")
    btn_transf.click()

    contas_filtradas = filtrar_contas(storage_data, span_text)
    numero_field = context.driver.find_element(By.NAME, "accountNumber")
    digito_field = context.driver.find_element(By.NAME, "digit")
    valor_field = context.driver.find_element(By.NAME, "transferValue")
    descricao_field = context.driver.find_element(By.NAME, "description")
    btn_submit = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Transferir agora')]")

    conta = contas_filtradas[0].split("-")[0]
    digito = contas_filtradas[0].split("-")[1]

    numero_field.send_keys(conta)
    digito_field.send_keys(digito)
    valor_field.send_keys(valor)
    descricao_field.send_keys(descricao)
    btn_submit.click()

    #salvar local storage
    local_storage_data = context.driver.execute_script("return JSON.stringify(localStorage);")
    local_storage_dict = json.loads(local_storage_data)
    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    # Atualiza ou adiciona novos usuários
    storage_data.update(local_storage_dict)

    with open('storage.json', 'w') as file:
        json.dump(storage_data, file, indent=4)




@then('o usuário deve ver um aviso de transferência realizada com sucesso')
def step_retorno_sucesso(context):
    page_source = context.driver.page_source
    search_text = 'Transferencia realizada com sucesso'
    assert search_text in page_source, "Texto de erro de cadastro não encontrado."

@then('o usuário deve ver um aviso de "Você não tem saldo suficiente para essa transação"')
def step_retorno_saldo_insuficiente(context):
    page_source = context.driver.page_source
    search_text = 'Você não tem saldo suficiente para essa transação'
    assert search_text in page_source, "Texto de erro de cadastro não encontrado."
