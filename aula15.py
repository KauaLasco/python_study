#O input serve para que o usuário insira informações
#para prosseguir com a execução do código!

input('Qual o seu nome? ')
#Como podemos ver é possível inserir strings (str) dentro
#de inputs.

#É possível também armazenar/coletar dados utilizando o
#input. Simplesmente utilizando uma variável.

nome = input('Qual o seu nome? ')
print(f'O seu nome é: {nome}')

#Podemos também fazer com que exiba a variável e o valor
#dela dentro da string.
print(f'O seu nome é: {nome=}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(f'A soma dos números {numero_1} e {numero_2} resulta em: {numero_1 + numero_2}')
#Como podemos ver utilizando a função print desta forma,
#resultou na concatenação dos valores e não na soma.
#Pelo simples fato de que os números digitados são (str)!

#É possível transformar em int em uma linha só porém
#isso pode ocasionar transtorno e sómente principiantes fazem isso.
numero_3 = int(input('Digite um número: '))
numero_4 = int(input('Digite outro número: '))

print(f'A soma dos números {numero_3} e {numero_4} resulta em: {numero_3 + numero_4}')

#Para fazer uma checagem no valor inserido no input da
#variável, podemos criar outra variável para transformar
#o str em int
numero_5 = int(input('Digite um número: '))
numero_6 = int(input('Digite outro número: '))

int_numero_5 = int(numero_5)
int_numero_6 = int(numero_6)

print(f'A soma dos números {numero_5} e {numero_6} resulta em: {int_numero_5 + int_numero_6}')