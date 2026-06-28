'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''

while False: #Enquanto a condição for verdadeira o código entra no 'while'. Quando for falsa
    ...      #ele sai e para a execução do while. Podemos para-lo tornando a condição em
             # 'FALSE'ao invés de utilizar o 'break'
print('Acabou.')

contador = 0

while contador < 22:
    contador += 1
    print(contador)