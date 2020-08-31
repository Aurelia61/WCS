from dataAnalyst import dataAnalyst

def methode():

    dataAnalyst1 = dataAnalyst()

    dataAnalyst.suivreFormation(dataAnalyst1)
    print(f'La méthode suivreFormation() a été utilisée.')
    print(f'motivation vaut maintenant {dataAnalyst1.motivation}')
    print(f'progression vaut maintenant {dataAnalyst1.progression}')
    if dataAnalyst1.motivation < 0 :
        print("BRAVO TU AS GAGNÉ !!!")        
    elif dataAnalyst1.progression > 100:
        print("BRAVO TU AS APPRIS !!!")        
    else:
        dataAnalyst.bosserPlus(dataAnalyst1)
        print(f'La méthode bosserPlus() a été utilisée.')
        print(f'motivation vaut maintenant {dataAnalyst1.motivation}')
        print(f'progression vaut maintenant {dataAnalyst1.progression}')
        if dataAnalyst1.motivation < 0 :
            print("BRAVO TU AS GAGNÉ !!!")            
        elif dataAnalyst1.progression > 100:
            print("BRAVO TU AS APPRIS !!!")            
        else:
            dataAnalyst.echouer(dataAnalyst1)
            print(f'La méthode echouer() a été utilisée.')
            print(f'motivation vaut maintenant {dataAnalyst1.motivation}')
            print(f'progression vaut maintenant {dataAnalyst1.progression}')
            if dataAnalyst1.motivation < 0 :
                print("BRAVO TU AS GAGNÉ !!!")                
            elif dataAnalyst1.progression > 100:
                print("BRAVO TU AS APPRIS !!!")
            else:
                dataAnalyst.reussir(dataAnalyst1)
                print(f'La méthode reussir() a été utilisée.')
                print(f'motivation vaut maintenant {dataAnalyst1.motivation}')
                print(f'progression vaut maintenant {dataAnalyst1.progression}')
                if dataAnalyst1.motivation < 0 :
                    print("BRAVO TU AS GAGNÉ !!!")
                elif dataAnalyst1.progression > 100:
                    print("BRAVO TU AS APPRIS !!!")
                else:
                    dataAnalyst.echouer(dataAnalyst1)
                    print(f'La méthode echouer() a été utilisée.')
                    print(f'motivation vaut maintenant {dataAnalyst1.motivation}')
                    print(f'progression vaut maintenant {dataAnalyst1.progression}')
                    if dataAnalyst1.motivation < 0 :
                        print("BRAVO TU AS GAGNÉ !!!")                        
                    elif dataAnalyst1.progression > 100:
                        print("BRAVO TU AS APPRIS !!!")
                    else:
                        dataAnalyst.bosserPlus(dataAnalyst1)
                        print(f'La méthode bosserPlus() a été utilisée.')
                        print(f'motivation vaut maintenant {dataAnalyst1.motivation}')
                        print(f'progression vaut maintenant {dataAnalyst1.progression}')
                        if dataAnalyst1.motivation < 0 :
                            print("BRAVO TU AS GAGNÉ !!!")
                            
                        elif dataAnalyst1.progression > 100:
                            print("BRAVO TU AS APPRIS !!!")
                        else:
                            dataAnalyst.echouer(dataAnalyst1)
                            print(f'La méthode echouer() a été utilisée.')
                            print(f'motivation vaut maintenant {dataAnalyst1.motivation}')
                            print(f'progression vaut maintenant {dataAnalyst1.progression}')
