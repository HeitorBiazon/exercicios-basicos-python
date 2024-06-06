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
     print(f"O número {numero} é impar")

# %%
