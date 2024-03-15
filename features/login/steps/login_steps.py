import json
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Eu quero acessar minha conta')
def step_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://bugbank.netlify.app')

@when('o usuário insere credenciais de {usuario} e {senha}')
def realiza_login(context, usuario, senha):
    if usuario == 'null':
        usuario = ""
    if senha == 'null':
        senha = ""

    with open('storage.json', 'r') as file:
        storage_data = json.load(file)

    for key, value in storage_data.items():
        context.driver.execute_script(f"window.localStorage.setItem('{key}', JSON.stringify({value}));")

    username_field = context.driver.find_element(By.XPATH, "/html//div[@id='__next']/div//div[@class='card__login']/form//input[@name='email']")
    password_field = context.driver.find_element(By.XPATH, "/html//div[@id='__next']/div//div[@class='card__login']/form//input[@name='password']")
    submit_button = context.driver.find_element(By.XPATH, "/html//div[@id='__next']/div//div[@class='card__login']/form//button[@type='submit']")

    username_field.send_keys(usuario)
    password_field.send_keys(senha)
    submit_button.click()

@then('o usuário deve ser redirecionado para a home da conta')
def step_valida_redicionamento_home(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'btnExit'))
    )
    assert 'home' in context.driver.current_url


@then('deve ser apresentado erro de credenciais')
def step_retorno_invalido(context):
    page_source = context.driver.page_source
    search_text = 'Usuário ou senha inválido.'
    assert search_text in page_source, "Texto de erro de cadastro não encontrado."


@then('deve ser apresentado erro de campo vazio')
def step_retorno_mensagem_erro(context):
    elements = context.driver.find_elements(By.CLASS_NAME, 'input__warging')
    assert len(elements) > 0, "Elemento não encontrado"

@then('deve ser apresentado erro de caracteres inválidos')
def step_retorno_popup_erro(context):
    page_source = context.driver.page_source
    search_text = 'Usuário ou senha inválido.'
    assert search_text in page_source, "Texto de erro de cadastro não encontrado."

