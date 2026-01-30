def pad(data,**kwargs):
    if 'pad_size' in kwargs:
        pad_size = kwargs['pad_size']
    else: pad_size = 2

    if "pad_value" in kwargs:
        pad_value = kwargs['pad_value']
    else:
        pad_value = 0
    pad_data = [pad_value] * pad_size + data + [pad_value] * pad_size
    return pad_data




test_data = [10,20,30]
print(pad(test_data))
print(pad(test_data, pad_size=3))
print(pad(test_data, pad_value=1))
print(pad(test_data ,pad_size=3, pad_value=1))