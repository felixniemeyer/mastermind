import numpy


class Option:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = None

    def setDataByAllowedList(self, allowed):
        if len(allowed) == self.width and self.height > self.width:
            self.data = numpy.zeros((self.width, self.height), dtype=bool)
            for column in range(self.width):
                for rowId in allowed[column]:
                    self.data[column][rowId] = True
        else:
            print("error when parsing parameters to create Option!\n")

    def setData(self, data):
        self.data = data

    def __str__(self):
        for row in range(self.height):
            for column in range(self.width):
                print("O" if self.data[column][row] else "#", end="")
            print("")

    def newFromMerge(a, b):
        width = a.width
        height = b.height
        if height == b.height and width == b.width:
            data = numpy.zeros((width, height), dtype=bool)
            for row in range(height):
                for column in range(width):
                    data[column][row] = a.data[column][row] and b.data[column][row]
            option = Option(width, height)
            option.setData(data)
            return option
        else:
            return None

    def findSpecificGuess(self):
        return self.findGuessRecursively([], 0)

    def findGuessRecursively(self, prefix, column):
        if column == self.width:
            return prefix
        for i, cell in enumerate(self.data[column]):
            if cell and i not in prefix:
                guess = self.findGuessRecursively(prefix + [i], column+1)
                if guess is not None:
                    return guess

    def newWithTrue(width, height):
        data = numpy.ones((width, height), dtype=bool)
        option = Option(width, height)
        option.setData(data)
        return option

    def newWithFalse(width, height):
        data = numpy.zeros((width, height), dtype=bool)
        option = Option(width, height)
        option.setData(data)
        return option

    def isValid(self):
        for place in range(self.width):
            ok = False
            for color in range(self.height):
                if self.data[place][color]:
                    ok = True
                    break
            if not ok:
                return False
        return True

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return numpy.array_equal(self.data, other.data)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
