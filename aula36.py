"""
Operadores de atribuição
= | += | -= | *= | /= | //= | **= | %=
"""
contador = 22

while contador:
    contador %= 2

    if contador > 0:
        print('Impar.')
    else:
        print('Par.')

    print(contador)