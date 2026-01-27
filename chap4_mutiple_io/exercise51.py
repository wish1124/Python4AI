from exercise44 import get_randiant_data

def standardization(data,verbose):
    n_data = len(data)

    mean = sum(data) / n_data
    var = sum([ (sample-mean)**2 for sample in data ]) / n_data
    std = var **0.5

    data_ = data.copy()
    for sample_idx,sample in enumerate(data_):
        data_[sample_idx] = (sample-mean) /std
    if verbose:
        print(f"===============Before standardization ========")
        print(f"{mean = } / {std = }\n")

        mean = sum(data_) / n_data
        var = sum([(sample - mean) ** 2 for sample in data]) / n_data

        print(f"============After Standardization============")
        print(f"{mean = } / {std = }")
        std = var ** 0.5
    return data_

n_students = 10
scores = get_randiant_data(n_students,min_val=0,max_val=100,random_seed=0)

scores_stdz = standardization(scores,verbose=False)
print(f"{scores = }")
print(f"{scores_stdz = }")
