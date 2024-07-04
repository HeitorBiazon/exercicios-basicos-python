'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''
import random

contador = 0
num = random.randrange(0, )

while True:
     num_usuario = int(input("Digite um número inteiro para tentar advinhar: "))
     contador +=1
     if num_usuario == num:
          jogo = input(f"Você acertou em {contador} tentativas. Aperte qualquer tecla para prosseguir. ")
     elif num_usuario > num:
          print("Número maior do que o valor correto. ")
     else:
          print("Número menor do que o valor correto. ")

     continuar = input("Aperte qualquer tecla para continuar ou digite 'sair' para encerrar o jogo. ").lower()

     if continuar == "sair":
          print(f"Jogo encerrado.")
          break
     