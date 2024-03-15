from behave import __main__ as behave_executable

def main():
    feature_paths = [
        'features/registro/registro.feature',
        'features/login/login.feature',
        'features/transferencia/transferencia.feature',
        'features/extrato/extrato.feature',
        'features/saldo/saldo.feature',
        'features/pagamentos/pagamentos.feature',
        'features/saque/saque.feature',
    ]

    for feature_path in feature_paths:
        behave_executable.main(['--no-capture', feature_path])

if __name__ == "__main__":
    main()