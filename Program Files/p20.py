from collections import defaultdict

# Read dimensions n and m
n, m = map(int, input().split())

# Create a defaultdict with lists as default values
group_a = defaultdict(list)

# Read Group A words and record their 1-indexed positions
for i in range(1, n + 1):
    word = input()
    group_a[word].append(i)

# Read and process Group B words
for _ in range(m):
    word = input()
    if word in group_a:
        # Unpack the list of integers into space-separated string output
        print(*group_a[word])
    else:
        # Word does not appear in Group A
        print(-1)