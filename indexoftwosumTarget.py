arr = list(map(int,input("Enter numbers ").split()))
target = int(input("Enter target "))
ans = []
for idx,ele in enumerate(arr):
    for j in range(idx+1,len(arr)):
        value = ele + arr[j]
        if(value == target):
            ans = [idx,j]
            break
    if ans:
        break
print(ans)

            