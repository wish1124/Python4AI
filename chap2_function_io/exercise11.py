import random

def print_score_max_min(scores):
    max_score,min_score = None,None
    for score in scores:
        if max_score == None or score> max_score:
            max_score = score
        if min_score == None or score < min_score:
            min_score = score

    print(f"max_score / min_score : {max_score} / {min_score}")

n_student =5
scores = [random.randint(1,4) for _ in range(n_student)]
print_score_max_min((scores))

