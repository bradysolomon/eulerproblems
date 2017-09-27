#The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

#Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

#create variable to store added series
added = 0
#create variable to run through while loop
num = 1
while num <= 1000:
    #num is multiplied by itself and added to added
    added = added + num ** num
    #1 is added to num so it will cycle through every number until 1000
    num += 1
#added variable is turned into a string so its length can be found
added = str(added)
#create a new variable to store the length of added
length = len(added)
#prints the last 10 digits of added
print added[length-10:length]
