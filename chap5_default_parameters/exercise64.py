def pad(data,pad_size,pad_value = 0):
    pad_data = [pad_value] * pad_size + data + [pad_value] * pad_size
    return pad_data

if __name__ == '__main__':
    from exercise59 import get_random_scores

    data = get_random_scores(n_students=10,min_val=10,max_val=20)
    print(f"original data: {data}")

    data =pad(data,pad_size=2)
    print(f"padded data: {data}")