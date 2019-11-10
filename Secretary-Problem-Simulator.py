# This program finds the optimal solution to the secretary problem by using the Monte Carlo method and learning
# Importing time and random packages so that random numbers can be generated with time seed 0
import random
import time

# There are all variables that the user can quickly modify to change how accurate the output will be. Of course, higher inputs for sampleSize, highestPossibleScore, iterationsPerPercent will result in more accuracy
random.seed(time.time())  # Allows for random num generation
wholesomeIterationLimit = 20 # This specifies how many times the simulation will be run. A higher value results in higher accuracy
wholesomeIteration = 0 # This initializes the wholesomeIteration variable with value 0. This keeps track of which iteration the program is on
wholesomeTotal = 0 # This keeps track of the sampling window sizes that are most accurate for each iteration
while wholesomeIteration < wholesomeIterationLimit:
    sampleSize = 100 # How many samples we will take/ candidates we will interview.
    highestPossibleScore = 200 # Highest possible score per applicant
    percentTested = 10 # Starting percent tested. Will increment up for each percent being tested
    upperPercentLimit = 90 # Defining the highest percent that we will test
    percentIncrements = 1 # How much we increment percentTested by for each test
    iterationsPerPercent = 100 # How many times we test a given percent
    testingWindowList = [] #testwindow list value
    currentList = [] # Initializing current list which will have randomly generated values to represent the interview candidates
    iterationAccuracy = 0 # iteration is the accuracy of the percent you are currently on. This will change as the program iterates for each trial of a specific percent
    highestIterationAccuracy = 0 # This is the highest accuracy that you have from a given percent
    mostAccurateTestWindow = 0 # This is the most accurate iteration of percentTested and will change depending on which one becomes the most accurate
    testWindowListMaximum =0 # This is the maximum of the testWindow of a given percent. This will change between trials and percents tested
    optimalSolutionCounter = 0 # This keeps track of how many times the program successfully gets the highest value with the method
    testListMaxResult = 0 # This keeps track of the first value of the actual sampling window that is greater than or equal to the maximum of the testing window

    #This while loop iterates and tests for every perecent until the end
    while percentTested<upperPercentLimit:

        # Letting the user know that the program is testing a given percent
        print('Program working correctly. Currently on iteration', wholesomeIteration+1)

        # Creating a new list with all values of 0 for each percent tested. Resetting optimalSolutionCounter and testListMaxResult after each percent is tested
        currentList = [0] * sampleSize
        optimalSolutionCounter = 0
        testListMaxResult = 0

        # This iterates for as many times as specified in the above variables. Essentially, it will iterate a certain number of times to remove outliers and get a resalistic view of how accurate a given percent is
        for iterations in range(0, iterationsPerPercent):

            # Resetting testWindowListMaximum to 0 between each iteration
            testWindowListMaximum=0

            # This iterates for every index in currentList and will fill it up with random values
            for i in range(sampleSize):
                # Setting the index of currentList equal to a random number from 1 to the highestPossibleScore as specified above
                currentList[i] = random.randint(0,highestPossibleScore)
                # Incrementing i up one between each iteration
                i+=1

            # Setting actualListMaximum equal to the highest value/best candidate from the randomly generated currentList
            actualListMaximum = max(currentList)
            # Setting testWindowSize equal to our sampleSize as specified above and for the percentTested for the current interation. Casting as an integer since it will be our length of the sub-list
            testWindowSize = int((sampleSize * percentTested/100))
            # Setting testingWindowList equal to a sublist from index 0 to the testWindowSize as specified above to represent the testing window of the current iteration
            testingWindowList = currentList[0:testWindowSize]
            # Setting testWindowListMaximum equal to the maximum/best candidate for the testing window that we are currently using. This is used as reference for when to pick a candidate
            testWindowListMaximum = max(testingWindowList)

            # This for loop wll iterate and and find a value after the testing window where we will look for a value/candidate that is chosen based on the maximum of the test window experience
            # Starting at testWindowSize since we only want to look past the testWindow to sampleSize-1 since the index if the length-1
            for j in range (testWindowSize, sampleSize):#changed
                # This if statement evaluates if the current value is >= max of the test window (concept of the secretary problem)
                if currentList[j] >= testWindowListMaximum:
                    # Setting this value to the varaible testListMaxResult so it can be compared to the actual maximum
                    testListMaxResult = currentList[j]
                    # Break loop since once you select a candidate, you don't interview any more. You make the decision based on your test window experience and then you choose immediately afterwards
                    break

                # If you are unable to find a candidate/value greater than the testWindowListMaximum then you get stuck with the last candidate and this will evalute true if you are on the last index
                elif j == (sampleSize-1):
                    # Setting your chosen candidate/testListMaxResult equal to the last index if you can't find anything with your testWindowMaximu
                    testListMaxResult = currentList[j]

                # Incrementing j up by 1 so that all indices can be tested
                j += 1

            # Evaluating if the candidate chosen/testListMaxResult is the actual best candidate/maximum of the list/actualListMaximum
            if testListMaxResult == actualListMaximum:
                # If you did get the best candidate, optimalSolutionCounter will mark that down
                optimalSolutionCounter += 1

            # Iterating iterations variable up by one for the loop to functoin correctly
            iterations += 1

        # Calculating the accuracy of the current iteration/percent by calculating how many times the optimal solutions were gotten divided by how many iterations were tested. Should be set depending on the computer tested
        # This is used to compare the accuracy between loops
        iterationAccuracy = optimalSolutionCounter/(iterationsPerPercent)

        # If the accuracy of the current iteration is highest and the current highest, then the if statement will evaluate to true
        if iterationAccuracy > highestIterationAccuracy: #changed
            # Setting the highest iteration accuracy equal to the current one
            highestIterationAccuracy = iterationAccuracy
            # Setting the mostAccurateTestWindow to the percent that we just tested that had the highest accuracy
            mostAccurateTestWindow = percentTested

        # Iterating percentTested by percentIncrements so that more testing window sizes can be tested
        percentTested += percentIncrements

    # Adding mostAccurateTestWindow to the wholesomeTotal which will eventually be evaluated to average the most accurate test windows
    wholesomeTotal +=mostAccurateTestWindow
    # Incrementing wholesomeIteration up by 1 to go to the next iteration
    wholesomeIteration+=1


# Calculate the average for the optimal percentage for the sampling window by dividing the total by the number of iterations
wholesomeTotal = wholesomeTotal/wholesomeIterationLimit
# At the end, printing out the most accurate window size
print('\n \n \n', wholesomeTotal, "Percent is the optimal percentage of the test/sampling window size")