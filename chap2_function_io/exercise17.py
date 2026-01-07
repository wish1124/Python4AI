def cal_sum_upto_n(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print(cal_sum_upto_n(5))
print(cal_sum_upto_n(10))
print(cal_sum_upto_n(20))
