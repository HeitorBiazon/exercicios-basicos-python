#%% EXERCÍCIO 1
'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

name = input("Give me your name: ")

age = int(input("Enter your age: "))

print(f"Você irá fazer 100 anos de idade em {2024 + 100}")

#%% -- EXERCÍCIO 2
'''
Exercise 2 (and Solution)
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

numero = int(input("Digite um número: "))

if (numero & 2 == 0) and (numero & 4 == 0):
     print(f"O número {numero} é par e é divisível por 4.")
elif numero % 2 == 0:
     print(f"O número {numero} é par e não é divisível por 4")
else:
     print(f"O número {numero} é impar ")

# %%
'''Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.'''

## Exibir elementos da lista1 que são menores que 5
lista1 = [4, 22, 1, 3, 9, 7, 11, 12, 2, 27, 2, 15]
nova_lista = []

for i in lista1:
     if i < 5:
          nova_lista.append(i)
print(nova_lista)

## Exibir elementos da lista1 que são menores que o número que foi pedido ao usuário e que está armazenado na variável numero
numero = int(input("Digite um número: "))
lista2 = []
for i in lista1:
     if i < numero:
          lista2.append(i)
print(lista2)
# %%
'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

## Exibir os divisores abaixo de 1000 de um determinado número 

numero = int(input("Digite um número: "))
divisores = []
for i in range(1, numero + 1):
     if numero % i == 0:
          divisores.append(i)
print(divisores)

# %%
