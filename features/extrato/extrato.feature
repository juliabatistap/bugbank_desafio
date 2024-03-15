#language: pt
#encoding: UTF8

@Extrato
Funcionalidade: Extrato
  Contexto: Como um usuário do bugbank
    Dado Eu quero verificar meu extrato

@Positivo @ComSaldo
Esquema do Cenario: Verificar extrato (enviados)
  Quando o usuário faz login com as credenciais de <usuario> e <senha> e acesso a página de extrato
  Então o usuário deve visualizar suas transferências enviadas
  Exemplos:
    | usuario                      | senha    |
    | com_saldo@yopmail.com        | senha123 |


@Positivo @SemSaldo
Esquema do Cenario: Verificar extrato (recebidos)
  Quando o usuário faz login com as credenciais de <usuario> e <senha> e acesso a página de extrato
  Então o usuário deve visualizar suas transferências recebidas
  Exemplos:
    | usuario                      | senha    |
    | sem_saldo@yopmail.com        | senha123 |