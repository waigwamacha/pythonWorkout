some_list = []

while True:
    item = input("Enter whatever comes to mind (a number, a word): ")
    some_list.append(item)
    if item == 'q':
        break

print(some_list)
print(len(some_list))

for i in some_list:
    print(i)
    print(type(i))
