import random

def get_random_scores(n_students):
    scores = [random.randint(0,100) for _ in range(n_students)]
    return scores

def cal_score_max(scores):
    max_score = None
    for i in scores:
        if max_score == None or i > max_score:
            max_score = i
    return max_score

def cal_score_min(scores):
    min_score = None
    for i in scores:
        if min_score == None or i < min_score:
            min_score = i
    return min_score


n_people =10
scores = get_random_scores(n_people)
print(scores)
print(cal_score_max(scores))
print(cal_score_min(scores))