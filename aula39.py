'''
Iterando strings com while
'''

nome = 'Kauã Lasco dos Santos'

ind_nome = len(nome)
num_ind = 0
str_nova = ' ' #Para os carcteres serem adicionados a nova string, a variavel dela deve estar declarada, fora
#do loop. Porque se não toda vez que voltar no começo do loop, ela voltará a ser vazia.

while num_ind < ind_nome:
    letra = nome[num_ind]
    str_nova += letra + " "
    #str_nova += f'*{letra}' PODEMOS ACRESCENTAR AS LETRAS JÁ COM O ASTERÍSCO NA NOVA STRING DESSA MANEIRA.
    print(str_nova)
    num_ind += 1

str_nova = str_nova.replace(" ", "*") #Troca caracteres específicos por outros desejados/selecioados. (replace)
print(str_nova)