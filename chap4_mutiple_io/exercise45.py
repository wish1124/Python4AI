def pad(data,pad_size,pad_value):
    data = [pad_value] * pad_size +  data + [pad_value] * pad_size
    return data

if __name__ == "__main__":
    from exercise44 import get_randiant_data

    n_data, min_val, max_val = 10, 10, 100
    data = get_randiant_data(n_data=n_data, min_val=min_val, max_val=max_val, random_seed=2)
    print(f"original data: {data}")



    pad_size, pad_value = 2,0
    data = pad(data,pad_size=pad_size,pad_value=pad_value)
    print(f"padded data: {data}")