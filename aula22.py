'''Operador lógico (or)

or - qualquer condição verdadeira avalia
toda a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro,
a expressão inteira será avaliada naquele valor. 
São considerados falsy (que você já viu)
0, 0.0, '', False
Também existe o None que é usado para representar
um não valor.
'''

entrada = input("[E]ntrada [S]air: ")
senha_digitada = input("Senha: ")

SENHA_PERMITIDA = "1234567"

if (entrada == "E" or entrada == "e") and senha_digitada == SENHA_PERMITIDA:
    print("Entrada realizada com sucesso!")
elif entrada == "S":
    print("Saiu do sistema.")
else:
    print("Opção selecionada ou senha inválida!")

#Avaliação de curto-circuito
senha = input("insira: ") or "Sem senha"
print(senha)