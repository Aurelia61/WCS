def longest_consec(strarr, k):
    n = len(strarr)
    lenght = 0
    if n == 0 or n < k or k <= 0 :
        return ""
    else:
        for word in strarr :
            print(f'le mot :: {word}')
            for index in range(len(strarr) - k) :
                for number in range(k) :
                    print(f'le nombre :: {number}')
                    print(f'le longueur du mot au numéro :: {len(word[number])}')
                    lenght += len(word[number])
                    print(f'longueur :: {lenght}')

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) 
