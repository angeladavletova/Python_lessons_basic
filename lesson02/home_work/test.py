a = [0, 1, 2, 3, 4, 10, 10]
b = set([0, 1, 4, 10, 10])
k = 0



for i in range(len(b)):
    if a[i - k] in b:
        del a[i - k]
        k += 1

print(a, b)
a = list(input())
print(a, type(a))