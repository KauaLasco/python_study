#Conversão de tipos, coerção
#type convertion, typecasting, coercion
#é o ato de converter um tipo em outro
#tipos imutáveis e primitivos:
#str, int, float, bool

print(1 + 1)
print('a' + 'b')

#Acima podemos ver um plimorfismo acontecendo. Um sinal que era,
#para ser usado em uma conta soma, está sendo usado também
#para concatnar duas strings.
#Isso é algo que geralmente só é possível em linguagens dinâmicas!

#Se tentarmos concatenar uma string com um número seja float ou int,
#não será possível pois, só é possível concatenar string com string!
#print('1' + 1)

#Quando o Python retorna "TypeError" significa que é um erro de tipo,
#por exemplo: um str que é pra ser int, ou etc.

#Em linguagens de tipagem fraca ela simplesmente converte o tipo errado em outro e realiza a ação.
#Mas em linguagens de tipagem forte como o Python, ela simplesmente não sabe o que fazer com essa informação,
#por isso que cada tipo tem que estar escrito de forma correta.

#O Python só vai converter um tipo em outro somente se isso for possível!
print(int('1'), type('1'))

#Para alterarmos o tipo de um dado, devemos utilizar as classes, int, str, bool
print(str(1), type(str(1)))

print(int('1'), type(int('1')))

#Para somar um valor que está em str, basta alterar seu tipo.
print(int('1') + 1)

#A soma de um número float com um int (inteiro), retorna outro número float.
print(float('1') + 1)

#Em boolean uma string vazia é considerada (False) e uma 
#string com um valor mesmo que com um "espaço" é considerada (True).
print(bool('')) #False
print(bool(' ')) #True

#É possível também transformar números em strings.
print(str('11' + 'b'))