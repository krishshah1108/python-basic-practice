# Convert lists to sets
set_a = set(a)
set_b = set(b)

# 1. Common elements (Intersection)
common_elements = set_a & set_b

# 2. Elements only in a (Difference)
only_in_a = set_a - set_b

# 3. Elements only in b (Difference)
only_in_b = set_b - set_a

# Convert sets back to lists
common_elements = list(common_elements)
only_in_a = list(only_in_a)
only_in_b = list(only_in_b)

# Print results
print("Common elements:", common_elements)
print("Elements only in a:", only_in_a)
print("Elements only in b:", only_in_b)
