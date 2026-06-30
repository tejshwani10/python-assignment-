# Read English newspaper subscribers
n = int(input())
english_subscribers = set(map(int, input().split()))

# Read French newspaper subscribers
m = int(input())
french_subscribers = set(map(int, input().split()))

# Find and print the number of students who subscribed to both
print(len(english_subscribers.intersection(french_subscribers)))