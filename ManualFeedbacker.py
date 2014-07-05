class ManualFeedbacker:

    def __init__(self):
        print("how many colors?")
        self.height = int(input())
        print("how many places?")
        self.width = int(input())

    def evaluate(self, guess):
        print("\n"+str(guess)+"")
        print("how many have the right color and are at the right place?")
        full = int(input())
        print("how many have a right color but are at a wrong place?")
        half = int(input())
        print("thanks")
        return half, full
