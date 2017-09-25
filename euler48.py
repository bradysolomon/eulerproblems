added = 0
num = 1
while num <= 1000:
    added = added + num ** num
    num += 1
added = str(added)
length = len(added)
print added[length-10:length]
