import random

def get_random_score(n_students):
    scores = [random.randint(0,100)
              for _ in range(n_students)]

    return scores


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


def cal_max(data):
    max_score = None
    for sample in data:
        if max_score == None or sample > max_score:
            max_score=sample
    return max_score


def cal_min(data):
    min_score = None
    for sample in data:
        if min_score == None or sample < min_score:
            min_score = sample
    return min_score


def get_data_statistics(data):
    stat_dict = {
        "mean": cal_mean(data), "var": cal_var(data), "std": cal_std(data),
        "min": cal_min(data), "max": cal_max(data)}

    return stat_dict


def standardization(data):
    data_ = data.copy()
    mean, std = cal_mean(data_), cal_std(data_)
    for sample_idx, sample in enumerate(data_):
        data_[sample_idx] = (sample - mean) / std
    return data_


def min_max_norm(data):
    data_ = data.copy()

    data_max,data_min = cal_max(data_),cal_min(data_)
    for sample_idx,sample in enumerate(data_):
        data_[sample_idx] = (sample - data_min) / (data_max - data_min)
    return data_