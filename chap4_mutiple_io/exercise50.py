from exercise49 import cal_max_min

def sort(data,descending):
    data_ = data.copy()
    data_sort = []

    n_data = len(data)
    for _ in range(n_data):
        if descending:
            target = cal_max_min(data_,max_min='max')
        else:
            target = cal_max_min(data_,max_min='min')

        data_sort.append(target['value'])
        data_.pop(target['idx'])
    return data_sort

from exercise44 import get_randiant_data

n_students =10
scores = get_randiant_data(n_students,min_val=0,max_val=100,random_seed=0)
scores_sort_descending = sort(scores,descending=True)
scores_sort_ascending = sort(scores,descending=False)
print(f"{scores = }")
print(f"{scores_sort_descending = }")
print(f"{scores_sort_ascending = }")