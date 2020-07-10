# 1ere solution
def to_jaden_case(string):
    string = " ".join(w.capitalize() for w in string.split())
    return print(string)


to_jaden_case("how can")

