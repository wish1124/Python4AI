def edit_list(test_list):
    test_list = test_list.copy()
    test_list[0] = 10

def edit_dict(test_dict):
    test_dict =test_dict.copy()
    test_dict['a'] = 10

test_list = [1,2,3]
edit_list(test_list)
print(test_list, '\n')

test_dict = {'a' : 1 , 'b' : 2}
edit_dict(test_dict)
print(test_dict)