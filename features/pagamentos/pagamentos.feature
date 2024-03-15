#language: pt
#encoding: UTF8

@Saldo
Funcionalidade: Pagamentos
  Contexto: Como usuário
    Dado Eu quero verificar pagamentos

  @Negativo @ComSaldo
  Esquema do Cenario: Verificar Pagamentos
    Quando o usuário insere os seguintes dados de <usuario> e <senha> para acessar a sua conta
    Então o usuário receber uma mensagem impedindo de entrar no menu de pagamentos
    Exemplos:
      | usuario                               | senha    |
      | com_saldo@yopmail.com                 | senha123 |
