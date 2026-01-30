def cal_score_mean(scores, **kwargs):
    if 'base_score' in kwargs:
        scores = [score + kwargs['base_score'] for score in scores]

    scores_mean = sum(scores) / len(scores)
    return scores_mean


scores = [10, 20, 30]
print(cal_score_mean(scores))
print(cal_score_mean(scores, base_score=10))