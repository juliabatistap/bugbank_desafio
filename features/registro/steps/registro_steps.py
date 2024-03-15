from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json



@given('Eu quero poder me registrar em uma conta')
def step_registro(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.get('https://bugbank.netlify.app')
    reg_link = context.driver.find_element(By.XPATH,"/html//div[@id='__next']/div/div[2]//div[@class='card__login']/form/div[@class='login__buttons']/button[@type='button']")
    reg_link.click()

@when('o usuário insere os seguintes dados de {email}, {nome}, {senha}, {confirmacao} e {com_saldo} para cadastrar conta')
def step_entrada_dados_registro(context, email, nome, senha, confirmacao, com_saldo):
    email_field = context.driver.find_element(By.XPATH, "/html//div[@id='__next']/div/div[2]//div[@class='card__register']/form//input[@name='email']")
    nome_field = context.driver.find_element(By.XPATH, "/html//div[@id='__next']/div/div[2]//div[@class='card__register']/form//input[@name='name']")
    senha_field = context.driver.find_element(By.XPATH, "/html//div[@id='__next']/div/div[2]//div[@class='card__register']/form//input[@name='password']")
    confirmacao_de_senha_field = context.driver.find_element(By.XPATH, "/html//div[@id='__next']/div/div[2]//div[@class='card__register']/form//input[@name='passwordConfirmation']")
    criar_conta_com_saldo_checkbox = context.driver.find_element(By.XPATH, "/html//label[@id='toggleAddBalance']")

    email_field.send_keys(email)
    nome_field.send_keys(nome)
    senha_field.send_keys(senha)
    confirmacao_de_senha_field.send_keys(confirmacao)


    if com_saldo == 'sim':
        criar_conta_com_saldo_checkbox.click()

    submit_button = context.driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]//div[@class='card__register']/form/button[@type='submit']")
    submit_button.click()

    #salvar local storage
    local_storage_data = context.driver.execute_script("return JSON.stringify(localStorage);")
    local_storage_dict = json.loads(local_storage_data)
    if senha == confirmacao:
        with open('storage.json', 'r') as file:
            storage_data = json.load(file)

        # Atualiza ou adiciona novos usuários
        storage_data.update(local_storage_dict)

        with open('storage.json', 'w') as file:
            json.dump(storage_data, file, indent=4)

@then('o usuário deve ser redirecionado para a página inicial')
def step_valida_redicionamento_home(context):
    try:
        botao = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html//div[@id='__next']/div/div[3]/div//a[@href='#']"))
        )
        botao.click()
    except Exception as e:
        assert False, f"Falha ao clicar no elemento: {e}"

@then('ao usuário deve ser apresentado erro de cadastro')
def valida_erro_cadastro(context):
    page_source = context.driver.page_source
    search_text = 'As senhas não são iguais.'
    assert search_text in page_source, "Texto de erro de cadastro não encontrado."

