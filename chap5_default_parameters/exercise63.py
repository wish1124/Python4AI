def unique(data,return_cnt = False):
    unique_dict = {}
    for sample in data:
        unique_dict[sample] = unique_dict.get(sample,0) + 1
    if return_cnt:
        return list(unique_dict.keys()),list(unique_dict.values())
    else:
        return list(unique_dict.keys())


from exercise59 import get_random_scores

scores = get_random_scores()
print(unique(scores))
print(unique(scores,return_cnt=True))