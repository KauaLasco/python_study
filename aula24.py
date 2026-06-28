#Operadores in e not in (entre e não entre)
#Strings são iteraveis 
# 0 1 2 3  
# K a u ã
#-4-3-2-1

nome = "Kauã"

print(nome[2])
print(nome[3])

#Quando eu checko "in" eu posso checkar letra por letra.

print("a" in nome) #True
print("x" in nome) #False
print(10 * "-")

#O "not in" é o inverso. Se a letra não estiver na variavel "nome" vai retornar true e não false.

print("as" not in nome) #False
print("x" not in nome) #True

nome = input("Digite o seu nome: ")

encontrar = input("Digite o que você quer encotrar: ")

if encontrar in nome:
    print(f"{encontrar} está no nome.")
else:
    print(f"{encontrar} não está no nome.")