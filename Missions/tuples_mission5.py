

def change(index, new_value) :
    my_tuple = ("data analyst", "data scientist", "data engineer", "data architect")
    my_tuple = my_tuple[0:index-1] + (new_value,) + my_tuple[index:]
    print(f' The position of the value to change : {index}, the new value : {new_value}')
    print(my_tuple)

change(3,"python")

