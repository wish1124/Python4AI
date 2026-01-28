import random

def get_random_scores(n_students=20,min_val=0,max_val=100,random_seed = None):
    if random_seed is not None:
        random_seed(random_seed)

    scores = [random.randint(min_val,max_val) for _ in range(n_students)]
    return scores

if __name__ == "__main__":
    scores = get_random_scores()
    print(f"{scores = }")


    scores =get_random_scores(random_seed=0)
    print(f"{scores = }")

    scores =get_random_scores(random_seed= 1)
    print(f"{scores = }")