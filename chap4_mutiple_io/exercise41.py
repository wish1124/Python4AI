def cal_score_mean(scores,base_score):
    score_sum = 0
    for score in scores:
        score_sum += score +base_score
    score_mean = score_sum / len(scores)
    return score_mean

scores = [10,20,30]

score_mean1 =cal_score_mean(scores =scores,base_score=0)
score_mean2 =cal_score_mean(scores =scores,base_score=10)
score_mean3 =cal_score_mean(scores =scores,base_score=20)

print(f"no base score: {score_mean1}")
print(f"base score 10:  {score_mean2}")
print(f"base score 20: {score_mean3}")