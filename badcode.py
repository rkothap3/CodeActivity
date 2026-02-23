class Calculator:

#adds ints together
    @staticmethod
    def add(a, b):
        #defines code
        c = 0 #sets c to 0
        c += a
        c += b
        return c # return c

#subtracts them
    @staticmethod
    def subtract(a, b):
        c = a
        d = b
        e = c - d #subtracts c and d
        return e # returns e

    @staticmethod
    def multiply(a, b):
        for i in range (b):
            a += a + a # adds a to itself
        return a #returns e

#divides them
    @staticmethod
    def divide(a, b):
       c = a / b
       return c #returns e