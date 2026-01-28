from exercise64 import pad

def avg_pool(data,pad_size=None,pad_value=0,pool_size=2,stride=None):
    if pad_size is not None:
        data = pad(data,pad_size=pad_size,pad_value=pad_value)
    if stride is None:
        stride = pool_size

    n_data = len(data)
    n_window = int((n_data - pool_size) / stride ) +1

    pooled_data = []
    for window_idx in range(n_window):
        start_idx = window_idx * stride
        window = data[start_idx: start_idx + pool_size]

        window_avg = sum(window) /pool_size
        pooled_data.append(window_avg)
    return pooled_data


if __name__ == '__main__':
    from exercise59 import get_random_scores

    data = get_random_scores(n_students=10,min_val=0,max_val=10)

    print(f"data : {data}")
    print(f"{avg_pool(data) = }")
    print(f"{avg_pool(data,pad_size=2) = }")
    print(f"{avg_pool(data,pad_size=2,pool_size=3)}")