words = input("Enter sentence: ").split()
new_word = ' '.join(words[::-1]) # Reversing the list using slicing
print(new_word)
