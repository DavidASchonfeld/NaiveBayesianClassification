#!/usr/bin/env python3

import os, sys, re

# Global Variables
array_training = []
array_classifying = []

# The method call that starts the appropriate methods in this file is located at the bottom of this file.

def exitUsageStatement():
    print ("Usage: %s filenameForTrainingData filenameForClassifyingData" % sys.argv[0])
#                  0 1                       2
    sys.exit()


def readTextFile(fileName_input):

    if not os.path.exists(fileName_input):
        sys.exit("Error: File %s was not found" % fileName_input)

    file_input = open(fileName_input, "r")
    array_input = []
    for input_line in file_input:

        input_lineString = input_line[:-1]
        # Adds each line from the file to the variable
        # and removes the new line character (/n) from the end of each line
        array_input.append(input_lineString.split(","))
        # Converts each line (which is a string) to an array
    file_input.close()
    return array_input


def voteToIndex(inputVote):
    if (inputVote == "y"):
        return 0
    elif (inputVote == "n"):
        return 1
    elif (inputVote == "?"):
        return 2
    else:
        sys.exit("Value %s found, invalid because it is not 'n', 'y' nor '?'" % inputVote)


def runProgram():

    # Checking # of input arguments
    if len(sys.argv) < 3:
        print("Too few argments")
        exitUsageStatement()

    if len(sys.argv) > 3:
        print("Too many arguments")
        exitUsageStatement()

    # Process Text Input Files:
    global array_training, array_classifying
    array_training = readTextFile(sys.argv[1])
    array_classifying = readTextFile(sys.argv[2])

    # Calculating P(Party)
    num_Democrats = 0
    num_Republicans = 0
    for loopSenator in range(0, len(array_training)):
        # Up to down, Iterating through each senator
        if (array_training[loopSenator][0] == 'democrat'):
            num_Democrats += 1
        elif (array_training[loopSenator][0] == 'republican'):
            num_Republicans += 1
        else:
            sys.exit('Party %s is not valid. This program assumes there are only 2 parties: \'democrats\' and \'republicans\'' % (array_training[loopSenator][0]))

    # Below, float() is added so fractions < 1 would not be rounded to 0
    P_Democrat = float(num_Democrats)/(num_Democrats + num_Republicans)
    P_Republican = float(num_Republicans)/(num_Democrats + num_Republicans)

    # Calculating P(Law X) and P(Law X | Party)
    P_Law = [[0, 0, 0]]
    P_Law_givenDemocrat = [[0, 0, 0]]
    P_Law_givenRepublican = [[0, 0, 0]]
    # We have a dummy law at the beginning because we will start counting laws at position 1 (not 0)
    # Format:
    # P_Law[
    #       [Law1: P X=Y, X=N, X=?]
    #       [Law2: P X=Y, X=N, X=?]
    #       etc.
    # ]
    for loopLaw in range(1, len(array_training[0])-1):  # Starting at 1 because 0 is the party official
        # Left to right, looping through each law a certain senator has voted on

        # Q means abstention (which is also represented by ?)
        #             Y  N  Q
        num_Answer = [0, 0, 0]
        num_Answer_givenDemocrat = [0, 0, 0]
        num_Answer_givenRepublican = [0, 0, 0]
        for loopSenator in range(0, len(array_training)):
            # Do NOT add -1 to len(array_training) or else you would skip the last senator on the list
            # Up to down, iterating through each senator
            num_Answer[voteToIndex(array_training[loopSenator][loopLaw])] += 1
            if (array_training[loopSenator][0] == 'democrat'):
                num_Answer_givenDemocrat[voteToIndex(array_training[loopSenator][loopLaw])] += 1
            elif (array_training[loopSenator][0] == 'republican'):
                num_Answer_givenRepublican[voteToIndex(array_training[loopSenator][loopLaw])] += 1
            else:
                sys.exit('Party %s is not valid. This program assumes there are only 2 parties: \'democrats\' and \'republicans\'')

        P_ThisLaw = [float(num_Answer[0])/sum(num_Answer), float(num_Answer[1])/sum(num_Answer), float(num_Answer[2])/sum(num_Answer)]
        P_ThisLaw_givenDemocrat = [float(num_Answer_givenDemocrat[0])/sum(num_Answer_givenDemocrat), float(num_Answer_givenDemocrat[1])/sum(num_Answer_givenDemocrat), float(num_Answer_givenDemocrat[2])/sum(num_Answer_givenDemocrat)]
        P_ThisLaw_givenRepublican = [float(num_Answer_givenRepublican[0])/sum(num_Answer_givenRepublican), float(num_Answer_givenRepublican[1])/sum(num_Answer_givenRepublican), float(num_Answer_givenRepublican[2])/sum(num_Answer_givenRepublican)]
        # To prevent the division from In the division, at least 1 # must be declared as a float, or if the division means a # < 0, the number will be set to 0.
        P_Law.append(P_ThisLaw)
        P_Law_givenDemocrat.append(P_ThisLaw_givenDemocrat)
        P_Law_givenRepublican.append(P_ThisLaw_givenRepublican)

    for loopMysteryPerson in range(0, len(array_classifying)):
        ProductOfAllApplicableX_givenDemocrat = 1
        ProductOfAllApplicableX_givenRepublican = 1
        for loopLaw in range(1, len(array_classifying[loopMysteryPerson])-1):
            #NOTE: We start at 1 (not 0) because '0' is the dummy space for where the party would be typed, if this was training data and not classifying data

            ProductOfAllApplicableX_givenDemocrat *= float(P_Law_givenDemocrat[loopLaw][voteToIndex(array_classifying[loopMysteryPerson][loopLaw])])
            ProductOfAllApplicableX_givenRepublican *= float(P_Law_givenRepublican[loopLaw][voteToIndex(array_classifying[loopMysteryPerson][loopLaw])])

        Numerator_Democrat = ProductOfAllApplicableX_givenDemocrat*P_Democrat
        Numerator_Republican = ProductOfAllApplicableX_givenRepublican*P_Republican

        Denominator = Numerator_Democrat + Numerator_Republican

        P_MysteryPersonIsDemocrat = Numerator_Democrat / Denominator

        print (P_MysteryPersonIsDemocrat)


# Code that runs as soon as the script is called
runProgram()
