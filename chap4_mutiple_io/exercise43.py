import random

def get_normal_data(n_data,mean,std):
    data = [random.gauss(mu = mean, sigma=std) for _ in range(n_data)]
    return data

def extract_pass_scores(scores,thershold):
    pass_scores = [score for score in scores if score >= thershold]
    return pass_scores
def extract_no_pass_scores(scores,thershold):
    no_pass_scores = [score for score in scores if score < thershold]
    return no_pass_scores

n_data,gen_mean,gen_std = 30,70,10
thershold = 80
scores = get_normal_data(n_data=n_data,mean = gen_mean,std=gen_std)

pass_scores = extract_pass_scores(scores=scores, thershold=thershold)
no_pass_scores = extract_no_pass_scores(scores=scores,thershold=thershold)
print(f"{pass_scores}")
print(f"{no_pass_scores}")
