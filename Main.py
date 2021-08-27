# simple transition function method

# Union Method

# Extended transition function



def main():
    desiredString = input("Write a desired string: ")
    dS = []
    for i in desiredString: #splits desiredString into chars
        dS.append(i)
    print(dS)
    #add to transitionTable "states": , "alphabet": , "initialState": , "finalStates": ,"evaluation":
    transitionTable = {} #empty dictionary
    f = open("test1.txt", "r")
    for x in f:
        print(x)

    f.close() 



if __name__ == "__main__": 
    main()