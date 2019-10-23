number = int(input('''Please enter the number you would like to test!
The number is: '''))
divider = 2
while divider < number:
    if number % divider == 0:  # That is, if the given num. is dividable by anything else other that 1 (excluded through
                               # the initialising of i at 2) and itself (excluded through <, and NOT <=)
        print(f'{number} is not a prime number.\n')
        print(f'The smallest divider of this number is {divider}.\n')
        break
    divider = divider + 1
else:  # This else block is executed as soon as the condition divider < number gets violated and before the if condition
       # is met, that is, after the iterations are complete without meeting the if condition.
    print(f'No other dividers are found for the given number. Therefore, {number} is a prime number.\n')
print('Thanks for using our service. See you next time!')