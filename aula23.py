'''Operador lógico "not"

Usado para inverter expressões.
not True = False
not False = True
'''

senha = input("Senha: ")

#Uma string vazia é avaliada como falsy, portanto if not senha. Se você não digitou a senha, não digitou nada.
if not senha:
    print("Você não digitou nada.")
#O not é muito utilizado para inverter a expressão.
  