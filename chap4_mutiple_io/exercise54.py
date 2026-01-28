def split_scores(scores,threshold):
    score_pass,score_no_pass = [],[]
    for score in scores:
        if score > threshold: score_pass.append(score)
        else:
            score_no_pass.append(score)
    return score_pass,score_no_pass

from exercise44 import get_randiant_data

n_students,min_val,max_val = 20,0,100
threshold = 80

scores = get_randiant_data(n_data = n_students,min_val=min_val,max_val=max_val,random_seed=0)

print(f"{scores = }")

score_pass, score_no_pass = split_scores(scores,threshold)
print(f"{score_pass = }")
print(f"{score_no_pass = }")