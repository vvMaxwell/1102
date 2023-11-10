with open("three_digit_numbers.txt") as fileDescriptor:
        sample = fileDescriptor.read()
cols = sample.split()
numList = []
for col in cols:
    num = int(col)
    numList.append(num)
start = min(numList)
for count in range(start, max(numList)):
    print(count)
    if count not in numList:
        print(f"{count} is missing")
with open("sorted_numbers.txt", "w") as fileDescriptor:
    for count in range(start, max(numList)):
        print(count)
        if count not in numList:
            fileDescriptor.write(f"{count} is missing ")