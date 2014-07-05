import random
from option import Option
from itertools import combinations, permutations


class Guesser:

    def __init__(self, feedbacker):
        self.feedbacker = feedbacker
        self.width = feedbacker.width
        self.height = feedbacker.height
        self.options = [Option.newWithTrue(self.width, self.height)]

    def solve(self):
        solution = None
        while not solution:
            guess = self.generateGuess()
            feedback = self.feedbacker.evaluate(guess)
            if self.checkFeedback(feedback):
                solution = guess.toString()
            else:
                newOptions = self.interpretFeedback(guess, feedback)
                self.joinOptions(newOptions)
                if len(self.options) == 0:
                    print("Das Feedback war widersprüchlich.")
                if len(self.options) == 1:
                    print("Now i know the solution ;)")
        return solution

    def checkFeedback(self, feedback):
        return feedback == (0, self.width)

    def interpretFeedback(self, guess, feedback):
        """
        This function generates all options that fit the guess and feedback
        """
        newOptions = []
        #guess is a list, we need it as a set for set operations
        guessSet = set(guess)
        half, full = feedback
        #decide what colors from guess where at the right place
        for fullColors in combinations(guessSet, full):
            fullColorsSet = set(fullColors)
            #decide what colors from guess do appear
            for halfColors in combinations(guessSet - fullColorsSet, half):
                for possibility in self.scatterXOnYPermutations(halfColors, self.width - full):
                    option = self.generateAllowedList(possibility, guess, fullColors)
                    if option is not None:
                        newOptions.append(option)
        return newOptions

    def generateAllowedList(self, possibility, guess, fullColors):
        guessSet = set(guess)
        allowed = []
        dummy = iter(possibility)
        skip = False
        for place in range(self.width):
            if guess[place] in fullColors:
                allowed.append([guess[place]])
            else:
                d = next(dummy)
                if d == -1:
                    allowed.append(list(set(range(self.height)) - guessSet))
                else:
                    color = d
                    if color == guess[place]:
                        skip = True
                        break
                    else:
                        #halfColor at a different place it was in the guess
                        allowed.append([color])
        if not skip:
            option = Option(self.width, self.height)
            option.setDataByAllowedList(allowed)
            return option
        else:
            return None

    def scatterXOnYPermutations(self, items, places):
        solutions = [[-1 for x in range(places)]]
        for item in items:
            newSolutions = []
            for solution in solutions:
                for i, value in enumerate(solution):
                    if value == -1:
                        newSolutions.append(solution[:i] + [item] + solution[i+1:])
            solutions = newSolutions
        return solutions

    def joinOptions(self, newOptions):
        joinedOptions = []
        print("joining with new options:")
        self.printOptions(newOptions)
        for option in self.options:
            for newOption in newOptions:
                joinedOption = Option.newFromMerge(option, newOption)
                if joinedOption.isValid():
                    joinedOptions.append(joinedOption)
        joinedOptions = self.cleanOptions(joinedOptions)
        self.options = joinedOptions
        print("results in:")
        self.printOptions(joinedOptions)

    def cleanOptions(self, options):
        cleanedOptions = []
        for a in options:
            if a not in cleanedOptions:
                cleanedOptions.append(a)
        return cleanedOptions

    def printOptions(self, options):
        for option in options:
            print(option.__str__())

    def generateGuess(self):
        return self.options[0].findSpecificGuess()

    def score(self):
        """at how many places can each color appear?"""
        #not used yet. relying on random ;)
        score = []
        for a in range(self.feedbacker.width):
            score.append(0)
        for option in self.options:
            rating = option.getRating()
            for i, rate in enumerate(rating):
                score[i] += rate
