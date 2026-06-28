"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0   

while contador < 22:
    contador += 1

    if contador == 5:
        print('Não quero mostrar o 5. xD hahaha')
        continue

    if contador >= 8 and contador <=13:
        continue #Ignora todo o código abaixo enquanto a condição for atendida e volta ao início do loop.

    print(contador)

    if contador == 14:
        break #Quebra toda a sequência e principalmente a execução do loop (while/for).