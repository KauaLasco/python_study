'''O que são?

São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode
ser conhecido previamente ou determinado através de uma expressão lógica.

Comando for: 

O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de
vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.
'''

#for
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for i in texto:
    if i.upper() in VOGAIS:
        print(i, end="")

print()

#Uma string em Python é um objeto iterável
#O for tem o else também. E ele sempre é executado no final do laço.
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for i in texto:
    if i.upper() in VOGAIS:
        print(i, end="")
else:
    print()

'''Função range() no for

O range() é uma função build-in do Python, ela é usada para produzir uma sequência de números inteiros a partir
de um início (inclusivo) para um fim (exclusivo). Se usarmo range(i, j) será produzido:

i, i+1, i+2, i+3, ..., j-1.

Ela recebe 3 argumentos: 1 - start(opcional), 2 - stop (obrigatório) e 3 - step (opcional).
'''

#range exemplo.
for numero in range(0,11):
    print(numero, end=" ")
else:
    print()
#Exibindo a tabuada do 5.
for numero in range(0,51, 5):
    print(numero, end=" ")

print()

'''Comando while
Quando eu quero executar até que algo aconteça?

O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos
o número exato de vezes que nosso bloco de código deve ser executado.

'''

#Exemplo while:
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

#O while é muito parecido com o if, a diferença é que o if testa e executa uma vez, já o while vai executar
#toda vez que certa condição for atendida.

#O while é igual ao for pois também tem a mesma funcionalidade do else.

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário até agora!")

#O while possui uma palavra reservada o "break", ele para a execução do programa
#Podemos utilizar o loop infinito utilizando o while. Usando o "True" ou condições que sejam verdadeiras.
#Como por exemplo 1 == 1, 2 > 1 e por assim vai. Enquando a lógica for verdadeira o loop continua sendo executado.

while True:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)

#Lembrando que é possível utilizar o break no for também.

for numero in range(101):
    if numero == 22:
        break

    print(numero, end=" ")

print()

#Temo também o "continue" que ele pula certo valor ou coisa desejada.

for numero in range(101):
    if numero == 22:
        continue

    print(numero, end=" ")

print()

#Um exemplo, exibir apenas os números impares.

for numero in range(101):
    if numero % 2 == 0:
        continue

    print(numero, end=" ")
