import random



def get_random_scores(n_students):
    random_scores = [random.randint(1,100) for _ in range(n_students)]
    return random_scores
def cal_std(data):
    n_data = len(data)

    mean = sum(data)/n_data
    squared_diffs = [(sample - mean) ** 2 for sample in data]
    var = sum(squared_diffs) / n_data
    std = var ** 0.5
    return std

n_student = 10
scores =get_random_scores(n_student)
scores_std = cal_std(scores)
print(f"{scores = }")
print(f"{scores_std = }")