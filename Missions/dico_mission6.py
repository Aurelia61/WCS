wildcodeschool =	{
    "data_analyst": 4,
    "total_campus" : 19,
    "data_scientist": 2,
    "dev_web": 13
}

def get_values(dictionnary):
    list_values = []
    for key in dictionnary.keys() :
        list_values.append(dictionnary[key])
    print(list_values)

get_values(wildcodeschool)

print(wildcodeschool.values())
