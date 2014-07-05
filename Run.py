from manualfeedbacker import ManualFeedbacker
from guesser import Guesser

print("Welcome, im a masterminded bot.")

guesser = Guesser(ManualFeedbacker())
solutionString = guesser.solve()

print("Well it seems like i've found the solution. It's: " + solutionString)

print("Goodbye you fool! ;)")
