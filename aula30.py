#Escrevendo o código para uma pessoa. (DEIXAR O CÓDIGO LIMPO)

'''
CONSTANTE = "Variaveis" que não mudam o valor. Sempre devem estar em letras maiúsculas.
Muitas condições no mesmo if = (ruim) torna o código menos legivel e complexo de entender.
    <- Contagem de complexidade = (ruim) quanto mais blocos de código dentro de outros blocos, torna o código
menos legivel e complexo de entender.

'''

velocidade = 61 #Velocidade atual do carro.
local_carro = 90 #Local em que o carro está na estrada.

RADAR_1 = 60 #Velocidade máxima do radar 1.
LOCAL_1 = 100 #Local aonde o radar 1 está.
RADAR_RANGE = 1 #A distância de onde o radar pega.

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = velocidade_carro_passou_radar_1 and carro_passou_radar_1

if carro_multado_radar_1:
    print("A velocidade do carro passou do radar 1 e foi multado.")

# if velocidade_carro_passou_radar_1 and carro_passou_radar_1:
#     print("A velocidade do carro passou do radar 1 e foi multado.")

# if velocidade > RADAR_1:
#     print("Velocidade do carro passou do radar 1.")

# if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
# local_carro <= (LOCAL_1 + RADAR_RANGE) and \
# velocidade > RADAR_1:
#     print("O carro foi multado no radar 1.")