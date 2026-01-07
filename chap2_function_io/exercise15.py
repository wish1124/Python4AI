import random




def get_random_scores(n_students):
    random_scores = [random.randint(1,100) for _ in range(n_students)]
    return random_scores

def cal_mean(data):
    mean = sum(data) / len(data)
    return mean

n_student =10
scores = get_random_scores(n_student)
scores_mean =cal_mean(scores)
print(f"{scores = }")
print(f"{scores_mean =}")
