from behave import fixture
from selenium import webdriver
import logging

@fixture
def before_all(context):
    """
    Configura o navegador antes de todos os cenários.
    """
    logging.debug("O arquivo environment.py está sendo executado.")
    context.driver = webdriver.Chrome()

@fixture
def after_all(context):
    """
    Limpa após todos os cenários.
    """
    logging.debug("O arquivo environment.py está sendo executado.")
    context.driver.quit()


@fixture
def before_scenario(context, scenario):
    """
    Configura o navegador antes de cada cenário.
    """
    # Você pode redefinir o estado do navegador aqui, se necessário

@fixture
def after_scenario(context, scenario):
    """
    Limpa após cada cenário.
    """
    # Você pode limpar o estado do navegador aqui, se necessário
