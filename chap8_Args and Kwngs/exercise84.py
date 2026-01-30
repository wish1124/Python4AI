test_list = [1,2,3,4,5]

a,b,*c = test_list
print(a,b,c)

*a,b,c  = test_list
print(a,b,c)

a,*b,c = test_list
print(a,b,c)