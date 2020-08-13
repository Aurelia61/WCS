
# # # #   my solution   # # # #

def to_camel_case(text):
    list_tx = list(text)
    result = []
    if len(list_tx) != 0 :
        for index in range(len(list_tx)):
            if list_tx[index] == "_" or list_tx[index] == "-" :
                list_tx[index+1] = list_tx[index+1].upper()
            if list_tx[index] == "_" :
                result.append("")
            elif list_tx[index] == "-" :
                result.append("")
            else :
                result.append(list_tx[index])
    else:
        print("")
    result_tx = "".join(result)
    return result_tx

print(to_camel_case("The-stealth-warrior"))


# # # #   solution plus courte   # # # #
def to_camel_case(text):
    list = [x for x in text]
    if len(list) != 0: 
        for i in range(len(list)):
            if list[i] in ('-', '_'):
                list[i+1] = list[i+1].upper()
    list = ''.join([i for i in list if i not in ('-', '_')])
    return list

print(to_camel_case("The-stealth-warrior"))