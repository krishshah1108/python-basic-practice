def sumOfDigits(n):
    if(n<=0):
        return 0
    lastDigit = n % 10
    n = n // 10
    return lastDigit + sumOfDigits(n)

print(sumOfDigits(626))