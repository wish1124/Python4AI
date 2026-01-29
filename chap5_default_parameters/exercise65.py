def avg_pool(data,pool_size=2,stride=None):
    if stride is None:
        stride = pool_size
    n_data = len(data)
    n_windows = int((n_data - pool_size) / stride) + 1

    pooled_data = []
    for window_idx in range(n_windows):
        start_idx = window_idx * stride
        window = data[start_idx:start_idx+pool_size]

        window_avg = sum(window) /pool_size
        pooled_data.append(window_avg)
    return pooled_data

if __name__ == '__main__':
    from exercise59 import get_random_scores
    from exercise64 import pad

    data = get_random_scores(n_students=10,min_val=0,max_val=10)
    data = pad(data,pad_size=2)

    print(f"{avg_pool(data) = }")
    print(f"{avg_pool(data, pool_size=3)}")
    print(f"{avg_pool(data,pool_size=3,stride=2)}")