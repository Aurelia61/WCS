import random


wildcodeschool =	{
    "data_analyst": 4,
    "data_scientist": 2,
    "dev_web": 13,
    "total_campus" : 19
}


element_delete = random.choice(['data_analyst', 'data_scientist', 'dev_web'])
print(element_delete)
del wildcodeschool[element_delete]

print(wildcodeschool)