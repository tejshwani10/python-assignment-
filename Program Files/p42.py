# Function to generate the first n Fibonacci numbers starting with 0
def fibonacci(n):
    # Handle base edge cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize list with first two terms
    fib_list = [0, 1]
    
    # Continuously append the sum of the last two elements
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
        
    return fib_list

# Lambda function to cube a given value
cube = lambda x: x ** 3

# Main Execution block (matches the HackerRank challenge structure)
if __name__ == '__main__':
    n = int(input("Enter the number of Fibonacci elements: "))
    
    # Map the lambda function over the generated sequence
    cubed_fibonacci = list(map(cube, fibonacci(n)))
    
    # Print the final transformed list
    print(cubed_fibonacci)