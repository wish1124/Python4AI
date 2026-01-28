def unique(data):
    unique_dict = {}
    for sample in data:
        unique_dict[sample] = unique_dict.get(sample,0) + 1
    return list(unique_dict.keys()) , list(unique_dict.values())

from exercise44 import get_randiant_data

n_students , min_val, max_val = 100,0,10
scores = get_randiant_data(n_data=n_students,min_val=min_val,max_val=max_val,random_seed= 0)
print(f"{scores = }")

unique_value,unique_cnt = unique(scores)
print(f"{unique_value = }")
print(f"{unique_cnt = }")