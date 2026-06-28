a = 'A'
b = 'B'
c = 1.1
formato = ''

print(formato)

#Tudo em Pyhton é um objeto! Pois tudo tem métodos!
#Um objeto tem ações, ele pode realizar algumas ações!
#E essas ações são chamadas de métodos!

formato = ''.format(a, b, c) #no momento o que está em parênteses
#são argumentos, mas depois podem ser transformados em parâmetros!

formato = 'a={}, b={}, c={}'.format(a, b, c) #Como podemos ver
#o método (format) faz com que consigamos inserir os valores
#de variáveis dentro de strings, porém a cada chave inserida como podemos ver no exemplo,
#é inserido o valor da variável que você digitou sequêncialmente no (format)!

print(formato)

#É possível escrever isso de outras formas!
string = 'a={}, b={}, c={}'
formato = string.format(a, b, c)
print(formato)

#Agora suponhamos que você deseje alterar a casa decimal da variável C
#Para isso é necessário somente que você insira o :.2f dentro da chave.
string = 'a={}, b={}, c={:.2f}'
formato = string.format(a, b, c)
print(formato)

#Quando aparecer o erro "out of range" significa que o valor procurado não existe,
#ou seja, não tem! Ou seja, você está buscando uma coisa que já acabou!

#Você pode alterar também as sequências das chaves, inserido o número da ordem que corresponde as variáveis do format
#Lembre-se, sempre se inicia no 0, ou seja a primeira variável é o número 0!

string = 'a={1}, b={0}, c={2:.2f}'
formato = string.format(a, b, c)
print(formato)

#parâmetro nomeado é o nome que damos para as coisas que inserimos dentro da chamada das funções,
#ou da criação das funções

string = 'a={nome2}, b={nome1}, b={nome1}, c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)
#Tudo depois de uma nomeação ter sido feita dentro dos parênteses, tem que ser nomeado também!
