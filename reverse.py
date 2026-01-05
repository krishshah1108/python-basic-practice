num = int(input("Enter a number: "))

orgNum = num
revNum = 0
while(num>0):
    lastDigit = num % 10
    revNum = revNum*10 + lastDigit
    num = num // 10
print(revNum)

