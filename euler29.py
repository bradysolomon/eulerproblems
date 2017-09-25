a = list(range(2,101))
sequence = []
for x in a:
    for y in a:
        sequence.append(x**y)
sequence = list(set(sequence))
print len(sequence)
#print sequence
