import random

class Personagem:
    def __init__(self, nome, idade, vida, ataque, defesa, especial_atributo="Média"):
        self.nome = nome
        self.idade = idade
        self.vida_maxima = vida
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.especial_atributo = especial_atributo

    def atacar(self, alvo):
        if not self.esta_vivo():
            print(f"{self.nome} não pode atacar, pois está derrotado.")
            return

        print(f"{self.nome} usa um ataque normal em {alvo.nome}!")
        
        dano_base = self.ataque - alvo.defesa
        variacao = random.uniform(0.8, 1.2)
        dano_calculado = int(dano_base * variacao)
        dano_final = max(1, dano_calculado)
        
        alvo.receber_dano(dano_final)

    def atacar_especial(self, alvo):
        if not self.esta_vivo():
            return

        niveis_chance = {
            'Baixa': 0.3,
            'Média': 0.5,
            'Alta': 0.7
        }
        chance_sucesso = niveis_chance.get(self.especial_atributo, 0.5)

        if random.random() <= chance_sucesso:
            print(f"{self.nome} usa seu poder especial e acerta em cheio!")
            dano_base = (self.ataque * 2) - alvo.defesa
            variacao = random.uniform(0.8, 1.2)
            dano_calculado = int(dano_base * variacao)
            dano_final = max(2, dano_calculado)
            
            alvo.receber_dano(dano_final)
        else:
            print(f"{self.nome} tenta usar seu poder, mas falha e perde o turno!")

    def receber_dano(self, quantidade):
        chance_esquiva = random.randint(1, 10)
        numero_sorte_esquiva = random.randint(1, 10)
        
        if chance_esquiva == numero_sorte_esquiva:
            print(f"  {self.nome} se esquivou do ataque e não recebeu dano!")
            return

        self.vida -= quantidade
        if self.vida < 0:
            self.vida = 0
        print(f"  {self.nome} recebeu {quantidade} de dano. Vida atual: {self.vida}")

        if not self.esta_vivo():
            print(f"  {self.nome} foi derrotado!")

    def esta_vivo(self):
        return self.vida > 0

    def upgrade_vida(self, incremento=10):
        self.vida += incremento
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def __str__(self):
        status = "Vivo" if self.esta_vivo() else "Derrotado"
        return f'Personagem: {self.nome} (Vida: {self.vida}/{self.vida_maxima}, Atk: {self.ataque}, Def: {self.defesa}, Atr: {self.especial_atributo}) - {status}'