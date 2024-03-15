#language: pt
#encoding: UTF8

  @Registro
Funcionalidade: Registro de Conta
  Contexto:Como um novo usuário
  Dado Eu quero poder me registrar em uma conta

@Positivo @SemSaldo
Esquema do Cenario: Realizar registro de conta sem saldo com sucesso
  Quando o usuário insere os seguintes dados de <email>, <nome>, <senha>, <confirmacao> e <com_saldo> para cadastrar conta
  Então o usuário deve ser redirecionado para a página inicial
  Exemplos:
    | email                                 | nome          | senha    | confirmacao | com_saldo |
    | sem_saldo@yopmail.com                 | Julia Batista | senha123 | senha123    | nao       |

@Positivo @ComSaldo
Esquema do Cenario: Realizar registro de conta com saldo com sucesso
  Quando o usuário insere os seguintes dados de <email>, <nome>, <senha>, <confirmacao> e <com_saldo> para cadastrar conta
  Então o usuário deve ser redirecionado para a página inicial
  Exemplos:
    | email                                 | nome          | senha    | confirmacao | com_saldo |
    | com_saldo@yopmail.com                 | Julia Batista | senha123 | senha123    | sim       |

@Negativo
Esquema do Cenario: Registro de conta com falha devido a senhas diferentes
  Quando o usuário insere os seguintes dados de <email>, <nome>, <senha>, <confirmacao> e <com_saldo> para cadastrar conta
  Então ao usuário deve ser apresentado erro de cadastro
  Exemplos:
    | email                                 | nome          | senha    | confirmacao | com_saldo |
    | zessecoiluppeu-8038@yopmail.com       | Julia Batista | senha123 | senha1234   | sim       |
