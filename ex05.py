'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)'''

## Exibir os elementos em comum de duas listas, sem repetir elementos.
import random

lista_a = []
lista_b = []

for i in range(random.randint(0, 5)):
     lista_a.append(random.randrange(50,200))

for i in range(random.randrange(0,10)):
     lista_b.append(random.randrange(0,100))

print(lista_a)
print(lista_b)

nova_lista = list(set(lista_a) & set(lista_b)) 

print(nova_lista)