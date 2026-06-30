# Number of students subscribed to the English newspaper
n_english = int(input())

# Roll numbers of students subscribed to the English newspaper
english_students = set(map(int, input().split()))

# Number of students subscribed to the French newspaper
n_french = int(input())

# Roll numbers of students subscribed to the French newspaper
french_students = set(map(int, input().split()))

# Find English subscribers who are not in the French subscriber list
only_english = english_students.difference(french_students)

# Output the total count
print(len(only_english))