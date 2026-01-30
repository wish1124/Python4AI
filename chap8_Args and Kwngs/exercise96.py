def print_params(*args,**kwargs):
    print(f"{kwargs = }")
    print(f"{args = }")

print_params(1,2,a=10,b=20)