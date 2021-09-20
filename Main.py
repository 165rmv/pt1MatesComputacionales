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
		cleanX = x.strip()
		splStr = re.split(',|=>|\n', cleanX)
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

# user String validator
def inDictionary():
	s1 = set(transitionTable["alphabet"])
	s2 = set(dS)
	if len(s2) == 1:
		print(s2, "only one char")
		if(s2 & s1):
			print("GOOD String")
		else: 
			print("BAD string")
	else:
		print("more than one char")
		if(s1 == s2):
			print(s2, "sets are the same GOOD")
		else:
			print(s2, "BAD string")

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
	file.close()
	pprint.pprint(transitionTable)
	inDictionary()

if __name__ == "__main__": 
    main()
