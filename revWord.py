word = input("Enter word: ").replace(" ", "").lower()  # Remove spaces and convert to lowercase
revword = word[::-1]  # Reverse the word without spaces
if word == revword:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")