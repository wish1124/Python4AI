import random



def print_mean_var_std(scores):
    n_student = len(scores)
    score_mean = sum(scores) / len(scores)
    sqared_diffs = [(score -score_mean)**2 for score in scores]
    score_var = sum(sqared_diffs) / n_student
    score_std = score_var**0.5

    print(f"mean: {score_mean:.2f}\nvar: {score_var:.2f}\n std: {score_std:.2f}")

n_student = 10
my_scores =[random.randint(0,100) for _ in range(n_student)]
print(my_scores)
print_mean_var_std(my_scores)


