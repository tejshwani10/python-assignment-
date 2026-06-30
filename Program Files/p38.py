# Read input quantities and lists of roll numbers
n_english = int(input())
english_subs = set(map(int, input().split()))

n_french = int(input())
french_subs = set(map(int, input().split()))

# Calculate the symmetric difference (students subscribed to only one paper)
only_one_paper = english_subs.symmetric_difference(french_subs)

# Output the total count
print(len(only_one_paper))