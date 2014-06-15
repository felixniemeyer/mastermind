import random 
import Option

class Guesser:

	def __init__(self, feedbacker): 
		self.feedbacker = feedbacker
		self.width = feedbacker.width
		self.height = feedbacker.height
		self.options = set()
		self.options.add(Option(self.width, self.height)) 
		
	def solve(self):
		solution = None
		while !solution:
			guess = self.generateGuess()
			feedback = self.feedbacker.evaluate(guess)
			if checkFeedback(feedback): 
				solution = guess.toString()
			else
				newOptions = interpretFeedback(guess, feedback) #generator
				joinOptions(newOptions)
	
	def interpretFeedback(self, guess, feedback):
		newOptions = set()
		guessSet = set(guess)
		half, full = feedback
		for fullColors in itertools.combinations(guessSet, full):
			fullColorsSet = set(fullColors)
			for halfColors in itertools.combinations(guessSet - fullColorsSet, half):
				halfColorsSet = set(halfColors)
				halfColorsDummies = ["h"+str(i) for i in halfColors ]
				for possibility in itertools.permutations((range(self.height) - guessSet) | halfColorsDummies):
					halfColorsSet = set(halfColors)
					allowed = []
					counter = 0
					skip = False
					for position in possibility: 
						while guess[counter] in fullColors: 
							allowed.append(guess[counter])
							counter += 1
						if type(position) is str:
							color = int(position[1:])
							if color == guess[counter]: #halfColor may not be at the same place it was in the guess
								skip = True
								break
							else
								allowed.append(color)
						else:
							allowed.append([x for x in set(range(self.height)) - guessSet])
						counter += 1
					if not skip:
						newOptions.add(Option(allowed))
		return newOptions
	
	def joinOptions(self, newOptions):
		joinedOptions = set()
		for option in self.options:
			for newOption in newOptions:
				joinedOption = joinOption(option, newOption)
				if checkOption(joinedOption):
					joinedOptions.add(joinedOption)
		self.options = joinedOptions
	
	def generateGuess(self)
		guess = random.sample(range(self.height, self.width)
		
	

	def score(self)
		"""at how many places can each color appear?"""
		#not used yet. relying on random ;)
		score = []
		for a in range(self.feedbacker.width):
			score.append(0)
		for option in self.options:
			rating = option.getRating()
			for i, rate in enumerate(rating):
				score[i] += rate
		
		
				
			
			
