def split_and_join(line):
    #  Split the string into a list of words using a space delimiter
    words = line.split(" ")
    
    #  Join the list of words back together using a hyphen
    result = "-".join(words)
    
    #  Return the modified string
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)