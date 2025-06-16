import tkinter as tk

from game.engine import jogar


def iniciar_interface():
    janela = tk.Tk()
    janela.title("✊✋✌️ Pedra, Papel ou Tesoura")
    janela.geometry("500x600")
    janela.configure(bg="#eef2f3")

    pontos_usuario = tk.IntVar(value=0)
    pontos_maquina = tk.IntVar(value=0)
    resultado_var = tk.StringVar(value="Melhor de 3! \n Escolha uma jogada para começar!")
    mensagem_final = tk.StringVar(value="")

    fonte_titulo = ("Segoe UI", 18, "bold")
    fonte_texto = ("Segoe UI", 12)

    # Cabeçalho
    tk.Label(janela, text="🎮 Pedra, Papel ou Tesoura", font=fonte_titulo, bg="#eef2f3", fg="#333").pack(pady=20)

    # Resultado
    resultado_frame = tk.Frame(janela, height=100, bg="#eef2f3")
    resultado_frame.pack_propagate(False)
    resultado_frame.pack(pady=10, fill="x")

    resultado_label = tk.Label(
        resultado_frame, textvariable=resultado_var,
        font=("Segoe UI", 13, "italic"), bg="#dff0d8", fg="#3c763d",
        bd=2, relief="groove", padx=10, pady=10, wraplength=400
    )
    resultado_label.pack(expand=True)

    # Função de reinício do jogo
    def reiniciar_jogo():
        pontos_usuario.set(0)
        pontos_maquina.set(0)
        resultado_var.set("Escolha uma jogada para começar!")
        mensagem_final.set("")
        resultado_label.configure(bg="#dff0d8", fg="#3c763d")
        botao_reiniciar.pack_forget()  # Esconde o botão

    # Escolha
    def escolher(opcao):
        if pontos_usuario.get() >= 3 or pontos_maquina.get() >= 3:
            return

        maquina, resultado = jogar(opcao)

        if resultado == "usuario":
            pontos_usuario.set(pontos_usuario.get() + 1)
            resultado_var.set(f"✅ Você escolheu {opcao}\n💻 Máquina escolheu {maquina}\nVocê venceu esta rodada!")
            resultado_label.configure(bg="#d9edf7", fg="#31708f")
        elif resultado == "maquina":
            pontos_maquina.set(pontos_maquina.get() + 1)
            resultado_var.set(f"❌ Você escolheu {opcao}\n💻 Máquina escolheu {maquina}\nVocê perdeu esta rodada.")
            resultado_label.configure(bg="#f2dede", fg="#a94442")
        else:
            resultado_var.set(f"🤝 Ambos escolheram {opcao}. Empate!")
            resultado_label.configure(bg="#fcf8e3", fg="#8a6d3b")

        # Vitória
        if pontos_usuario.get() == 3:
            mensagem_final.set("🎉 Parabéns, você venceu o jogo!")
            botao_reiniciar.pack(pady=15)
        elif pontos_maquina.get() == 3:
            mensagem_final.set("😢 A máquina venceu o jogo.")
            botao_reiniciar.pack(pady=15)

    # Botões
    botoes_frame = tk.Frame(janela, bg="#eef2f3")
    botoes_frame.pack(pady=20)

    def criar_botao(texto, cor, comando):
        return tk.Button(
            botoes_frame, text=texto, font=fonte_texto,
            bg=cor, fg="white", width=12, height=2,
            bd=0, activebackground="#333", cursor="hand2",
            command=comando
        )

    criar_botao("✊ Pedra", "#4CAF50", lambda: escolher("pedra")).pack(side=tk.LEFT, padx=10)
    criar_botao("✋ Papel", "#2196F3", lambda: escolher("papel")).pack(side=tk.LEFT, padx=10)
    criar_botao("✌️ Tesoura", "#f44336", lambda: escolher("tesoura")).pack(side=tk.LEFT, padx=10)

    # Placar
    placar_frame = tk.Frame(janela, bg="#eef2f3")
    placar_frame.pack(pady=20)

    tk.Label(placar_frame, text="🏆 Placar", font=fonte_titulo, bg="#eef2f3", fg="#444").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(placar_frame, text="Você:", font=fonte_texto, bg="#eef2f3").grid(row=1, column=0, sticky="e", padx=5)
    tk.Label(placar_frame, textvariable=pontos_usuario, font=fonte_texto, fg="green", bg="#eef2f3").grid(row=1, column=1, sticky="w")

    tk.Label(placar_frame, text="Máquina:", font=fonte_texto, bg="#eef2f3").grid(row=2, column=0, sticky="e", padx=5)
    tk.Label(placar_frame, textvariable=pontos_maquina, font=fonte_texto, fg="red", bg="#eef2f3").grid(row=2, column=1, sticky="w")

    # Mensagem final
    mensagem_final_label = tk.Label(janela, textvariable=mensagem_final,
                                    font=("Segoe UI", 14, "bold"),
                                    bg="#eef2f3", fg="#6a1b9a")
    mensagem_final_label.pack(pady=10)

    rodape = tk.Label(janela, text="Desenvolvido por Juliene Monteiro", 
            font=("Segoe UI", 10), bg="#eef2f3", fg="#999")
    rodape.pack(side="bottom", pady=10)

    # 🔁 Botão de reinício (inicia escondido)
    botao_reiniciar = tk.Button(janela, text="🔁 Jogar Novamente", font=fonte_texto,
                                bg="#6a1b9a", fg="white", width=18, height=2,
                                command=reiniciar_jogo)
    botao_reiniciar.pack_forget()

    janela.mainloop()