#Formatação básica de strings

"""
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Conversion flags - !r !s !a

"""

variavel = "ABC"
print(f"{variavel: >10}") #Preenche 10 espaços para a esquerda.
print(f"{variavel: <10}") #Preenche 10 espaços para a direita.
print(f"{variavel:-<10}") #Preenche 10 espaços para a direita.
print(f"{variavel:->10}") #Preenche 10 espaços para a esquerda.
print(f"{variavel:-^11}") #Preenche 10 espaços para o centro.

#É possível editar números também.
print(f"{1000.4198724129084:.2f}") #Exibe apenas duas casas decimais.
print(f"{1000.4198724129084:,.1f}") #Separa os números pela vírgula.
print(f"{1000.4198724129084:+.1f}") #Podemos indicar para o Python também para mostrar o sinal do número.
print(f"{-1000.4198724129084:+.1f}") #Podemos indicar para o Python também para mostrar o sinal do número.
print(f"{-1000.4198724129084:-.1f}") #Podemos indicar para o Python também para mostrar o sinal do número.
