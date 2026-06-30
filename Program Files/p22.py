# The lambda function to cube a number
cube = lambda x: x ** 3

def fibonacci(n):
    # Return a list of the first n fibonacci numbers
    if n <= 0:
        return []
    elif n == 1:
        return [0]
        
    # Start with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the rest of the sequence iteratively
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
        
    return fib_sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))