def accum(s) :
    result = []
    for index, letter in enumerate(s) :
        result.append(letter.upper() + (letter.lower() * index))
    return "-".join(result)


print(accum("abcd"))
    
