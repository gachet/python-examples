#!/usr/bin/python

class Primes(object):

    def divisible(self, x, y):
        return (0 == (x % y))

    def generateList(self, x, y):
        if (x == y):
            return [y]
        else:
            return [x] + self.generateList(x+1, y)

    def dividers(self, x):
        l = self.generateList(1, x)
        laux = []
        for i in l:
            if (0 == (x % i)):
                laux = laux + [i]
        return laux

    def primes(self, x):
        l = self.generateList(1, x)
        laux = []
        for i in l:
            d = self.dividers(i)
            if ((len(d) == 2) or (i == 1)):
                laux = laux + [i]
        return laux


    
# x = int(raw_input("Give me a number: "))
# p = Primes()
# print p.primes(x)
