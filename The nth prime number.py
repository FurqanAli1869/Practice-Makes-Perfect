# Finding the 123rd prime number:
# THOUGHT: We know that number IS a prime, so we know that the else block above is the one being executed. We also
# know that the if condition is violated 123 times in a row starting from the number 2 (i.e. the first prime). We
# just don't know the number at which the if condition is violated for the 123rd time.
List = []
order = 0
number = 1
divider = 2
wanted_prime = int(input('Which prime would you like to know? '))
while order < wanted_prime:
    number += 1
    divider = 2
    while divider < number:
        if number % divider == 0:
            break
        divider += 1
        pass
    else:  # If prime
        order += 1
        while order <= 100:
            List.append(number)
            break
        continue
else:
    order_as_string = str(wanted_prime)
    if order_as_string[-1] == '1' and order_as_string[-2] != '1':
        print(f'The {wanted_prime}st prime number is {number}')
    elif order_as_string[-1] == '2' and order_as_string[-2] != '1':
        print(f'The {wanted_prime}nd prime number is {number}')
    elif order_as_string[-1] == '3' and order_as_string[-2] != '1':
        print(f'The {wanted_prime}rd prime number is {number}')
    else:
        print(f'The {wanted_prime}th prime number is {number}')
print(f'The first 100 primes are {List}')
#   List of differences
dude = []
i = 0
List_2 = List[1:]
while i <= 98:
    diff = List_2[i] - List[i]
    dude.append(diff)
    i += 1

print(f'The list of the differences is {dude}')

#   Alternative Solution
# for i in range(len(List) - 1):
#     dude.append(List[i+1] - List[i])
# print(dude)
#
# print(len(dude))

