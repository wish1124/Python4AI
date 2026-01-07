from utils import get_random_score
from utils import cal_mean,cal_var,cal_std
from utils import cal_max,cal_min


def get_data_statistics(data):
    stat_dict = {
        "mean": cal_mean(data), "var": cal_var(data), "std": cal_std(data),
        "min": cal_min(data), "max": cal_max(data)}

    return stat_dict

n_students = 100
scores =get_random_score(n_students)

scores_stats =get_data_statistics(scores)
print(f"{scores_stats = }")