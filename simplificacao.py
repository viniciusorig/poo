from math import gcd

class fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise Exception("apenas denomidaores maiores que zero")
        else:
            self.numerador = numerador
            self.denominador = denominador
    def __repr__(self) -> str:
        return f"{self.numerador} / {self.denominador}"
    
    def simpli(self, a, b):
        c = gcd(a, b)
        a = a/c
        b = b/c
        return fracao(a,b)

    def __add__(self, outro:'fracao'):
        a = (self.denominador * outro.numerador) + (self.numerador * outro.denominador)
        b = self.denominador * self.denominador
        return self.simpli(a,b)

    def __sub__(self, outro:'fracao'):
        a = (self.denominador * outro.numerador) + ((self.numerador * outro.denominador) *-1)
        b = self.denominador * self.denominador
        return self.simpli(a,b)
        
    def __mul__(self, outro:'fracao'):
        a = self.numerador * outro.numerador
        b = self.denominador * outro.denominador
        return self.simpli(a,b)
    
    def __truediv__(self, outro:'fracao'):
        a = self.numerador * outro.denominador
        b = self.denominador * outro.numerador
        return self.simpli(a,b)
    


a = fracao(1, 2)
print(f"fracao_orig :: {a}")
print(f"soma :: {a + a}")
print(f"sub :: {a - a}")
print(f"multi:: {a * a}")
print(f"div :: {a / a}")
    
