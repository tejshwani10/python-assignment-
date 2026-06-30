# Read the total number of test cases
t = int(input())

for _ in range(t):
    try:
        # Read a string line and unpack into variables a and b
        a, b = input().split()
        
        # Perform integer division using the // operator
        print(int(a) // int(b))
        
    except ZeroDivisionError as e:
        # Catch and print division by zero errors
        print("Error Code:", e)
        
    except ValueError as e:
        # Catch and print invalid type conversion errors
        print("Error Code:", e)