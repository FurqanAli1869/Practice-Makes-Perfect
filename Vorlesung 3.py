

# Funktion, die den größeren zweier Werte zurückibt
def maximum(first_value, second_value):

    first_value = int(input('first value  '))
    second_value = int(input('second value  '))
    if first_value > second_value:
        print(f'Der größere Wert ist {first_value}')
    elif second_value > first_value:
        print(f'Der größere Wert ist {second_value}')
    else:
        print('Beide Werte sind gleich')
#  Funktion, die das größte Element einer Liste zurückibt
def maximum_2(liste=[5, 3, 8, 1]):

    if liste[0] > liste[1] and liste[0] > liste[2] and liste[0] > liste[3]:
        print(f'{liste[0]} ist das größte Element')
    elif liste[1] > liste[0] > liste[2] and liste[0] > liste[3]:
        print(f'{liste[1]} ist das größte Element')
    elif liste[2] > liste[0] and liste[2] > liste[1] and liste[2] > liste[3]:
        print(f'{liste[2]} ist das größte Element')
    elif liste[3] > liste[0] and liste[3] > liste[1] and liste[3] > liste[2]:
        print(f'{liste[3]} ist das größte Element')
maximum_2(liste=[1, 2, 44, 43])


def maximum_3(liste=[5, 3, 8, 1]):
    look = []
    for ind, elem in enumerate(liste):
        look.append(tuple([ind, elem]))
    print(look)

maximum_3()
