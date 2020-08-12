def CheckLevel(score):
    """
        Checking the Level to adapt the diffculties
    """
    #global Level,Add
    if score in range(0,250): #Level 1
        Add=20
        Level=1
        return Add, Level
    elif score in range(250,500): #Level 2
        Add=18
        Level=2
        return Add, Level
    elif score in range(500,750): #Level 3
        Add=16
        Level=3
        return Add, Level
    elif score in range(750,1000): #Final Level
        Add=14
        Level=4
        return Add, Level

add_current = 20
level_current = 1

Score = int(input("e"))

(Add , Level) = CheckLevel(Score)
add_current = Add
level_current = Level

print (add_current , level_current)