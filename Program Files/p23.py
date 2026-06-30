import textwrap

def wrap(string, max_width):
    # This automatically splits the text and returns a string separated by \n
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)