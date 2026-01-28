def cal_max_min(data):
    max_value,min_value =None,None

    for sample_idx,sample in enumerate(data):
        if max_value == None or sample >  max_value:
            max_value = sample
        if min_value == None or sample < min_value:
            min_value = sample
    return max_value,min_value

from exercise44 import get_randiant_data

n_students,min_val,max_val = 10,0,10

scores = get_randiant_data(n_data = n_students,min_val=min_val,max_val=max_val,random_seed=0)

print(f"{scores = }")

scores_mean,scores_std = cal_max_min(scores)
print(f"{scores_mean = } / {scores_std = }")