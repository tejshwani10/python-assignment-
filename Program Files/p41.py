# Read number of students (N) and subjects (X)
N, X = map(int, input().split())

# Gather all subject score rows
scores = [list(map(float, input().split())) for _ in range(X)]

# Zip columns together to get student clusters and print averages
for student_scores in zip(*scores):
    print(round(sum(student_scores) / X, 2))