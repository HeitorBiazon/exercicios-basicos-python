'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock'''
while True:
    print("Jogo de Pedra-Papel-Tesoura")

    jogador1 = input("Digite para escolher entre 'pedra', 'papel' ou 'tesoura' para o jogador 1: ").upper()
    jogador2 = input("Digite para escolher entre 'pedra', 'papel' ou 'tesoura' para o jogador 2: ").upper()

    if jogador1 == jogador2:
        print("Empate. Ambos são iguais")
     
    elif (jogador1 == "PEDRA" and jogador2 == "TESOURA") or (jogador1 == "TESOURA" and jogador2 == "PAPEL") or (jogador1 == "PAPEL" and jogador2 == "PEDRA"):
        print(f"{jogador1} ganha de {jogador2}, jogador 1 ganhar do jogador 2")
     
    else:
        print(f"{jogador2} ganha de {jogador1}, jogador 2 ganhar do jogador 1")
          
    continuar = input("Deseja começar um novo jogo? (s para continuar/n para papar) ").upper()
    if continuar == "N":
        break
