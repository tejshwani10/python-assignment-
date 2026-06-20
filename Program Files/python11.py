if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # 1. Fetch the list of scores for the queried student name
    query_scores = student_marks[query_name]
    
    # 2. Calculate the average score
    average_score = sum(query_scores) / len(query_scores)
    
    # 3. Print the average formatted strictly to 2 decimal places
    print(f"{average_score:.2f}")