def print_params(a,*args,**kwargs):
    print(f"{a = }")
    print(f"{args =}")
    print(f"{kwargs = }")

print_params(1)
print_params(1,10,20,30)
print_params(1,10,20,30,kw1 = 100,kw2 = 200)