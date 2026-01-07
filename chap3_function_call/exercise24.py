from utils import (get_random_score,cal_mean,cal_var,cal_std,cal_max,cal_min)

n_students =10
scores = get_random_score(n_students)

scores_mean =cal_mean(scores)
score_var = cal_var(scores)

print(f"{scores = }")
print(f"{scores_mean = } / {score_var =}")

score_info = {
    "mean" : cal_mean(scores),  "var" : cal_var(scores) ,"std":cal_std(scores),
    "min" : cal_min(scores),"max" : cal_max(scores)}

print(score_info)