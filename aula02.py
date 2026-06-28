#A função print() é utilizada para exibir as coisas na tela!
#E ela recebe algo que chamamos de "argumento".
#Argumento é algo que geralmente passamos para funções, assim como a função print().

print(12, 34)

#Para colocarmos/inserirmos outros argumentos em uma função, devemos utilizar a vírgula (,)!

#Existe um atalho que se você clicar em uma linha e depois acionar as teclas CTRL + C e depois CTRL + V, essa linha será copiada para a linha de baixo!

print(56, 78)

#Esses argumentos que estamos passando na função print(), são argumentos não nomeados!
#Pois os inserimos somente para a função print() exibir na tela.

print(9, 10, sep='-')

#Podemos utilizar também argumentos nomeados como o sep=''.
#Ele cria/substitui uma separação entre argumentos inseridos na função.
#Para inserir o separador desejado, basta inseri-lo dentros das aspas duplas ou simples da função sep=""!

print(11, 12, sep="@")

#Existem caractéres que não aparecem porém eles estão sendo executados!
#Como por exemplo a quebra de linha que é representada pelo argumento \r\n
# r para "return" e n para "line feed"!

#\r\n = CRLF
#\N = LF (LINUX ou em Windows mais atuais)

#Para inserir a quebra de linha em uma função, devemos utilizar o argumento nomeado end=''!

print(22, 11, end='\r\n')
print(7,12, end='\n')
print(14, 3, end='!')
print(1)

#Como podemos ver, podemos alterar o final do que vai ser exibido em um argumento!
#Porém, podemos ver também que caso alteremos, não será realizado a quebra de linha e teremos que adiciona-la novamente!

print(22, 22, end='##\n')
print(7, 14, end='\n##')
print(12, 11, end='\r\n')

#Podemos adicionar a quebra de linha antes ou depois também, como pedemos ver no exemplo acima!

#Na programação não podemos utilizar letras maiúsculas aonde quisermos, pois o python o identifica como sendo outro caractere ocasionando assim um erro!
