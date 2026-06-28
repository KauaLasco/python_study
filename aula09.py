#O Python consegue fazer operações entre int e float sem problemas
#Sempre que você fizer uma conta com somente números inteiros o resultado será um número inteiro.
#quando for feito por números inteiros e um ou mais números flutuantes, o resultado será um número flutuante.

adicao = 10 + 10
print('Adição: ', adicao)

subtracao = 10 - 5
print('Subtração: ', subtracao)

multiplicacao = 10 * 10
print('Multiplicação: ', multiplicacao)

divisao = 10 / 2.2 #Sempre retorna um número de ponto flutuante "FLOAT"
print('Divisão: ', divisao)

divisao_inteira = 10 // 2.2 #Só retorna um número de ponto flutuante se algum número na operação for flutuante,
#caso o contrário retornará sempre um número inteiro. Não exibe as casas decimais!
print('Divisão Inteira: ', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação: ', exponenciacao)

modulo = 55 % 2 #É o resto da divisão. É o valor que sobra da divisão!
print('Módulo: ', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0) #Como podemos ver conseguimos utilizar o módulo para saber se um número é impar ou par
print(15 % 2 == 0) #e para sabermos se um número é divisivel por outro, caso sobre um "resto" na divisão,
print(16 % 2 == 0) #não é.

