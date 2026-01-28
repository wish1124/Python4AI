from chap2_function_io.exercise20 import n_data
from exercise44 import get_randiant_data

def cal_mean(data):
    n_data = len(data)

    mean = sum(data) / n_data
    var =  sum([(sample - mean)**2 for sample in data]) /n_data
    std = var**0.5

    return mean,std

from exercise44 import get_randiant_data

n_students,min_val,max_val = 10,0,10

scores = get_randiant_data(n_data = n_students,min_val=min_val,max_val=max_val,random_seed=0)

print(f"{scores = }")

scores_mean,scores_std = cal_mean(scores)
print(f"{scores_mean = } / {scores_std = }")