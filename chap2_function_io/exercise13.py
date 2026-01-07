import random

def cal_mean(data):
    mean = sum(data) / len(data)
    return mean

n_score = 5
scores = [random.randint(1,100) for _ in range(5)]

scores_mean = cal_mean(scores)
print(f"{scores = } ")
print(f"{scores_mean = }")