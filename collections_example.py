from collections import Counter
c = Counter([1, 1,3,3,2,2, 2, 3, 3, 3, 4, 4, 4, 4])
print(c) # Counter({3: 5, 4: 4, 2: 3, 1: 2})
print(c.values()) # dict_values([2, 5, 3, 4])
print(sum(c.values())) # 14
print(c.items()) # dict_items([(1, 2), (3, 5), (2, 3), (4, 4)])

for element, ctr in c.items():
    print(element,ctr)
#1 2
#3 5
#2 3
#4 4