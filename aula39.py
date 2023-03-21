nome = 'Felipe Manoel'

# tamanho_nome = len(nome)

# print(nome)
# print(tamanho_nome)

# #print(nome[7])

contador = 0
novo_nome = ''

while contador < len(nome): 
    print(nome[contador])

    numero_letra = f'*{nome[contador]}'
    novo_nome += numero_letra
    contador += 1
novo_nome += '*'
print(novo_nome)