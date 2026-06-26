# traditional dictionary approach #
t={}
for i in range(1,6):
    for j in range(1,6):
        t[(i,j)] = i * j
print(t)
