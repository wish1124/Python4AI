from exercise45 import pad

def avg_pool(data,window_size,stride,pad_size,pad_value):
    data = pad(data,pad_size=pad_size,pad_value=pad_value)

    n_data = len(data)
    n_windows = int((n_data - window_size) / stride) + 1

    pooled_data = []
    for window_idx in range(n_windows):
        strat_idx = window_idx * stride
        window = data[strat_idx:strat_idx+window_size]

        window_avg = sum(window) / window_size
        pooled_data.append(window_avg)
    return pooled_data

def max_pool(data,window_size,stride,pad_size,pad_value):
    data = pad(data,pad_size=pad_size,pad_value=pad_value)

    n_data = len(data)
    n_windows = int((n_data-window_size) / stride) +1

    pooled_data = []
    for window_idx in range(n_windows):
        strat_idx = window_idx * stride
        window = data[strat_idx:strat_idx+window_size]

        pooled_data.append(max(window))
    return pooled_data