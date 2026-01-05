# Online Python - IDE, Editor, Compiler, Interpreter
no_of_elements = int(input("Enter total no of elements: "))
elem_arr = []
for i in range(no_of_elements):
    inp_element = int(input(f"Enter element no: {i+1} "))
    elem_arr.append(inp_element)

target = int(input("Enter target element: "))
ele_found = False
for index, ele in enumerate(elem_arr):
    if ele == target:
        ele_found = True
        print(f"Found target {target} at index {index}")
        break
if not ele_found:
    print(f"Target {target} is not found")

