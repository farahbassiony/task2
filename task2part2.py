a = []
n = int(input("Number of elements in array:"))
print("Enter the numbers")
for i in range(n):
   l = int(input())
   a.append(l)
for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if a[j] < a[min]:
            min = j
    if min != i:
        a[i], a[min] = a[min], a[i]
print(a)