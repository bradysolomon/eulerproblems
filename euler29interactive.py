print " "
print "Consider all integer combinations of ab for 2 <= a <= 5 and 2 <= b <= 5:"
print " "
print "2**2=4, 2**3=8, 2**4=16, 2**5=32"
print "3**2=9, 3**3=27, 3**4=81, 3**5=243"
print "4**2=16, 4**3=64, 44=256, 45=1024"
print "5**2=25, 5**3=125, 5**4=625, 5**5=3125"
print "If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:"
print " "
print "4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125"
print " "
print "Enter a range of positive integers and find how many distinct terms are generated using the above method."
print "Note: the range given by Euler Problem 29 is 2-200."
print " "

low = raw_input("What is the lower value of the range you want?")
high = raw_input("What is the upper value of the range you want?")

if int(low) < 0 or int(high) < 0:
    print "Please use only positive integers."
elif low > high:
    print "The lower limit should not be higher than the upper limit."
else:
    #create a, a list of integers 2-100
    a = list(range(int(low),int(high)+1))
    #create an empty list to add numbers that fill conditions to
    sequence = []
    #cycle through every number in a for every number of a
    for x in a:
        for y in a:
            #add the result of the first number to the power of the second number to the 'sequence' list
            sequence.append(x**y)
    #change the list into a set to remove duplicate results, then change it back to a list.
    sequence = list(set(sequence))
    #print the length of the 'sequence' list
    print len(sequence)
