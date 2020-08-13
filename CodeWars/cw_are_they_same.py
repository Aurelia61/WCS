def comp(array1, array2) :
    if array1 != None and array2 != None :
        array1.sort()
        array2.sort()
        array1_mult =[]
        for number1 in array1 :
            if number1 > 0 :
                mult_array1 = number1 * number1
                array1_mult.append(mult_array1)
            elif number1 < 0 :
                number = -number1
                mult_array1 = number1 * number1
                array1_mult.append(mult_array1)
        array1_mult.sort()
        if array2 == array1_mult :
            return True
        elif array1 == [] and array2 == [] :
            return True
        else:
            return False
    elif array1 == None or array2 == None:
        return False


print(comp([-121, -144, 19, -161, 19, -144, 19, -11],[11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))