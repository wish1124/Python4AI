input_num = int(input())

def cal_divisor(num):
    divisor = []

    for i in range(1,num+1):
        if num % i == 0:
            divisor.append(i)
    print(f"The divisors of {num} are {divisor}")

cal_divisor(input_num)

