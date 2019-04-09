list_5 = [1, 5, 5, 32, 1]
print(list_5)
list_5_sorted = sorted(list_5)
for element in range(len(list_5)-1):
    if list_5_sorted[element] == list_5_sorted[element + 1]:
        print("Duplicates detected ", list_5_sorted[element])