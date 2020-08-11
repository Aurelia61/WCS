def count_smileys(arr):
    for index in range(len(arr)):
        for caractere in arr[index]:
            if caractere[:1] == ":" or caractere == ";" :
                print("ok")
            if caractere[1:1] == "" :
                print("ok")
            else:
                continue



print(count_smileys([':D',':~)',';~D',':)']))