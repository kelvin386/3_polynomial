from numbers import Number

class Polynomial:
    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):   #The special method defines what is returned for str(p) and print(p)

        coefs = self.coefficients
        terms = []

        if coefs[0]:     #0 is False; same as if coefs[0] == 0
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:  #same as if self.degree() ==0...
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c==1 else c}x^{d}"
                    for d,c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"
        #if the former is an empty string, then the empty string is false, hence return "0"
        #if the former is not empty, return it

    def __eq__(self, other):
        
        return isinstance(other, Polynomial) \
            and self.coefficients == other.coefficients #check whether the second argument is a Poly, then compare

    def __add__(self, other):
        
        #The addition of tuples is concatenation! Can't just add them!
        if isinstance(other, Polynomial):
            
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a+b for a,b in zip(self.coefficients, other.coefficients)) #zip will stop when one of them runs out
            coefs += self.coefficients[common:] + other.coefficients[common:] #The lower degree one will have nothing after "common"

            return Polynomial(coefs)
        
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0]+other,)+self.coefficients[1:])

        else:
            return NotImplemented


    def __radd__(self,other):
        return self + other #Reverse add is the same as normal add
