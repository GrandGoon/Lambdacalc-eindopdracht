#!/usr/bin/env python3


class LambdaTerm:
    """Abstract Base Class for lambda terms."""

    def fromstring(self):
        """Construct a lambda term from a string."""
        raise NotImplementedError

    def substitute(self, rules):
        """Substitute values for keys where they occur."""
        #let rules always be given in format [a, b] where a is the variable that should be replaced by variable b.
        raise NotImplementedError
    def reduce(self):
        """Beta-reduce."""
        raise NotImplementedError

class Variable(LambdaTerm):
    """Represents a variable."""
    def __init__(self, symbol):
        self.symbol = symbol
        self.allargs = True
    def __repr__(self):
        return 'Variable('+repr(self.symbol)+')'
    def __str__(self):
        return str(self.symbol)
    def substitute(self, rules):
        #let rules always be given in format [a, b] where a is the variable that should be replaced by variable b.
        if self.symbol == rules[0].symbol:
            self.symbol = rules[1].symbol
        return self

class Abstraction(LambdaTerm):
    """Represents a lambda term of the form (λx.M)."""

    def __init__(self, variable, body): #alpha conversie!
        self.variable = variable
        self.body = body
        self.allargs = False
    def __repr__(self):
        return "Abstraction("+repr(self.variable)+', '+repr(self.body)+')'
    def __str__(self):
        return '(λ'+str(self.variable)+'.'+str(self.body)+')'
    def __call__(self, argument): raise NotImplementedError
        
    def substitute(self, rules): #given new variable should never collide with bound variable! also, we assume that variable in self.variable is immutable
        self.body = self.body.substitute(rules)
        return self

class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

    def __init__(self, function, argument): #implementeer Alfa-conversie om name collisions te voorkomen
        self.function = function
        self.argument = argument
        if type(self.function) == type(self.argument) == Variable:
            self.allargs = True
        else:
            self.allargs = False
    def __repr__(self):
        return 'Application('+repr(self.function)+', '+repr(self.argument)+')'
    def __str__(self):
        if self.allargs:
            return str(self.function)+str(self.argument)
        elif self.function.allargs and self.argument.allargs:
            return str(self.function)+str(self.argument)
        else:
            return '('+str(self.function)+')'+ str(self.argument)
    def substitute(self, rules):
        self.function.substitute(rules)
        self.argument.substitute(rules)
        return self
    def reduce(self): raise NotImplementedError
