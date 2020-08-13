def longest_consec(strarr, k):
    n = len(strarr)
    lenght = 0
    result = ""
    if n == 0 or n < k or k <= 0 :
        return ""
    elif k == 1 :
        lenght_max = 0
        for index in range(len(strarr)) :
            lenght = len(strarr[index])
            if lenght > lenght_max :
                lenght_max = lenght
        return strarr[index]
    else:
        lenght_max = 0
        for index in range(len(strarr) - k+1):
            conc_tx = "".join(strarr[index : index+k])
            if len(conc_tx) > lenght_max :
                lenght_max = len(conc_tx)
                result = conc_tx
        return result

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
