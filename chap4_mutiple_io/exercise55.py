import random


def random_split(data, train_size):
    data = data.copy()
    n_total_data = len(data)
    n_train_data = int(train_size * n_total_data)

    random.shuffle(data)
    train_ds = data[:n_train_data]
    test_ds = data[n_train_data:]

    return train_ds, test_ds
from exercise44 import get_randiant_data
dataset = list(range(100))
print(f"{len(dataset) =} -> {dataset = }")

train_ds , test_ds = random_split(dataset,train_size=0.6)
print(f"{len(train_ds) = } -> {train_ds = }")
print(f"{len(test_ds) = } -> {test_ds = }")