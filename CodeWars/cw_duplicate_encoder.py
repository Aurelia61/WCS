def duplicate_encode(word) :
    result = []
    for letter in word.lower() :
        # nb_letter = word.lower()count(letter)
        # print(f'{letter} :: {nb_letter}')
        if word.lower().count(letter) == 1 :
            result.append("(")
        else:
            result.append(")")
    return("".join(result))

print(duplicate_encode("Success"))