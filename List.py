# A list that contains the squares of the numbers 1 to 100
liste_der_Quadrate = []
n = 1
while n <= 100:
    liste_der_Quadrate.append(n ** 2)
    n = n + 1
print(f'Die Liste der Quadratzahlen: {liste_der_Quadrate} \n')
print(f'Die ersten drei Elemnte der Liste  sind {liste_der_Quadrate [:3]},\n')
print(f'und die letzten drei sind {liste_der_Quadrate[-3:]}. \n')

# The sum of all elements in that list:

    # liste_der_Quadrate[0] + liste_der_Quadrate[1] + liste_der_Quadrate[2] + etc.
summe = 0
i = 0
while i <= 99:
    summe = summe + liste_der_Quadrate[i]
    i = i + 1
print(f'Die Summe aller Elemente der liste ist {summe}.')

# This code is to test whether my program works or not: print(summe - ((100 * 101 * 201) / 6)). If the result is zero,
# then my program works. If not, then there's a bug in the program.

