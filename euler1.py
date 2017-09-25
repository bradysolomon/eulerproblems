number = 1
final = 0
while number < 1000:
    if number % 5 == 0 or number % 3 == 0:
        final += number
        number += 1
    else:
        number += 1
print final
