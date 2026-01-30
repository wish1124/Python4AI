def print_params(a,*args,b=10,**kwargs):
    print(f"{a = }")
    print(f"{args = }")
    print(f"{b = }")
    print(f"{kwargs = }")

print_params(1)
print_params(1,10,20)
print_params(1,10,20,b=100)
print_params(1,10,20,b=100,kew1=1000,kw2 =2000)