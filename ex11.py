'''Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.'''

numero = int(input("Digite um número: "))
divisores = []
def isPrime():
     for i in range(1, numero + 1):
          if numero % i == 0:
               divisores.append(i)
          numero_divisores = len(divisores)
          if numero_divisores == 2:
               print(f"{numero} é um número primo")
          else:
               print(f"{numero} não é um número primo.")

isPrime()
          

