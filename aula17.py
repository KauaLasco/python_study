condicao = False
condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print('código para condição 1')
elif condicao2:
    pass #Você pode utilizar o "pass" ou os "..." para
#passar para próxima linha e não executar o código.
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')


#Caso uma condição seja atendida e executada o bloco condicional
#para de funcionar e executa o resultado da condição que correspondeu.

#Por exemplo, no bloco condicional há muitos elif, e suponhamos
#que as 4 ultimas condicões sejam as mesmas, porém quando o código
#chegar na primeira condição que corresponde com essas quatros,
#ele exibirá somente o resultado desta primeira e não executará
#nada abaixo dela.