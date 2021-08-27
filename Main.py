#\
# simple transition function method

# Union Method

# Extended transition function



def main():
    desiredString = input("Write a desired string: ")
    dS = []
    for i in desiredString: #splits desiredString into chars
        dS.append(i)
    #dictionary without values
    transitionTable = {
        "states": None, 
        "alphabet": None, 
        "initialState": None, 
        "finalStates": None,
        "evaluation": None
    } 
    file = open("test1.txt", "r")
    # \n needs to be splitted
    # evaluation key needs to be filled maybe another for
    for idx, x in enumerate(file):
        splitString = x.split(",")
        if idx == 0:
            transitionTable["states"] = splStr
        elif idx == 1: 
            transitionTable["alphabet"] = splitString
        elif idx == 2: 
            transitionTable["initialState"] = splitString
        elif idx == 3: 
            transitionTable["finalStates"] = splitString                        
        else: 
            pass
            
    
    print(transitionTable)
    file.close() 



if __name__ == "__main__": 
    main()