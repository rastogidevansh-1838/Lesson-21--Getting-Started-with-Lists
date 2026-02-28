L = [3, 5, 6, 4, 12, 8, 9, 1, 18, 7]
print("Original List:", L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("sum = ", count)
print("average = ", avg)
L.sort
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])