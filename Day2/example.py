L = [1,2,3,4,5]
sum = 0
for i in L:
    sum = sum + i
print("Current sum:", sum)

product = 1
for i in L:
    product = product * i
print("Current product:", product)

# Time Complexity : O(n) where n is the number of elements in the list L.


L = [1,2,3,4,5]
for i in L:
    for j in L:
        print('({}, {}'.format(i,j))