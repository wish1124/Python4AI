from utils import get_random_score,get_data_statistics,cal_max,cal_min,min_max_norm

n_students = 10
scores = get_random_score(n_students)
print(get_data_statistics(scores))


scoures_mm = min_max_norm(scores)
print(get_data_statistics(scoures_mm))