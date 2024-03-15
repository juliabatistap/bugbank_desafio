#language: pt
#encoding: UTF8

  @Saldo
Funcionalidade: Saque
  Contexto: Como usuário
  Dado Eu quero realizar um saque

@Negativo @ComSaldo
Esquema do Cenario: Solicitar Saque
  Quando o usuário insere os dados de <usuario> e <senha> para acessar a conta
  Então o usuário receber uma mensagem impedindo de entrar no menu de saque
  Exemplos:
    | usuario                               | senha    |
    | com_saldo@yopmail.com                 | senha123 |

