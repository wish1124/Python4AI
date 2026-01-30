def print_coords(*args):
    def check_dim():
        if len(args[0]) != len(args[1]):
            print(f"ValueError: x and y must have same first dimension,"
                  f"but have shapes {len(args[0]),} and {(len(args[1]),)}")
    if len(args) == 1:
        x_list = list(range(len(args[0])))
        y_list = args[0]
    elif len(args) ==2:
        check_dim()
        x_list,y_list =args

    for idx,(x,y) in enumerate(zip(x_list,y_list)):
        print(f"{idx} -th coord: ({x},{y})")
    print()

print_coords([1,2,3])
print_coords([1,2,3],[10,20,30])
print_coords([1,2,3],[10,20,30,40])