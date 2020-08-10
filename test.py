def accum(s) :
    result = []
    for index, letter in enumerate(s) :
        result.append(letter.upper() + (letter.lower() * index))
    return "-".join(result)


print(accum("abcd"))




# def toJadenCase(string):
#     print(string)
#     #splitting sentence to individual words in list
#     wordList = string.split()
#     print(wordList)
    
#     #creating a list to hold capitalized words
#     capWordList = []
#     print(capWordList)
    
#     #looping through wordList to capitalise words
#     for word in wordList:
    
#         #capitalization
#         capWord = word.capitalize()
#         print(capWord)

        
#         #adding capitalized word to capWordList
#         capWordList.append(capWord)
    
#     #joining words in capWordList as Jaden Case
#     jadenCase = " ".join(capWordList)
    
#     #returning the final case to the function
#     return jadenCase

# toJadenCase("abcd")