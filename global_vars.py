# Mostra o que acontece durante os ataques da batalha:
class Funcao:
    # Mostra o que ocorre caso ataque acertou o alvo:
    def mostrar_texto_ataque_normal(self, retornado, mensagem):
        # Mostra o que retornará:
        dano = retornado[0]
        foi_critico = retornado[1]
        errou = True if dano == 0 else False # errou caso deu nenhum dano ("0")
        # Mensagem caso o pokemon tenha errado:
        if errou:
            mensagem.texto = "Errou o alvo"
        # Mensagem caso o pokemon tenha acertado:
        else:
            # Caso o ataque tenha sido crítico:
            if foi_critico:
                mensagem.texto = "Foi muito efetivo! Perdeu {} HP".format(dano)
            # Caso o ataque tenha sido normal:
            else:
                mensagem.texto = "Fez perder {} HP".format(dano)
    # Mostra o que ocorre caso errou o ataque:
    def mostrar_mensagem_errou(self, mensagem):
        if not mensagem.texto == "Errou o alvo":
            mensagem.texto = "Errou"
# Cria o objeto:
funcao = Funcao()