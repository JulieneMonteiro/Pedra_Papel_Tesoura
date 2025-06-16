def validar_escolha(escolha, opcoes):
    return escolha in opcoes

def mostrar_resultado(usuario, maquina):
    if usuario == maquina:
        print("🤝 Empate!")
        return "empate"

    if (
        (usuario == "pedra" and maquina == "tesoura") or
        (usuario == "papel" and maquina == "pedra") or
        (usuario == "tesoura" and maquina == "papel")
    ):
        print("✅ Você venceu esta rodada!")
        return "usuario"
    else:
        print("❌ A máquina venceu esta rodada!")
        return "maquina"
