def print_coords(*args):
    if len(args) == 1:
        x_list = list(range(len(args[0])))
        y_list = args[0]
    elif len(args) == 2:
        x_list = args[0]
        y_list = args[1]

        for idx,(x,y) in enumerate(zip(x_list,y_list)):
            print(f"{idx}-th coord : ({x},{y})")
        print()


print_coords([10,20,30])
print_coords([10,20,30],[3,4,5])