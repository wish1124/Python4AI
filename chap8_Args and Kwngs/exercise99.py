def print_params(a,b=10,*args,**kwargs):
    print(f"{a = }")
    print(f"{b = }")
    print(f"{args = }")
    print(f"{kwargs = }")

print_params(1)
print_params(1,2)
print_params(1,2,10,20)
print_params(1,2,kw1=100,kw2=200)
print_params(1,2,10,20,kw1=100,kw2=200)