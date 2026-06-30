def mutate_string(string, position, character):
    # Slice before the position, add the character, and append the rest
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    p, c = input().split()
    s_new = mutate_string(s, int(p), c)
    print(s_new)