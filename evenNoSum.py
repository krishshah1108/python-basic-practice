def evenNoSum(arr):
    total = 0
    for x in arr:
        if x%2 == 0:
            total = total+x
    return total
        
arr = [10,1,2,13,4,4]
print(evenNoSum(arr))