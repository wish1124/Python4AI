from exercise69 import print_vars

def test_function():
    x =10
    print(f"Local : {locals()}")
    print("function terminated\n")


test_function()
print("Global")
print_vars(globals())
