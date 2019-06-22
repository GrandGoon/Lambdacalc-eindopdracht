#!/usr/bin/env python3

#Issues: Calling An abstraction leaves the Abstraction itself permanently changed; for Id=Application(Variable('a'), Variable('a')) 
#and x=Variable('x'), calculating Id(x) gives Variable('x'), which is fair enough,
# but then printing Id gives Abstraction(Variable('a'), Variable('x')), which is nothing like the original function. RESOLVED

#ISSUE: substitution doesn't work for substituting anything but Variables by anything but Variables. RESOLVED

class LambdaTerm:
    """Abstract Base Class for lambda terms."""

    def fromstring(self):
        """Construct a lambda term from a string."""
        def dict_parentheses(string): #makes a dictionary that matches indices of opening parentheses to indices of corresponging closing parentheses.
            istart = []
            parentheses_dict = {}
            for i, c in enumerate(string):
                if c == '(':
                     istart.append(i)
                if c == ')':
                    try:
                        parentheses_dict[istart.pop()] = i
                    except IndexError:
                        return 'Error: invalid string, too many closing parentheses'
            if istart:  # check if stack is empty afterwards
                return 'Error: invalid string, too many opening parentheses'
            return parentheses_dict
        
        haakjes = dict_parentheses(self)
        traverser = 0
        #start Term.
        if self[0] not in ['(', '@', 'λ', ')']: #found a variable.
            Term = Variable(self[0])
            traverser = 1
        elif self[0] == '(': #evaluate Term within parentheses.
            Term = LambdaTerm.fromstring(self[1:haakjes[0]])
            traverser = haakjes[0]+1
        else: #@ or λ can only be encountered at start of string, thus
            Term = Abstraction(Variable(self[1]), LambdaTerm.fromstring(self[3:]))
            traverser = len(self)
        while traverser < len(self):
            if self[traverser] not in ['(', '@', 'λ', ')']: #found a variable.
                Term = Application(Term, Variable(self[traverser]))
                traverser+=1
            elif self[traverser] == '(': #evaluate term in parentheses
                Term = Application(Term, LambdaTerm.fromstring(self[traverser+1:haakjes[traverser]]))
                traverser=haakjes[traverser]+1
            else: return "illegal string" #@ or λ can only be encountered at start of string.
        return Term

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
    def __repr__(self):
        return 'Variable('+repr(self.symbol)+')'
    def __str__(self):
        return str(self.symbol)
    def substitute(self, rules):
        #let rules always be given in format [a, b] where a is the variable that should be replaced by variable b.
        if self.symbol == rules[0].symbol:
            return rules[1]
        return self
    def reduce(self):   #extra function to stop recursive reduction when recurson of Application reaches this class
        return self

class Abstraction(LambdaTerm):
    """Represents a lambda term of the form (λx.M)."""

    def __init__(self, variable, body): #alpha conversie!
        self.variable = variable
        self.body = body
    def __repr__(self):
        return "Abstraction("+repr(self.variable)+', '+repr(self.body)+')'
    def __str__(self):
        return 'λ'+str(self.variable)+'.'+str(self.body)
    def __call__(self, argument):
        copy = self
        return Application(copy, argument).reduce()
    def substitute(self, rules): #given new variable should never collide with bound variable! also, we assume that variable in self.variable is immutable
        z = self.body.substitute(rules)
        return Abstraction(self.variable, z)
    def reduce(self):   #extra function to facilitate recursive reduction when recurson of Application encounters this class
        self.body=self.body.reduce()
        return self

class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

    def __init__(self, function, argument): #implementeer Alfa-conversie om name collisions te voorkomen
        self.function = function
        self.argument = argument
    def __repr__(self):
        return 'Application('+repr(self.function)+', '+repr(self.argument)+')'
    def __str__(self):
        if type(self.function) == Abstraction: a = '('+str(self.function)+')'
        if type(self.function) == Application: a = str(self.function)
        if type(self.function) == Variable: a = str(self.function)
        if type(self.argument) == Abstraction: b = '('+str(self.argument)+')'
        if type(self.argument) == Application: b = str(self.argument)
        if type(self.argument) == Variable: b = str(self.argument)
        return a+b
    def substitute(self, rules):
        a = self.function.substitute(rules)
        b = self.argument.substitute(rules)
        return Application(a, b)
    def reduce(self): 
        if type(self.function) == Abstraction and type(self.argument) == Variable:
            return self.function.body.substitute([self.function.variable, self.argument])
        elif type(self.function) == Abstraction and type(self.argument) == Application:
            self.argument = self.argument.reduce()
            return self.function.body.substitute([self.function.variable, self.argument])
        elif type(self.function) == Variable:
            self.argument = self.argument.reduce()
            return self
        elif type(self.function) == Abstraction and type(self.argument) == Abstraction:
            z = self.function.body.substitute([self.function.variable, self.argument])
            return z.reduce()
        elif type(self.function) == Application and type(self.argument) != Application:
            self.function=self.function.reduce()
            return self.reduce()
        elif type(self.function) != Application and type(self.argument) == Application:
            self.argument = self.argument.reduce()
        elif type(self.function) == Application and type(self.argument) == Application:
            self.function = self.function.reduce()
            self.argument = self.argument.reduce()
            return self.reduce()
        else:
            return (type(self.function), type(self.argument)) #more cases?
            