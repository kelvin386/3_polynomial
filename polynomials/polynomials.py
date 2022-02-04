class Polynomial:
    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):   #It defines what is returned for str(p) and print(p)

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
