from utils import get_random_score,cal_mean

n_students = 100
scores = get_random_score(n_students)

scores_mean = cal_mean(scores)
print(f"mean before ms: {scores_mean:.2f}")

for score_idx in range(len(scores)):
    scores[score_idx] -= scores_mean

scores_mean = cal_mean(scores)
print(f"mean after ms: {scores_mean:.2f}")