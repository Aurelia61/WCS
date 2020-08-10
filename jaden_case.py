

#   #  #    solution la plus courte   #  #  #

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())


#   #  #    solution la plus documentée   #  #  #
def toJadenCase(string):
    #splitting sentence to individual words in list
    wordList = string.split()
    
    #creating a list to hold capitalized words
    capWordList = []
    
    #looping through wordList to capitalise words
    for word in wordList:
    
        #capitalization
        capWord = word.capitalize()
        
        #adding capitalized word to capWordList
        capWordList.append(capWord)
    
    #joining words in capWordList as Jaden Case
    jadenCase = " ".join(capWordList)
    
    #returning the final case to the function
    return jadenCase