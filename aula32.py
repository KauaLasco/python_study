"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se esse número é par ou impar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro.

"""
numero = input("Digite um número e verifique se ele é 'impar' ou 'par': ")
numero_int = int(numero)

if numero_int % 2 == 0:
    print(f"O número {numero_int} é par!")
else:
    print(f"O número {numero_int} é impar!")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.

"""
horario = input("Que horas são? ")

try:
    horario_float = float(horario)   
    if horario_float >= 0 and horario_float <= 11.59:
        print("Bom dia!")
    elif horario_float >= 12 and horario_float <= 17.59:
        print("Boa tarde!")
    elif horario_float >= 18 and horario_float <= 23.59:
        print("Boa noite!")
    else:
        print("Insira um horário válido!")
except:
    print("O horário deve estar no formato 24h.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome
é curto"; se tiver entre 5 e 6 letras, escreva "seu nome é médio"; maior que 6 escreva "seu nome é muito
grande"

"""
nome_usuario = input("Insira seu nome: ")
nome_usuario_str = str(nome_usuario)
verificar_se_ha_numero = [caractere for caractere in nome_usuario_str if caractere.isdigit()]

def perguntar_nome():
    if verificar_se_ha_numero:
        print("Insira somente letras.")
        exit
    elif len(nome_usuario_str) > 0 and len(nome_usuario_str) <= 4:
        print("Seu nome é curto.")
    elif len(nome_usuario_str) > 4 and len(nome_usuario_str) <= 6:
        print("Seu nome é médio.")
    elif len(nome_usuario_str) > 6:
        print("Seu nome é muito grande.")

perguntar_nome()

