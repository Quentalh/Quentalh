from personagem import Personagem
import random

class Heroi(Personagem):
    def __init__(self, nome, idade, vida, ataque, defesa, bondade, pocoes_vida=1, pocoes_ataque=1, pocoes_defesa=1):
        super().__init__(nome, idade, vida, ataque, defesa, bondade)
        self.pocoes_vida = pocoes_vida
        self.pocoes_ataque = pocoes_ataque
        self.pocoes_defesa = pocoes_defesa
        self.limite_status = 50

    def usar_pocao(self):
        print("Qual poção você quer usar?")
        print(f"1: Vida (Restantes: {self.pocoes_vida})")
        print(f"2: Ataque (Restantes: {self.pocoes_ataque})")
        print(f"3: Defesa (Restantes: {self.pocoes_defesa})")
        print("4: Voltar")

        while True:
            resp = input("> ").strip()
            
            if resp == "1":
                if self.pocoes_vida <= 0:
                    print("Você não tem mais poções de vida! Escolha outra.")
                    continue
                if self.vida == self.vida_maxima:
                    print("Sua vida já está no máximo! Escolha outra.")
                    continue
                
                self.pocoes_vida -= 1
                cura = 50
                self.vida += cura
                if self.vida > self.vida_maxima:
                    self.vida = self.vida_maxima
                print(f"{self.nome} usou Poção de Vida! Vida atual: {self.vida}/{self.vida_maxima}")
                return True

            elif resp == "2":
                if self.pocoes_ataque <= 0:
                    print("Você não tem mais poções de ataque! Escolha outra.")
                    continue
                if self.ataque >= self.limite_status:
                    print(f"Seu ataque já está no limite máximo ({self.limite_status})! Escolha outra.")
                    continue
                
                self.pocoes_ataque -= 1
                aumento = 10
                self.ataque += aumento
                if self.ataque > self.limite_status:
                    self.ataque = self.limite_status
                print(f"{self.nome} usou Poção de Ataque! Ataque atual: {self.ataque}")
                return True

            elif resp == "3":
                if self.pocoes_defesa <= 0:
                    print("Você não tem mais poções de defesa! Escolha outra.")
                    continue
                if self.defesa >= self.limite_status:
                    print(f"Sua defesa já está no limite máximo ({self.limite_status})! Escolha outra.")
                    continue

                self.pocoes_defesa -= 1
                aumento = 10
                self.defesa += aumento
                if self.defesa > self.limite_status:
                    self.defesa = self.limite_status
                print(f"{self.nome} usou Poção de Defesa! Defesa atual: {self.defesa}")
                return True

            elif resp == "4":
                print(f"{self.nome} decide não usar poções.")
                return False

            else:
                print("Opção inválida, tente novamente.")

    def salvar_refem(self, vilao, npc):
        if self.vida < vilao.vida:
            print(f"Você não tem energia para salvar {npc.nome} no momento.")
            return False

        chance = self.vida / vilao.vida
        print(f"Você tem uma chance de {chance*10:.2f}% de salvar {npc.nome}.")
        
        while True:
            opcao = input("Deseja tentar?\n\n 1 - Sim\n 2 - Não\n> ").strip()
            
            if opcao == "1":
                if random.random() <= 0.1 * chance:
                    print(f"Você salvou {npc.nome} e escapou, parabéns!")
                    return True
                else:
                    print(f"{vilao.nome} te impediu de tentar salvar {npc.nome}.")
                    return False
            elif opcao == "2":
                return False
            else:
                print("Opção inválida, tente novamente.")

    def __str__(self):
        base_info = super().__str__()
        pocoes_str = f"Poções V:{self.pocoes_vida}, A:{self.pocoes_ataque}, D:{self.pocoes_defesa}"
        return f'Herói: [{base_info}, {pocoes_str}]'