num = int(input("Enter a number: "))

def isSpecial(num):
    if num % 3 == 0:
        return True
    endsWith = num % 10
    if(endsWith == 5):
        return True
    return False
    
print(isSpecial(num))