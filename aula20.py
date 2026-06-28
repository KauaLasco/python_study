#Exercício.
#Identificar qual número das duas variaveis é maior.

primeiro_numero = int(input("Insira o primeiro número: "))
segundo_numero = int(input("Insira o segundo número: "))

if primeiro_numero > segundo_numero:
    print(f"O primeiro número inserido ({primeiro_numero}) é maior que o segundo número ({segundo_numero})!")
elif segundo_numero > primeiro_numero:
    print(f"O segundo número inserido ({segundo_numero}) é maior que o primeiro número ({primeiro_numero})!")
else:
    print(f"O primeiro número ({primeiro_numero}) e o segundo ({segundo_numero}) são iguais!")