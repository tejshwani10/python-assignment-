if __name__ == '__main__':
    s = input()
    
    # Check alphanumeric characters
    print(any(char.isalnum() for char in s))
    
    # Check alphabetical characters
    print(any(char.isalpha() for char in s))
    
    # Check any digits
    print(any(char.isdigit() for char in s))
    
    # Check  lowercase characters
    print(any(char.islower() for char in s))
    
    # Check uppercase characters
    print(any(char.isupper() for char in s))