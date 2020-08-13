def count_smileys(arr):

    count = 0

    eyes = [":", ";"]
    nose = ["-", "~"]
    mouth = [")", "D"]

    check_in_progress = True

    if len(arr) == 0 :
        return 0
    else:
        for index in range(len(arr)):
            check_in_progress = True
            print(f'Smiley :: {arr[index]}')
            # print(arr)
            for caractere in range(len(arr[index-1])):
                if len(arr[index]) == 3 :
                    while check_in_progress :
                        print(f'place du caractere :: {caractere}')
                        print(f'le caractere encours du smiley :: {arr[index][caractere]}')
                        if arr[index][caractere] in eyes :
                            print("ok pour les yeux")
                            print(f'2e caractere (nez) :: {arr[index][caractere+1]}')
                            if arr[index][caractere+1] in nose:
                                print("ok pour le nez")
                                print(f'3e caractere (bouche) :: {arr[index][caractere+2]}')
                                if arr[index][caractere+2] in mouth :
                                    print("ok pour la bouche")
                                    count += 1
                                    print(f'compteur :: {count}')
                                    check_in_progress = False
                                else:
                                    print("non pour la bouche")
                            else :
                                print("non pour le nez")
                                check_in_progress = False
                        else :
                            print("non pour les yeux")
                            check_in_progress = False
                elif len(arr[index]) == 2 :
                    while check_in_progress :
                        print(f'place du caractere :: {caractere}')
                        print(f'le caractere encours du smiley :: {arr[index][caractere]}')
                        if arr[index][caractere] in eyes :
                            print("ok pour les yeux")
                            print(f'2e caractere (bouche) :: {arr[index][caractere+1]}')
                            if arr[index][caractere+1] in mouth :
                                    print("ok pour la bouche")
                                    count += 1
                                    print(f'compteur :: {count}')
                                    check_in_progress = False
                            else :
                                print("non pour la bouche")
                                check_in_progress = False
                        else :
                            print("non pour les yeux")
                            check_in_progress = False
    return count



print(count_smileys([':)',':(',':D',':O',':;']))