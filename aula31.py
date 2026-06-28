'''
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
'''

v1 = 'a'
v2 = 'b'

print(id(v1))
print(id(v2))

#As vezes queremos sinalizar se alguma variável ou se o código passou por um if. Para isso podemos utilizar
#a seguinte estrutura:

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo!")
else:
    print("Não faça algo!")

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

#Com isso temo uma "bandeirinha" fincada agora no if. Nos avisando sempre que o código passar por lá.

if passou_no_if is None:
    print("Não passou no if!")

if passou_no_if is not None:
    print("Passou no if!")