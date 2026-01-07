from exercise36 import get_random_scores
def cal_mean(data):
    mean = sum(data) / len(data)
    return mean


def cal_var(data):
    n_data = len(data)
    mean = sum(data) / n_data

    squared_diffs = [(sample-mean)**2 for sample in data]
    var = sum(squared_diffs) / n_data
    return var


def cal_std(data):
    n_data = len(data)
    mean = sum(data) / n_data

    squared_diffs = [(sample-mean)**2 for sample in data]
    var = sum(squared_diffs) / n_data
    std = var**0.5
    return std

if __name__ == '__main__':

    n_students = 10
    scores = get_random_scores(n_students)

    score_mean =  cal_mean(scores)
    score_var = cal_var(scores)
    score_std = cal_std(scores)

    print(f"{cal_mean(scores) = }")
    print(f"{cal_var(scores) = }")
    print(f"{cal_std(scores) = }")
