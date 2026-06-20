if __name__ == '__main__':
    students = []
    
    # 1. Collect all inputs into a nested list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # 2. Get a sorted set of unique scores to find the second lowest
    unique_scores = sorted(list(set(student[1] for student in students)))
    second_lowest_score = unique_scores[1]
    
    # 3. Filter students who have the second lowest score and sort their names
    runner_ups = [student[0] for student in students if student[1] == second_lowest_score]
    runner_ups.sort()
    
    # 4. Print each name on a new line
    for name in runner_ups:
        print(name)