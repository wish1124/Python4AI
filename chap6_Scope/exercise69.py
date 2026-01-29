def print_vars(namespace_dict):
    namespace_dict = namespace_dict.copy()
    for name,obj in namespace_dict.items():
        if not name.startswith("__"):
            print(f"{name} : {obj}")

if __name__ == '__main__':
    print_vars(globals())