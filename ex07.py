"""Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."""
#Exibir os elementos pares de uma lista

lista_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [x for x in lista_a if lista_a % 2 == 0]

print(b)
