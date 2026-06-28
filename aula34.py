'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
condicao = True

# while condicao:
#     print(1)
#     print(2)
#     print(3)

while condicao:
    nome = input("Digite seu nome: ")
    print(f"Seu nome é {nome}.")
    
    if nome == 'sair':
        break #O "break" procura o laço de repetição mais próximo e o encerra.

print("While encerrado.")