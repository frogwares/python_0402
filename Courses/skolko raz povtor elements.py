number_array_1 = [1, 9, 2, 1, 2, 7, 5, 11, 4, 8, 10]
temp_list = []
for b in number_array_1:
    count_m = 0
    if b in number_array_1:
        for i in number_array_1:
            if i == b:
                count_m += 1
        if count_m > 1 and b not in temp_list:
            print('%d count in array - %d times' % (b, count_m))
        temp_list.append(b)