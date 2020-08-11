
def to_camel_case(text):
    list = [x for x in text]
    print(list)
    if len(list) != 0: 
        for i in range(len(list)):
            if list[i] in ('-', '_'):
                print(list[i+1])
                list[i+1] = list[i+1].upper()
                print(list[i+1])
    list = ''.join([i for i in list if i not in ('-', '_')])
    return list


print(to_camel_case("the_stealth_warrior"))