class Calculator:

#adds ints together
    @staticmethod
    def add(a, b):
        c = 0
        c += a
        c += b
        return c

#subtracts them
    @staticmethod
    def subtract(a, b):
        c = a
        d = b
        e = c - d
        return e

    @staticmethod
    def multiply(a, b):
        for i in range (b):
            a += a + a
        return a

#divides them
    @staticmethod
    def divide(a, b):
       c = a / b
       return c