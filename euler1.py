#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


#number is used below to check each number 1-1000 to see if it is a multiple of 3 or 5.
number = 1
#final is where all multiples of 3 or 5 that pass through are added together.
final = 0
#this while loop will cycle through every integer 1-1000, checking to see which ones are multiples of 3 or 5
while number < 1000:
#this if statement check to se if the number divided by 3 or 5 leaves a remainder of 0..
    if number % 5 == 0 or number % 3 == 0:
#if the number works, it is added to final.
        final += number
#number is increased by one no matter what
        number += 1
    else:
        number += 1
#final is printed.
print final
