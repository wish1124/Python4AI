import random



def get_random_scores(n_students):
    score = [random.gauss(50,10) for _ in range(n_students)]
    return score
if __name__ == '__main__':

    print("======Test code=======")
    n_students = 10
    scores = get_random_scores(n_students)
    print(f"{scores = }")