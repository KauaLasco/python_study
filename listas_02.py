'''Criando listas

Listas em Python podem armazenar de maneira sequêncial qualquer tipo de objeto.
Podemos criar listas utilizando o construtor "list", a função "range" ou colocando
valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis,
portanto podemos alterar seus valores após a criação

'''

frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

print() #QUEBRA DE LINHA.

#Todas as variáveis acima são consideradas listas.

'''Acesso direto

A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de
determinada sequência a partir do zero.

'''

#Exemplo
frutas = ["banana", "morango", "kiwi", "jabuticaba"]
print(frutas[1])
print(frutas[2])
print(frutas[0])
print(frutas[3])

#É possível também escolher itens das listas a partir do último objeto, como no exemplo abaixo.
print(frutas[-1])
print(frutas[-3])

print() #QUEBRA DE LINHA.

'''Listas aninhadas

Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas.
Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

'''

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

#É assim que acessamos listas dentro de outras lisas, o primiro colchete indica os objetos da lista pricipal e
#os demais as listas seguintes que foram selecionadas.
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

print() #QUEBRA DE LINHA.

'''Fatiamento

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso
basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o
cursor deve "pular" no acesso.

'''

lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])
print(lista[::3])
print(lista[::-2])

print() #QUEBRA DE LINHA.

'''Iterar Listas

A forma mais comum de percorrer os dados de uma lista é utilizando o comando "for".

'''

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

print() #QUEBRA DE LINHA.

'''Função enumerante

Às vezes é necessário saber qual o índice do objeto dentro do laço "for". Para isso podemos usar a 
função "enumerate".

'''

#Quando utilizamos o "enumerate" o primeiro valor do "for" é o contador, o segundo o objeto que vai percorrer
#a lista e devemos pasar a lista dentro do enumerate.

for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")

print() #QUEBRA DE LINHA.

'''Compreensão de listas

A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos
valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos 
de uma lista existente.

'''

#Adicionando valores em uma nova lista, utilizando o "append"
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

print() #QUEBRA DE LINHA.

#É possível realizar isso utilizando os comprehension também, que é uma forma mais otimizada de escrever tudo
#isso que escrevemos acima.

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

#A primeira parte de uma lista comprehension é o retorno, é o retorno dessa lista que eu vou gerar, a segunda parte
#apartir do "for" é a iteração e a parte do "if" é opicional. Somente as duas primeiras são obrigatórias.

print() #QUEBRA DE LINHA.

#Outros exemplos:

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

print() #QUEBRA DE LINHA.

#Comprehension
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]

print(quadrado)