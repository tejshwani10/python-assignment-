def count_substring(string, sub_string):
    count = 0
    # Loop through the string up to the point where the substring can fit
    for i in range(0, len(string) - len(sub_string) + 1):
        # Slice the string to the length of the substring and check for equality
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)