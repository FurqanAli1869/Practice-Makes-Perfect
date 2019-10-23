List = [1, 2.5, "'Furqan'", [5, 8]]
answer = 'Yes'
while answer == 'Yes':
    i = int(input(f'The list contains {len(List)} elements in total. '
                  f'What\'s the index of element you want to know the type of?  '))
    if type(List[i]) == int:
        print(f'The {i} element of the list is the integer {List[i]}\n')
        answer = input('Wanna continue? (Type "Yes" or "No") ')
        continue
    if type(List[i]) == float:
        print(f'The {i} element of the list is the float number {List[i]}\n')
        answer = input('Wanna continue? (Type "Yes" or "No") ')
        continue
    if type(List[i]) == list:
        print(f'The {i} element of the list is the list {List[i]}\n')
        answer = input('Wanna continue? (Type "Yes" or "No") ')
        continue
    if type(List[i]) == str:
        print(f'The {i} element of the list is the string {List[i]}\n')
        answer = input('Wanna continue? (Type "Yes" or "No") ')
        continue
print('Thanks for using our App. We hope to see you again!')






