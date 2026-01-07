from exercise36 import get_random_scores
from exercise37 import cal_mean,cal_std,cal_var

n_students = 100
scores = get_random_scores(n_students)

score_info = {
    'mean' : cal_mean(scores),'var' : cal_var(scores),'std' : cal_std(scores)
}
print(score_info)