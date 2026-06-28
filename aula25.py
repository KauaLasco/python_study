#Interpolação básica de strings

'''
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

'''

nome = "Kauã Lasco dos Santos"
preço = 1000.95897643
variavel = "%s, o preço total foi de R$%.2f" % (nome, preço) #Quando queremos interpolar mais de uma variavel na
#string devemos utilizar os parênteses ().
print(variavel)

#Interpolando e convertendo para Hexadecimal
print("O Hexadecimal de %i é %X" % (15, 15))
#Podemos aumentar as casas exibidas também no valor convertido para exadecimal. Utilizando o 02, 03 e etc.
print("O Hexadecimal de %i é %02X" % (15, 15))
print("O Hexadecimal de %i é %03X" % (15, 15))
print("O Hexadecimal de %i é %07X" % (15, 15))