from utils import get_random_score,cal_std,cal_mean

n_students = 100
scores = get_random_score(n_students)

score_mean , score_std = cal_mean(scores),cal_std(scores)
print(f"before stdz: {score_mean = :.2f} / {score_std = :.2f}")

for score_idx, score in enumerate(scores):
    scores[score_idx] = (score-score_mean) /score_std

score_mean,score_std = cal_mean(scores) ,cal_std(scores)
print(f"after stdz: {score_mean = :.2f} / {score_std = :.2f}")