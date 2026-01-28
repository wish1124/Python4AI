def cal_max_min(data,max=True):
    target_value,target_idx = None,None

    for sample_idx,sample in enumerate(data):
        if max:
            if target_value == None or sample >target_value:
                target_value = sample
                target_idx = sample_idx
        else:
                if target_value == None or sample < target_value:
                    target_value = sample
                    target_idx = sample_idx
    return target_value,target_idx

if __name__ == '__main__':
    from exercise59 import get_random_scores

    scores = get_random_scores()
    score_max = cal_max_min(scores)
    score_min = cal_max_min(scores,max=False)
    print(f"{score_max = } / {score_min = }")