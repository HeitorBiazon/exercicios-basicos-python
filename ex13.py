'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

numero_elementos = int(input("Digite o número de elementos: "))

n1 = 1
n2 = 2
for i in range(numero_elementos):
     print(n1)
     n3 = n1 + n2
     n1 = n2
     n2 = n3

