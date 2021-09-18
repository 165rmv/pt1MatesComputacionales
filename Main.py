import pprint
import re
dS = []

transitionTable = {
    "states": [], 
    "alphabet": [], 
    "initialState": [], 
    "finalStates": [],
    "evaluation": []
}

def fillDictionary(file):
	for idx, x in enumerate(file):
		splStr = re.split(',|=>|\n', x)
		if (idx == 0):
			transitionTable["states"] = splStr
		elif (idx == 1): 
			transitionTable["alphabet"] = splStr
		elif (idx == 2):
			transitionTable["initialState"] = splStr
		elif (idx == 3):
			transitionTable["finalStates"] = splStr
		elif (idx >= 4):
			transitionTable["evaluation"].append(splStr)
		else:
			pass

def inDictionary():
	pass

# simple transition function method
def simTranFunc():
    pass

# Union Method
def unionMethod():
    pass

# Extended transition function
def extenTranFunc():
    pass


def main():
	desiredString = input("Write a desired string: ")
	for i in desiredString:
		dS.append(i)
	file = open("test1.txt", "r")
	fillDictionary(file)
	pprint.pprint(transitionTable)
	file.close()

if __name__ == "__main__": 
    main()
