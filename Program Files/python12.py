if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        # Split the input line into command and arguments
        parts = input().split()
        command = parts[0]
        
        if command == "print":
            print(my_list)
        else:
            # Convert any remaining arguments from strings to integers
            arguments = map(int, parts[1:])
            
            # Dynamically call the list method (e.g., my_list.append, my_list.sort)
            getattr(my_list, command)(*arguments)