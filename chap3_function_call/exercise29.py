from utils import get_data_statistics,get_random_score

def cal_mean(data):
    mean = sum(data) /len(data)
    return mean

def cal_var(data):
    mean = cal_mean(data)

    squared_diffs = [(sample-mean)**2 for sample in data]
    var = sum(squared_diffs) / len(data)
    return var


def cal_std(data):
    var =cal_var(data)
    std = var**0.5
    return std


n_students = 100
scores =get_random_score(n_students)
score_std =cal_std(scores)
print(f"{score_std = :.2f}")


