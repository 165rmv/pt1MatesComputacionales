# simple transition function method

# Union Method

# Extended transition function



def main():
    desiredString = input("Write a desired string: ")
    dS = []
    for i in desiredString: #splits desiredString into chars
        dS.append(i)
    print(dS)
    #dictionary without values
    transitionTable = {
        "states": None, 
        "alphabet": None, 
        "initialState": None, 
        "finalStates": None,
        "evaluation": None
    } 
    file = open("test1.txt", "r")
    for x in file:
        print(x)

    file.close() 



if __name__ == "__main__": 
    main()