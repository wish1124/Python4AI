from exercise61 import cal_max_min

def sort(data,descending =True):
    data_ = data.copy()
    data_sort = []

    n_data = len(data)

    for _ in range(n_data):
        target_value,target_idx = cal_max_min(data_,max=descending)
        data_sort.append(target_value)
        data_.pop(target_idx)

    return data_sort

if __name__ == '__main__':
    from exercise59 import get_random_scores

    scores = get_random_scores()


    scores_sort_descending = sort(scores)
    scores_sort_ascending = sort(scores,descending=False)
    print(f"{scores_sort_descending = }")
    print(f"{scores_sort_ascending = }")