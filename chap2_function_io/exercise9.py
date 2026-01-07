import random



def print_score_mean(scores):
    score_mean = sum(scores) / len(scores)
    print(f"score_mean: {score_mean}")


n_student = 5
num_scores = [random.randint(0,100) for _ in range(n_student)]
print(num_scores)
print_score_mean(num_scores)

