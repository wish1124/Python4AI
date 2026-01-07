from utils import get_random_score,cal_max,cal_min

n_students = 100
scores =get_random_score(n_students)

score_max,score_min = cal_max(scores),cal_min(scores)
print(f"before min-max norm {score_max :.2f} / {score_min = :.2f}" )

for score_idx,score in enumerate(scores):
    scores[score_idx] = (score - score_min) / (score_max -score_min)

scores_max,scores_min = cal_max(scores),cal_min(scores)
print(f"after min-max norm: max {scores_max:.2f} / min {scores_min:.2f}")