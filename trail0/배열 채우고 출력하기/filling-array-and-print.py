new_list = map(str, input().split())
reverse_list = ''
for x in new_list:
    reverse_list = x + str(reverse_list)
print(reverse_list)