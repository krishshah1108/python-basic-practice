try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    ans = n1 / n2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
else:
    print(f"The result of {n1} divided by {n2} is: {ans}")
finally:
    print("Execution complete.")
