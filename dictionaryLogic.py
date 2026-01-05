data = {
    "apple": 20,
    "banana": 5,
    "orange": 8,
    "mango": 15
}

# Initialize min_fruit and max_fruit with the first key-value pair
first_key, first_value = next(iter(data.items()))
min_fruit = max_fruit = {first_key: first_value}

# Loop through the dictionary to find the min and max fruits
for key, value in data.items():
    if value < list(min_fruit.values())[0]:
        min_fruit = {key: value}
    if value > list(max_fruit.values())[0]:
        max_fruit = {key: value}

# Unpack the minimum fruit
min_fruit_key, min_fruit_value = min_fruit.popitem()

# Unpack the maximum fruit
max_fruit_key, max_fruit_value = max_fruit.popitem()

# Print the results
print(f"The fruit with minimum value is {min_fruit_key} with value {min_fruit_value}")
print(f"The fruit with maximum value is {max_fruit_key} with value {max_fruit_value}")
