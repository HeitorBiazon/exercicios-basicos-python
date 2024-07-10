'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

Concepts to practice
Lists and properties of lists
List comprehensions (maybe)
Functions'''
import random

lista1 = []

for i in range(random.randint(0, 5)):
     lista1.append(random.randrange(10))

def segunda_lista():
     print(f"Primera lista: {lista1}")

     nova_lista = lista1[0], lista1[-1]
     print(f"Nova lista: {nova_lista}")
segunda_lista()




