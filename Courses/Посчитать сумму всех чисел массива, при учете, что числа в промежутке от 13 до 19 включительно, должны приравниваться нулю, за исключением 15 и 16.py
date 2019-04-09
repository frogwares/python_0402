L = [12, 13, 15, 16, 19, 20, 14, 10]

for i in L:
    if i>=13 and i<=19 and i!=15 and i!=16:
        L.remove(i)
print(sum(L))