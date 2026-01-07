def cal_divosors(num):
    divisors = []

    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


num = int(input("Enter a number"))
divisors = cal_divosors(num)
print(f"divisors of {num} are {divisors}")