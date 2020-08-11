def count_smileys(arr):
    count = 0

    eyes = [":", ";"]
    nose = ["-", "~"]
    mouth = [")", "D"]

    if len(arr) == 0 :
        return 0
    else:
        for index in range(len(arr)):
            for caractere in range(len(arr[index-1])):
                if len(arr[index]) == 3 :
                    if arr[index][caractere] in eyes :
                        if arr[index][caractere+1] in nose:
                            if arr[index][caractere+2] in mouth :
                                count += 1
                elif len(arr[index]) == 2 :
                    if arr[index][caractere] in eyes :
                        if arr[index][caractere+1] in mouth :
                                count += 1
    return count


print(count_smileys([':)',':(',':D',':O',':;']))