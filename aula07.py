#Variáveis são usadas para salvar algo no computador.
#PEP8: Inicie variáveis com letras minúsculas, pode usar
#números e underlines (_). SnakeCase
#O sinal de igual (=) é o operador de atribuição. Ele é utilizado
#para atribuir um valor a um nome (variável).
#Uso: nome_variavel = expressão

nome_completo = 'Kauã Lasco dos Santos'
print(nome_completo)

soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)

#Variáveis não são utilizadas para abreviar o código!
#Muito pelo contrário, variáveis são utilizadas para tornar o código mais legivel
#e para não repetir coisas em lugares que você vai usar a mesma informação!

int_um = int('1')

print(int_um, type(int_um))

#Temos que ser super descritivos no nome de uma variável. 
#Nomeando-a com o exato nome de sua função/propósito!

nome = 'Kauã'
idade = 22
maior_de_idade = idade >= 18

print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)
