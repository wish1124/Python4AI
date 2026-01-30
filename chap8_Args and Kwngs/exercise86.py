def test_function(*args): #args 몇개가 들어오든 묶어서 처리
    print(f"{args = }")


test_function(1)
test_function(1,2)
test_function(1,2,3)

test_function([3,2,1],3,4)
test_function("abc" ,3 , "Hello World")