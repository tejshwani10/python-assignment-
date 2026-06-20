if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # 1. Convert the map object into a Python set to remove duplicate scores
    unique_scores = set(arr)
    
    # 2. Remove the maximum score from the set
    unique_scores.remove(max(unique_scores))
    
    # 3. The new maximum of the remaining scores is the runner-up score
    print(max(unique_scores))