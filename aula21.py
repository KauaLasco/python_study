#Operadores lógicos
#and (e) or (ou) not (não)
#and - Todas as condições precisam  ser verdadeiras.
#Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor (falso).
#São considerados falsy (que você já viu) 0, 0.0, '', e False.
#Também existe o tipo None que é usado para representar um não valor.

entrada = input("[E]ntrada [S]air: ")
senha_digitada = input("Senha: ")

SENHA_PERMITIDA = "1234567"

if entrada == "E" and senha_digitada == SENHA_PERMITIDA:
    print("Entrada realizada com sucesso!")
elif entrada == "S":
    print("Saiu do sistema.")
else:
    print("Opção selecionada ou senha inválida!")