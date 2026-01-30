def print_params(a=10,*args,**kwargs):
    print(f"{a = }")
    print(f"{args = }")
    print(f"{kwargs = }")


print_params()
print_params(1)
print_params(1,10,20,30)
print_params(1,kw1=100,kw2=200)
print_params(1,20,30, kw1=100,kw2=200)