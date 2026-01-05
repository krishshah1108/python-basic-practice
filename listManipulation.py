total_nums = int(input("Enter total numbers in the list: "))
man_list = []
for i in range(total_nums):
    inp = int(input(f"Enter number {i+1}: "))
    man_list.append(inp)
print(man_list)
unique = list(set(man_list))
print(f"Unique list: {unique}")