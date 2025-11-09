from personagem import Personagem

class Vilao(Personagem):
    def __init__(self, nome, idade, vida, ataque, defesa, maldade):
        super().__init__(nome, idade, vida, ataque, defesa, maldade)
        
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")

        self.ataque_original = ataque
        self.defesa_original = defesa
        
        self.pode_transformar = True 
        self.em_forma_final = False
        self.anger = 0 

    def transformar(self):
        if not self.pode_transformar:
            return

        print(f"\n!!! {self.nome} solta um rugido ensurdecedor! !!!")
        print(f"!!! {self.nome} está se transformando em sua forma final! !!!\n")
        
        self.vida = self.vida_maxima
        self.ataque = int(self.ataque_original * 1.5)
        self.defesa = int(self.defesa_original * 1.5)
        self.especial_atributo = 'Alta'
        
        self.em_forma_final = True
        self.pode_transformar = False

        print(f"Os status de {self.nome} aumentaram! [Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}]")

    def receber_dano(self, quantidade):
        super().receber_dano(quantidade)
        
        if self.esta_vivo() and (self.vida < (self.vida_maxima * 0.4)) and self.pode_transformar:
            self.transformar()

    def __str__(self):
        base_info = super().__str__()
        forma = "(Forma Final)" if self.em_forma_final else ""
        return f'Vilão: [{base_info}] {forma}'