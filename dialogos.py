import time

def checar_transformacao_dialogo(vilao):
    if vilao.anger >= 2 and vilao.pode_transformar:
        print("\n" + "="*30)
        print(f"Você esgotou a paciencia de {vilao.nome}!")
        print("Ele não vai esperar mais!")
        print("="*30 + "\n")
        time.sleep(2)
        vilao.transformar()

def executar_dialogo_turno(heroi, vilao):
    print("\n" + "-"*30)
    print(f"{vilao.nome}: 'Você é persistente, {heroi.nome}. Mas sua esperança é inútil.'")
    time.sleep(1)
    
    escolha = ""
    while escolha not in ['1', '2', '3']:
        escolha = input("O que você responde?\n 1: 'Sua tirania acaba aqui!'\n 2: 'Você fala demais para quem vai perder.'\n 3: (Ficar em silêncio)\n> ").strip()

    if escolha == '1':
        print(f"{vilao.nome}: 'Palavras vazias. Você não é o primeiro a dizê-las.'")
    elif escolha == '2':
        print(f"{vilao.nome}: '... Insolente! Vou adorar quebrar seu espírito.'")
        vilao.anger += 1
    elif escolha == '3':
        print(f"{vilao.nome}: 'Silêncio? Bom. Prepare-se para o seu túmulo.'")
    
    print("-" * 30 + "\n")

def executar_dialogo_hp(heroi,vilao):
    print("\n" + "-"*30)
    print(f"{vilao.nome}: 'Argh! Você... você é mais forte do que eu pensava!'")
    time.sleep(1)

    escolha = ""
    while escolha not in ['1', '2', '3']:
        escolha = input("O que você responde?\n 1: 'Renda-se agora e talvez eu poupe sua vida.'\n 2: 'Este é o seu fim, monstro!'\n 3: 'Eu só estou começando.'\n> ").strip()

    if escolha == '1':
        print(f"{vilao.nome}: 'Poupar? Hahaha! Eu nunca vou me render a você!'")
    elif escolha == '2':
        print(f"{vilao.nome}: 'Monstro? Você ousa?! Vou lhe mostrar o verdadeiro terror!'")
        vilao.anger += 1
    elif escolha == '3':
        print(f"{vilao.nome}: 'Impossível! Ninguém zomba de mim!'")
        vilao.anger += 1
    
    print("-" * 30 + "\n")
    
    checar_transformacao_dialogo(vilao)