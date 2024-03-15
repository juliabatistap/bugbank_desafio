#language: pt
#encoding: UTF8

@Transferencia
Funcionalidade: Transferência
  Contexto: Como um usuário do bugbank
    Dado Eu quero realizar uma transferência

@Negativo @SemSaldo
Esquema do Cenario: Realizar transferencia sem saldo
  Quando o usuário faz login com as credenciais de <usuario> e <senha> e transfere um <valor> e <descricao>
  Então o usuário deve ver um aviso de "Você não tem saldo suficiente para essa transação"
  Exemplos:
    | usuario                      | senha    | valor | descricao |
    | sem_saldo@yopmail.com        | senha123 | 45    | teste     |

@Positivo @ComSaldo
Esquema do Cenario: Realizar transferencia com saldo
  Quando o usuário faz login com as credenciais de <usuario> e <senha> e transfere um <valor> e <descricao>
  Então o usuário deve ver um aviso de transferência realizada com sucesso
  Exemplos:
    | usuario                      | senha    | valor | descricao |
    | com_saldo@yopmail.com        | senha123 | 50    | teste     |

@Negativo @ComSaldo
Esquema do Cenario: Realizar transferencia acima do saldo disponivel
  Quando o usuário faz login com as credenciais de <usuario> e <senha> e transfere um <valor> e <descricao>
  Então o usuário deve ver um aviso de "Você não tem saldo suficiente para essa transação"
  Exemplos:
    | usuario                      | senha    | valor | descricao |
    | com_saldo@yopmail.com        | senha123 | 1001  | teste     |
