def cal_scores_mean(scores,base_score = 0):
    if base_score != 0:
        scores = [score+base_score for score in scores]

    scores_mean = sum(scores) / len(scores)
    return scores_mean


from exercise58 import get_random_scores

scores = get_random_scores()

scores_mean1 = cal_scores_mean(scores)
print(f"no base score: {scores_mean1}")

scores_mean2 = cal_scores_mean(scores,base_score=20)
print(f"base score 20: {scores_mean2}")