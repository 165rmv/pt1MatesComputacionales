#-*- coding: utf-8 -*-
import pprint
import re

dS = []
firstElement = ""
lastElement = ""
dSlength = 0
transitionTable = {
    "states": [], 
    "alphabet": [], 
    "initialState": [], 
    "finalStates": [],
    "evaluation": None
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
		else:
			pass
			"""
			firstKey.append(splStr[0])
			eval = dict.fromkeys(firstKey)
			for i in range(len(eval)): 
				if splStr[i] == eval[i]:
					print(splStr[i]==eval[i])
				else:
					pass
			#print(eval)
			"""
	#return eval
			

# user String validator
def inDictionary():
	s1 = set(transitionTable["alphabet"])
	s2 = set(dS)
	#if a=0 String is accepted else String not acccepted
	if len(s2) == 1: 
		if(s2 & s1): #if element of dS in alphabet it's accepted
			a = 0
		else:
			a = -1
	else:
		if(s1 == s2): #if sets are the same it's accepted
			a = 0
		else:
			a = -1
	return a; 

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
	desiredString = input("Write a desired string: ").lower()
	for i in desiredString:
		dS.append(i)
	firstElement = dS[0]
	lastElement = dS[len(dS)-1]
	dSlength = len(dS)
	file = open("test1.txt", "r")
	fillDictionary(file)
	firstKey = transitionTable["states"]
	secondKey = transitionTable["alphabet"]
	eval = dict.fromkeys(firstKey)
	for y in firstKey:	
		eval[y] = dict.fromkeys(secondKey)
	pprint.pprint(eval)
	pprint.pprint(transitionTable)	
	
	file.close()
	if inDictionary() == -1:
		quit("\033[91m {}\033[00m".format('String is not accepted'))
	else: 
		print("\033[96m {}\033[00m".format("String can be processed"))
		print(firstElement, lastElement, dSlength)


if __name__ == "__main__": 
    main()
