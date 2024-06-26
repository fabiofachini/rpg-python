import random
import time

class Personagem:
    def __init__(self, nome, level, vida, vida_max, exp, ataque, defesa, agilidade, destreza):
        self.nome = nome
        self.level = level
        self.vida = vida
        self.vida_max = vida_max
        self.exp = exp
        self.exp_max = vida_max * 20
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
        self.destreza = destreza

    def ganhar_exp(self, quantidade):
        self.exp = self.exp + quantidade
        if self.exp >= self.exp_max:
            self.level_up()

    def level_up(self):
        if self.level <= 20:
            self.level = self.level + 1
            self.exp = self.exp - self.exp_max
            self.exp_max = self.exp_max * 1.5  # Exemplo: aumenta a experiência máxima em 50%
            self.vida_max = self.vida_max * 1.2  # Exemplo: aumenta a vida máxima em 20%
        else: 
            self.level = 20

    def atacar(self, alvo):
        print("Rolando dado...")
        time.sleep(3)
        dado6 = random.randint(1, 6)
        print(dado6)
        time.sleep(1)
        if dado6 == 1:
            print(f"{self.nome} errou o ataque!")
            return 0
        elif dado6 == 6:
            print(f"{self.nome} fez um ataque crítico!")
            dano = int(self.ataque * 1.5) - alvo.defesa
        else:
            dano = max(0, self.ataque - alvo.defesa)

        alvo.vida = alvo.vida - dano
        return dano

    def esta_vivo(self):
        return self.vida > 0


class Batalha:
    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def iniciar_batalha(self):
        print(f"Batalha iniciada entre {self.jogador.nome} e {self.inimigo.nome}!")

        # Determinar ordem de ataque com base na agilidade
        if self.jogador.agilidade >= self.inimigo.agilidade:
            primeiro = self.jogador
            segundo = self.inimigo
            print(f"{jogador.nome} ataca primeiro")
        else:
            primeiro = self.inimigo
            segundo = self.jogador
            print(f"{inimigo.nome} ataca primeiro")
        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():
            if not self.turno(primeiro, segundo):
                break
            if not self.turno(segundo, primeiro):
                break
        print("Fim da batalha.")
        print(self.jogador.exp)

    def turno(self, atacante, alvo):
        print(f"{atacante.nome} ataca {alvo.nome}.")
        dano = atacante.atacar(alvo)
        time.sleep(3)
        print(f"Causa {dano} de dano.")
        time.sleep(1)
        print(f"Vida {alvo.nome} {max(0, alvo.vida)}/{alvo.vida_max}")
        time.sleep(3)
        if not alvo.esta_vivo():
            print(f"{alvo.nome} foi derrotado!")
            time.sleep(3)
            atacante.ganhar_exp(alvo.vida_max * 5)
            return False
        return True

# Exemplo de uso:
jogador = Personagem(nome="Herói", level=1, vida=20, vida_max=20, exp=0, ataque=15, defesa=2, agilidade=4, destreza=2)
inimigo = Personagem(nome="Monstro", level=1, vida=20, vida_max=79, exp=0, ataque=5, defesa=2, agilidade=3, destreza=2)

batalha = Batalha(jogador, inimigo)
batalha.iniciar_batalha()