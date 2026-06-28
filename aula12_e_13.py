#PODEMOS UTILIZAR ELLIPSIS (...) Eles são place holders. Por exemplo, você já escreveu um código, porém
#não pensou ainda no algoritmo dele.

nome = 'Kauã'
altura = 2.07
peso = 95
imc = peso / (altura * altura)

print(f'{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc}')

#O f-string te possibilita a utilizar variáveis dentro de strings, colocando o "f" antes da string
#e quando for inserir uma variável colacar chaves antes e depois da variável.
#Podemos ver isso no "print" acima!\

#Caso você deseje alterar as casas decimais de uma variável você pode utlizar o ":.2f" depois da variável.
print(f'Minha altura é {altura:.3f}!')

#Se você quiser também separar os números com vírgula nos casos em que estamos trabalhando com valores de dinheiro
#podemos utilizar a vírgula antes ":,.2f"
dinheiro = 30000.22
print(f'Tenho {dinheiro:,} reais!')
