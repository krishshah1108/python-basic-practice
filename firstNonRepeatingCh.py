word = input("Enter word: ")

frq_count = {}
for ch in word:
    if ch not in frq_count:
        frq_count[ch] = 1
    else:
        frq_count[ch] = (frq_count[ch]+1)
print(frq_count)
for char in word:
    if frq_count[char] == 1:
        print("First non-repeating character:", char)
        break

