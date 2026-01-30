def test_function(param1,param2,param3):
    print(f"{param1} / {param2} / {param3}")


test_function(*[1,2,3])
test_function(*(1,2,3))