import random

def jogar(escolha_usuario):
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_maquina = random.choice(opcoes)

    if escolha_usuario == escolha_maquina:
        resultado = "empate"
    elif (
        (escolha_usuario == "pedra" and escolha_maquina == "tesoura") or
        (escolha_usuario == "papel" and escolha_maquina == "pedra") or
        (escolha_usuario == "tesoura" and escolha_maquina == "papel")
    ):
        resultado = "usuario"
    else:
        resultado = "maquina"

    return escolha_maquina, resultado
