from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
import time
import random
from dialogos import executar_dialogo_turno, executar_dialogo_hp

DIFICULDADES = {
    "facil": {
        'nome': 'Fácil',
        'heroi_attr': 'Alta', 
        'vilao_attr': 'Baixa', 
        'pocoes_v': 3, 'pocoes_a': 2, 'pocoes_d': 2
    },
    "media": {
        'nome': 'Média',
        'heroi_attr': 'Média', 
        'vilao_attr': 'Média', 
        'pocoes_v': 2, 'pocoes_a': 1, 'pocoes_d': 1
    },
    "dificil": {
        'nome': 'Difícil',
        'heroi_attr': 'Média', 
        'vilao_attr': 'Alta', 
        'pocoes_v': 1, 'pocoes_a': 1, 'pocoes_d': 0
    },
    "muito_dificil": {
        'nome': 'Muito Difícil',
        'heroi_attr': 'Baixa', 
        'vilao_attr': 'Alta', 
        'pocoes_v': 1, 'pocoes_a': 0, 'pocoes_d': 0
    }
}

def iniciar_batalha(config_dificuldade):
    try:
        cfg = config_dificuldade
        
        heroi = Heroi('Link', 25, 200, 50, 30, cfg['heroi_attr'], 
                      pocoes_vida=cfg['pocoes_v'], 
                      pocoes_ataque=cfg['pocoes_a'], 
                      pocoes_defesa=cfg['pocoes_d'])
        
        vilao = Vilao('Ganon', 100, 200, 40, 20, cfg['vilao_attr'])
        
        npc = Personagem('Zelda', 1, 1, 1, 1, 'Média')

    except ValueError as e:
        print(f"Erro ao criar personagem: {e}")
        return

    print("\n--- INÍCIO DO JOGO ---")
    print(f"Dificuldade: {cfg['nome']}")
    print(heroi)
    print(vilao)
    print(f"NPC: {npc.nome} (Vida: {npc.vida})")
    print("-" * 30)
    
    print(f"O vilão {vilao.nome} capturou {npc.nome}!")

    turno = 1
    jogo_ativo = True
    
    dialogo_turno_3_aconteceu = False
    dialogo_hp_70_aconteceu = False
    
    while jogo_ativo and heroi.esta_vivo() and vilao.esta_vivo():
        print(f"\n--- TURNO {turno} ---")
        print(f"{heroi.nome}: {heroi.vida}/{heroi.vida_maxima} HP")
        print(f"{vilao.nome}: {vilao.vida}/{vilao.vida_maxima} HP")
        print("-" * 20)
        
        if turno == 3 and not dialogo_turno_3_aconteceu:
            dialogo_turno_3_aconteceu = True
            executar_dialogo_turno(heroi, vilao)
            time.sleep(1)
        
        print(f"É a vez de {heroi.nome}!")
        
        acao_realizada = False
        while not acao_realizada:
            acao = ""
            opcoes_validas = ["1", "2", "3", "4"]
            
            while acao not in opcoes_validas:
                acao = input("O que você deseja fazer?\n 1 - Ataque Normal\n 2 - Ataque Especial (Arriscado)\n 3 - Usar Poção\n 4 - Tentar Salvar Refém\n> ").strip()

            if acao == "1":
                heroi.atacar(vilao)
                acao_realizada = True
            elif acao == "2":
                heroi.atacar_especial(vilao)
                acao_realizada = True
            elif acao == "3":
                if heroi.usar_pocao():
                    acao_realizada = True
                else:
                    print("Voltando ao menu de ações...")
                    acao_realizada = False
            elif acao == "4":
                if heroi.salvar_refem(vilao, npc):
                    print("O herói salvou o refém!")
                    jogo_ativo = False
                else:
                    print("A tentativa de salvamento falhou e você perdeu o turno.")
                acao_realizada = True
        
        if vilao.esta_vivo() and (vilao.vida < (vilao.vida_maxima * 0.7)) and not dialogo_hp_70_aconteceu:
            dialogo_hp_70_aconteceu = True
            executar_dialogo_hp(heroi, vilao)
            time.sleep(1)
        
        time.sleep(1)

        if not vilao.esta_vivo() or not jogo_ativo:
            break

        print(f"\nÉ a vez de {vilao.nome}!")
        time.sleep(1)
        
        chance_especial = 0.7 if vilao.em_forma_final else 0.5 

        if random.random() < chance_especial:
            print(f"{vilao.nome} vai arriscar um ataque especial!")
            vilao.atacar_especial(heroi)
        else:
            print(f"{vilao.nome} decide por um ataque normal.")
            vilao.atacar(heroi)
        
        turno += 1

    print("\n--- FIM DA BATALHA ---")
    
    if (not vilao.esta_vivo()) or (jogo_ativo == False and heroi.esta_vivo()):
        print(f"{heroi.nome} venceu!")
    else:
        print(f"{vilao.nome} venceu! O reino está condenado.")

    print("\n--- STATUS FINAL ---")
    print(heroi)
    print(vilao)
    print("\nPressione ENTER para voltar ao menu principal.")
    input()

def escolher_dificuldade():
    print("\n--- Escolha a Dificuldade ---")
    print("1: Fácil (Herói Forte, Vilão Fraco, Muitas Poções)")
    print("2: Média (Balanceado)")
    print("3: Difícil (Herói Fraco, Vilão Forte, Poucas Poções)")
    print("4: Muito Difícil (Herói Fraco, Vilão Forte, Quase sem Poções)")
    
    while True:
        escolha = input("> ").strip()
        if escolha == '1':
            return DIFICULDADES["facil"]
        elif escolha == '2':
            return DIFICULDADES["media"]
        elif escolha == '3':
            return DIFICULDADES["dificil"]
        elif escolha == '4':
            return DIFICULDADES["muito_dificil"]
        else:
            print("Opção inválida. Tente novamente.")

def main():
    config_atual = DIFICULDADES["media"]

    while True:
        print("\n" + "="*30)
        print("      BEM-VINDO AO JOGO")
        print("="*30)
        print(f"Dificuldade Atual: {config_atual['nome']}")
        print("\n1: Iniciar Jogo")
        print("2: Escolher Dificuldade")
        print("3: Sair")
        
        escolha = input("> ").strip()
        
        if escolha == '1':
            iniciar_batalha(config_atual)
        elif escolha == '2':
            config_atual = escolher_dificuldade()
            print(f"Dificuldade atualizada para: {config_atual['nome']}")
        elif escolha == '3':
            print("Obrigado por jogar! Até mais.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()