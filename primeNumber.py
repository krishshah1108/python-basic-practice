num = int(input("Enter a number: "))
divisibleBy = 0
for i in range(2,num):
    if(num%i == 0):
        divisibleBy+= 1
if(divisibleBy == 0):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

