from utils import get_random_score,cal_max


def cal_max_idx(data):
    max_score,max_score_idx = None,None
    for sample_idx, sample in enumerate(data):
        if max_score == None or sample > max_score:
            max_score = sample
            max_score_idx = sample_idx
    return max_score_idx


def sort(data):
    data_ = data.copy()
    data_sort = []
    for _ in range(n_students):
        max_score = cal_max(data_)
        max_score_idx = cal_max_idx(data_)

        data_sort.append(max_score)
        data_.pop(max_score_idx)
    return data_sort

n_students =10
scores =get_random_score(n_students)
scores_sort = sort(scores)
print(f"{scores = }")
print(f"{scores_sort = }")