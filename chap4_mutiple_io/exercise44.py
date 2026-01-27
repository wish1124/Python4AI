import random



def get_randiant_data(n_data,min_val,max_val,random_seed):
    random.seed(random_seed)

    data = [random.randint(min_val,max_val) for _ in range(n_data)]
    return data

if __name__ == "__main__":
    n_data, min_val, max_val =10,0,10
    data = get_randiant_data(n_data=n_data,min_val=min_val,max_val=max_val,
                             random_seed=0)
    print(f"{data = }")
