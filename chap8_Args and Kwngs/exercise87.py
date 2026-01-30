def cal_mean(*args):
    mean = sum(args) / len(args)
    return mean

print(cal_mean(1,2))
print(cal_mean(1,2,3))
print(cal_mean(1,2,3,4))