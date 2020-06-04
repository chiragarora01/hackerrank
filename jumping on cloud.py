n, arr = int(input()), list(input())
i= count = 0

while i < n - 2:
    if (arr[i + 1] == "0" or arr[i + 1] == "1") and arr[i + 2] == "0":
        count = count + 1
        i = i + 2
    else:
        count = count + 1
        i = i + 1
else:
    count = count + 1

print(count)
