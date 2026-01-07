import random



def get_random_scores(n_students):
    random_scores = [random.randint(1,100) for _ in range(n_students)]
    return random_scores

n_student = 10
scores = get_random_scores(n_student)
print(f"{scores =}")