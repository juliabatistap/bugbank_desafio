#language: pt
#encoding: UTF8

@Login
Funcionalidade: Login
  Contexto: Como um usuário do bugbank
    Dado Eu quero acessar minha conta

@Positivo @SemSaldo
Esquema do Cenario: Realizar login em conta sem saldo
  Quando o usuário insere credenciais de <usuario> e <senha>
  Então o usuário deve ser redirecionado para a home da conta
  Exemplos:
    | usuario                      | senha    |
    | sem_saldo@yopmail.com        | senha123 |

@Positivo @ComSaldo
Esquema do Cenario: Realizar login em conta com saldo
  Quando o usuário insere credenciais de <usuario> e <senha>
  Então o usuário deve ser redirecionado para a home da conta
  Exemplos:
    | usuario                      | senha    |
    | com_saldo@yopmail.com        | senha123 |

@Negativo
Esquema do Cenario: Realizar teste de login com credenciais invalidas
  Quando o usuário insere credenciais de <usuario> e <senha>
  Então deve ser apresentado erro de credenciais
  Exemplos:
    | usuario                      | senha    |
    | com_saldo@yopmail.com        | senha124 |

@Negativo
Esquema do Cenario: Realizar teste de login com campo de senha vazio
  Quando o usuário insere credenciais de <usuario> e <senha>
  Então deve ser apresentado erro de campo vazio
  Exemplos:
    | usuario                      | senha    |
    | com_saldo@yopmail.com        | null     |

@Negativo
Esquema do Cenario: Realizar teste de login com campo de usuário vazio
  Quando o usuário insere credenciais de <usuario> e <senha>
  Então deve ser apresentado erro de campo vazio
  Exemplos:
    | usuario                      | senha    |
    | null                         | senha124 |

@Negativo
Esquema do Cenario: Realizar teste de login com caracteres inválidos na senha
  Quando o usuário insere credenciais de <usuario> e <senha>
  Então deve ser apresentado erro de caracteres inválidos
  Exemplos:
    | usuario                      | senha    |
    | com_saldo@yopmail.com        | inválido |
@Negativo
Esquema do Cenario: Realizar teste de login com caracteres inválidos no usuário
  Quando o usuário insere credenciais de <usuario> e <senha>
  Então deve ser apresentado erro de caracteres inválidos
  Exemplos:
    | usuario                      | senha    |
    | invalido@yopmail.com         | senha124 |


