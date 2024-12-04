nome = input('digite seu nome')
altura = float(input('digite sua altura'))
peso = int(input('digite seu peso'))
imc = int(peso/altura**2)

print('{}, seu imc é {}.'.format(nome, imc))