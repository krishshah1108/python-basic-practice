# Online Python - IDE, Editor, Compiler, Interpreter
no_of_elements = int(input("Enter total no of elements: "))
elem_arr = []
for i in range(no_of_elements):
    inp_element = int(input(f"Enter element no: {i+1} "))
    elem_arr.append(inp_element)

def findSecondMax(elemArr):
    max_ele = elemArr[0]
    second_max_ele = elemArr[1]
    if max_ele < second_max_ele:
        max_ele, second_max_ele = second_max_ele, max_ele
    for ele in elemArr:
        if ele > max_ele:
            second_max_ele = max_ele
            max_ele = ele
        elif ele > second_max_ele and ele != max_ele:
            second_max_ele = ele
        
    return second_max_ele
secondLargestElement = findSecondMax(elem_arr)
print(f"Second larget element in the list is {secondLargestElement}")

