'''Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)'''

## Verificar se uma string é um palíndromo

texto = input("Digite um texto qualquer: ")
texto_inverso = texto[::-1]

if texto == texto_inverso:
     print("É um palíndromo")
else:
     print("Não é um palíndromo")