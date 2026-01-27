def avg_pool(data,window_size,stride):
    n_data =len(data)
    n_windows = int((n_data-window_size)/stride+1)

    pooled_data = []
    for window_idx in range(n_windows):
        start_idx = window_idx * stride
        window = data[start_idx:start_idx + window_size]

        window_avg = sum(window) /window_size
        pooled_data.append(window_avg)
    return pooled_data

from exercise44 import get_randiant_data
from exercise45 import pad

n_data,min_val,max_val =10,0,10
pad_size , pad_value =2,0
data =get_randiant_data(n_data = n_data, min_val=min_val,max_val=max_val,random_seed=2)
data =pad(data,pad_size=pad_size,pad_value=pad_value)
print(data)

window_size,stride =2,2
pooled_data = avg_pool(data,window_size=window_size,stride=stride)
