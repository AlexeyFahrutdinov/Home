my_list = [1, 2, 3]

print(len(my_list))

print(my_list[0])

print(my_list[0:])

another_list = ["Four", "Five", "Six"]

print(my_list + another_list)

new_list = my_list + another_list

new_list[0] = 11

print(new_list)

new_list.append(333)
print(new_list)

a = new_list.pop()
print(a)
print(new_list)

b = new_list.pop(2)
print(b)
print(new_list)

new_list = ["f", "d", "e"]
num_list = [4, 3, 2, 5]

new_list.sort()
num_list.sort()
sort_list = new_list.sort()
print(sort_list)
sort_list = new_list
print(sort_list)


print(new_list)
print(num_list)

new_list.reverse()
print(new_list)
# Новый текст
