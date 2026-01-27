def cal_max_min(data,max_min):
    target_value, target_idx = None,None

    for sample_idx,sample in enumerate(data):
        if max_min == 'max':
            if target_value == None or sample > target_value:
                target_value = sample
                target_idx = sample_idx
        elif max_min == 'min':
            if target_value == None or sample < target_value:
                target_value = sample
                target_idx = sample_idx
        else:
            print("TYPE ERROR: max_min in ['max','min']")

    return {'value': target_value, 'idx': target_idx}

if __name__ =='__main__':
    from exercise44 import get_randiant_data

    n_students = 10
    scores = get_randiant_data(n_students,min_val=0,max_val=100,random_seed=1)

    score_max = cal_max_min(scores,max_min = 'max')
    score_min = cal_max_min(scores,max_min='min')
    print(f"max : {score_max}")
    print(f"min : {score_min} ")
