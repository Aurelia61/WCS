def to_jaden_case(string):
    string_list = string.split()
    cap_string_list =[]
    for word in string_list :
        cap_word = word.capitalize()
        cap_string_list.append(cap_word)
    texte_jaden = " ".join(cap_string_list)
    print(texte_jaden)

quote = "How can mirrors be real if our eyes aren't real"  
to_jaden_case(quote)






