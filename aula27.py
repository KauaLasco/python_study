#Fatiamento de strings.

'''
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da string.

'''

variavel = "Olá mundo!"
print(variavel[5]) #Seleciona o índice 5.
print(variavel[0:3]) #Fatiando a string.
print(len(variavel[0:3])) #Conta os caracteres da string.
print(len(variavel)) #Conta os caracteres da string.
print((variavel[0:10:3])) #Fatia a string pulando a cada 3 caracteres.
print((variavel[::-1])) #Inverte todas as letras da string.
print((variavel[-1:-11:-1])) #Inverte todas as letras da string.

