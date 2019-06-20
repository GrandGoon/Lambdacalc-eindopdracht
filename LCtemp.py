#!/usr/bin/env python3

#Issues: Calling An abstraction leaves the Abstraction itself permanently changed; for Id=Application(Variable('a'), Variable('a')) 
#and x=Variable('x'), calculating Id(x) gives Variable('x'), which is fair enough,
# but then printing Id gives Abstraction(Variable('a'), Variable('x')), which is nothing like the original function.

class LambdaTerm:
    """Abstract Base Class for lambda terms."""

    def fromstring(self):
        """Construct a lambda term from a string."""
        raise NotImplementedError

    def substitute(self, rules):
        """Substitute values for keys where they occur."""
        #let rules always be given in format [a, b] where a is the variable that should be replaced by variable b.
        raise NotImplementedError
   # def reduce(self):
    #    """Beta-reduce."""
     #   raise NotImplementedError

class Variable(LambdaTerm):
    """Represents a variable."""
    def __init__(self, symbol):
        self.symbol = symbol
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
        self.rewind = self
    def __repr__(self):
        return "Abstraction("+repr(self.variable)+', '+repr(self.body)+')'
    def __str__(self):
        return '(λ'+str(self.variable)+'.'+str(self.body)+')'
    def __call__(self, argument):
        copy = self
        return Application(copy, argument).reduce()
    def substitute(self, rules): #given new variable should never collide with bound variable! also, we assume that variable in self.variable is immutable
        self.body = self.body.substitute(rules)
        return self

class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

    def __init__(self, function, argument): #implementeer Alfa-conversie om name collisions te voorkomen
        self.function = function
        self.argument = argument
    def __repr__(self):
        return 'Application('+repr(self.function)+', '+repr(self.argument)+')'
    def __str__(self):
        return str(self.function)+str(self.argument)
    def substitute(self, rules):
        self.function.substitute(rules)
        self.argument.substitute(rules)
        return self
    def reduce(self): 
        if type(self.function) == Abstraction:
            return self.function.body.substitute([self.function.variable, self.argument])
        else:
            return self
