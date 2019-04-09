#my_list = [1, 5, 32, 1, 55, 55]
#my_list_new = []
#for element in my_list:
  #  if element not in my_list_new:
    #    my_list_new.append(element)
#print("Count of unique elements: ", len(my_list_new))
#Collapse



a = [2, 5, 4, 2, 4, 6, 2, 2, 2, 5, 8]
b = list(set(a))
res = len(b)
print(res)