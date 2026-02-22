class Calculator:



    def add(a, b):
        c = 0
        c += a
        c += b
        return c
    def subtract(a, b):
        c = a
        d = b
        e = c - d
        return e
    def multiply(a, b):
        for i in range (b):
            a += a + a
        return a

    def divide(a, b):
       c = a / b
       return c