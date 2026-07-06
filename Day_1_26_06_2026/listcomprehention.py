
#example of traditional approach#
pairs=[]
for i in range(3):
    for j in range(4):
        pairs.append((i,j))
print(pairs)


#list comprehention of above code#
pairs=[(i,j)for i in range(3)for j in range(4)]
print(pairs)

#example 2 : traditional approach #

pairs=[]
for i in range(1,6):
    if i % 2 == 0:
        for j in range(1,6):
            if j % 2 !=0:
                pairs.append((i,j))
print(pairs)

#list comprehension of above code#

result = [(i, j) for i in range(1, 6) if i % 2 == 0 for j in range(1, 6) if j % 2 != 0 ]
print(result)