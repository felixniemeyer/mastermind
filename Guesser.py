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
		guessSet = set(guess)
		half, full = feedback
		for fullColors in itertools.combinations(guessSet, full):
			fullColorsSet = set(fullColors)
			for halfColors in itertools.permutations(guessSet - fullColorsSet, half):
	
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
		
		
				
			
			
