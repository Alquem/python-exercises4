class InputOutString():
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())




str_obj = InputOutString()
str_obj.getString()
str_obj.printString()
