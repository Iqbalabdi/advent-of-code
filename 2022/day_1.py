file = open("input.txt", "r")
count = 0
arr = []
for line in file:
    if line != "\n":
        count += int(line.rstrip())
    else:
        arr.append(count)
        count = 0

### Part 1
print(max(arr))

### Part 2
arr.sort(reverse=True)
print(arr[0]+arr[1]+arr[2])