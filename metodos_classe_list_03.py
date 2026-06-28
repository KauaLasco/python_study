#Um dos métodos da classe list é o "append". O append serve para inserir valores dentro de uma lista.

list = []

list.append(1)
list.append("Python")
list.append("Jesus IS THE GREATEST")

print(list)

print() #QUEBRA DE LINHA

#Outro método da classe list é o "clear", que serve para limpar todos os objetos/dados de uma lista.

list.clear()

print(list)

print() #QUEBRA DE LINHA

#Outro método é o "copy" que serve para copiar uma lista em outra lista diferente.

list = [1, 'Python', 'Jesus IS THE GREATEST']

l1 = list.copy()

print(f"{l1} - {id(l1)}\n{list} - {id(list)}")

print() #QUEBRA DE LINHA

#É possível alterar um valor de uma lista da seguinte forma, localizando o objeto que será alterado e atribuir
#o valor como que em uma variavel.

l1[0] = 2

print(l1)

print() #QUEBRA DE LINHA

#O método "count" serve para contar quantas vezes um determinado objeto/valor aparece em sua lista.

cores = ["Vermelho", "Azul", "Verde", "Vermelho", "Azul"]

print(cores.count("Vermelho"))
print(cores.count("Azul"))
print(cores.count("Verde"))

print() #QUEBRA DE LINHA

#Com o método "extend" você consegue inserir outras listas dentro de sua lista.

numeros = [1, 22, 15, 4, 2004, 14, 7]

cores.extend(numeros)

print(cores)

cores.extend(["JESUS IS THE GREATEST!"])

print(cores)

print() #QUEBRA DE LINHA

#O método "index" serve para você localizar a posição de "tal" objeto na lista.

print(cores.index(22))
print(cores[6])

print(cores.index("JESUS IS THE GREATEST!"))
print(cores[12])

#Em valores repetidos, o index retorna apenas a posição do primeiro objeto. Por exemplo: tem 3 letras A na lista,
#a primeira está na 3 posição, a segunda na 7 posição e a terçeira na 14 posição. O index vai retornar a posição
#da primeira, no caso a terçeira posição (3).
print() #QUEBRA DE LINHA

#Temos o "pop" também. Uma lista é organizada como em forma de "pilha". O primeiro elemento é o de baixo
#e o último é o prato de cima pois foi o último a ser colocado lá.
#É assim que o "pop" funciona.

print(cores.pop())
print(cores.pop())
print(cores.pop())
print(cores.pop(2))
print(cores.pop(0))

#O "pop" remove elementos de uma lista.

#Assim como o "remove faz"

print(cores)

cores.remove(2004)
print(cores)
#Porém, diferentemente do "pop", ao invés de você passar o índice do objeto, você deve passar o objeto em si.
#Caso haja mais de um mesmo objeto, o "remove", vai remover apenas o primeiro.

#Temos o "reverse" também, que espelha a lista, à põe de trás pra frente.

cores.reverse()
print(cores)