

def prettyprint(my_2d_list, width):
    for i in range(len(my_2d_list)):
        if (i != 0) and (i % width == 0):
            print()
        print(my_2d_list[i], end="")
    print()
