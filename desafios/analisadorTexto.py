nome = str(input('Digite seu nome completo: ')).strip()

maiuscula = nome.upper()
minuscula = nome.lower()
tamanhoSemEspaco = nome.__len__()-nome.count(' ')
dividirNome = nome.split()
tamanhoPrimeiroNome = dividirNome[0].__len__()

print('Nome maiusculo: {}'.format(maiuscula))
print('Nome minusculo: {}'.format(minuscula))
print('Tamanho primeiro nome: {}'.format(tamanhoPrimeiroNome))
print('Tamanho Nome Completo sem espaco: {}'.format(tamanhoSemEspaco))