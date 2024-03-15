#language: pt
#encoding: UTF8

  @Saldo
Funcionalidade: Saldo
  Contexto: Como usuário
  Dado Eu quero conferir meu saldo

@Positivo @ComSaldo
Esquema do Cenario: Verificar meu saldo
  Quando o usuário insere os seguintes dados de <usuario> e <senha> para acessar a conta
  Então o usuário deve visualizar o saldo atualizado
  Exemplos:
    | usuario                               | senha    |
    | com_saldo@yopmail.com                 | senha123 |

