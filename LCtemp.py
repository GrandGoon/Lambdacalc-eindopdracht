#!/usr/bin/env python3

import itertools


class LambdaTerm:
    """Abstract base class for lambda terms."""

<<<<<<< HEAD
=======

>>>>>>> Davy_the_sequel
    def __eq__(self, other): #tests if given lambda Terms are alpha-equivalent after beta-reduction
        def full_sub(sub, substr, perm): #sub denotes list of symbols in str to be subsituted, substr denotes said string, perm denotes what the symbols are to be substituted with
            mal = [0]*(len(substr))
            newstr = ''
            for i in range(0, len(substr)):
                if substr[i] in ['(', ')', '@', 'λ', '\\', '.', ' ']:
                    mal[i]=substr[i]
            for i in range(0, len(perm)):
                for k in range(0, len(substr)):
                    if substr[k] == sub[i]:
                        mal[k] = perm[i]
            for i in range(0, len(mal)):
                newstr += str(mal[i])
            return newstr
        alpha_eq=False
        self=self.reduce()
        other=other.reduce()
        if type(self) == type(other):
            #try permutations
            selfstr=str(self)
            otherstr=str(other)
            selfsyms = []
            othersyms = []
            for i in range(0, len(selfstr)):
                if selfstr[i] not in selfsyms and selfstr[i] not in ['(', ')', '@', 'λ', '\\', '.', ' ']:
                    selfsyms.append(selfstr[i])
            for i in range(0, len(otherstr)):
                if otherstr[i] not in othersyms and otherstr[i] not in ['(', ')', '@', 'λ', '\\', '.', ' ']:
                    othersyms.append(otherstr[i])
            if len(selfsyms) == len(othersyms):
                permstocheck = list(itertools.permutations(selfsyms))
                for i in range(0, len(permstocheck)):
                    if selfstr == full_sub(othersyms, otherstr, permstocheck[i]):
                        alpha_eq = True
                        break
        return alpha_eq
<<<<<<< HEAD

    def fromstring(self):
        """Construct a lambda term from a string."""
        self=self.strip()
        
        def dict_parentheses(string): #makes a dictionary that matches indices of opening parentheses to indices of corresponging closing parentheses.
=======


    def fromstring(self):
        """Construct a lambda term from a string."""
        self = self.strip()
        def dict_parentheses(string): #Makes a dictionary that matches indices of opening parentheses to indices of corresponging closing parentheses.
>>>>>>> Davy_the_sequel
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
<<<<<<< HEAD
        
        haakjes = dict_parentheses(self)
        traverser = 0
        #start Term.
        if self[0] not in ['(', '@', 'λ', ')', '\\']: #found a variable.
            Term = Variable(self[0])
            traverser += 1
        elif self[0] == '(': #evaluate Term within parentheses.
            Term = LambdaTerm.fromstring(self[1:haakjes[0]])
            traverser = haakjes[0]+1
        else: #@ or λ can only be encountered at start of string, thus
            Term = Abstraction(Variable(self[1]), LambdaTerm.fromstring(self[3:]))
            traverser = len(self)
        while traverser < len(self):
            if self[traverser] not in ['(', '@', 'λ', ')', ' ', '\\']: #found a variable.
                Term = Application(Term, Variable(self[traverser]))
                traverser+=1
            elif self[traverser] == '(': #evaluate term in parentheses
=======

        haakjes = dict_parentheses(self)
        traverser = 0
        #Start Term.
        if self[0] not in ['(', '@', 'λ', ')', '\\']:  #Found a variable.
            Term = Variable(self[0])
            traverser = 1
        elif self[0] == '(':  #evaluate Term within parentheses.
            Term = LambdaTerm.fromstring(self[1:haakjes[0]])
            traverser = haakjes[0]+1
        else:  #@ or λ or \ can only be encountered at start of string, thus
            Term = Abstraction(Variable(self[1]), LambdaTerm.fromstring(self[3:]))
            traverser = len(self)
        while traverser < len(self):
            if self[traverser] not in ['(', '@', 'λ', ')', '\\']:  #found a variable.
                Term = Application(Term, Variable(self[traverser]))
                traverser+=1
            elif self[traverser] == '(':  #Evaluate term in parentheses
>>>>>>> Davy_the_sequel
                Term = Application(Term, LambdaTerm.fromstring(self[traverser+1:haakjes[traverser]]))
                traverser=haakjes[traverser]+1
            elif self[traverser] == ' ':
                traverser += 1
<<<<<<< HEAD
            else: return "illegal string" #@ or λ can only be encountered at start of string.
        return Term
=======
            else: return "illegal string"  #@ or λ can only be encountered at start of string.
        return Term


    def reduce(self):
        """Automatically runs the correct reduction function when reduce() is called from LambdaTerm"""
        if isinstance (self, Variable):
            return Variable.reduce(self)
        elif isinstance (self, Abstraction):
            return Abstraction.reduce(self)
        else:
            return Application.reduce(self)


>>>>>>> Davy_the_sequel

class Variable(LambdaTerm):
    """Represents a variable."""
    def __init__(self, symbol):
        self.symbol = symbol
    def __repr__(self):
        return 'Variable('+repr(self.symbol)+')'
    def __str__(self):
        return str(self.symbol)
    def substitute(self, rules):
<<<<<<< HEAD
        #let rules always be given in format [a, b] where a is the variable that should be replaced by lambdaterm b.
        if self.symbol == rules[0].symbol:
            return rules[1]
        return self
    def reduce(self):   #extra function to stop recursive reduction when recurson of Application reaches this class
=======
        #let rules always be given in format [a, b] where a is the variable that should be replaced by variable b.
        if self.symbol == rules[0].symbol:
            self.symbol = rules[1].symbol
        return self
    def reduce(self):   #Extra function to stop recursive reduction when recurson of Application reaches this class
>>>>>>> Davy_the_sequel
        return self

class Abstraction(LambdaTerm):
    """Represents a lambda term of the form (λx.M)."""

    def __init__(self, variable, body):
        self.variable = variable
        self.body = body
<<<<<<< HEAD
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
=======
        self.rewind = self
    def __repr__(self):
        return "Abstraction("+repr(self.variable)+', '+repr(self.body)+')'
    def __str__(self):
        return '(λ'+str(self.variable)+'.'+str(self.body)+')'
    def __call__(self, argument):
        copy = self
        return Application(copy, argument).reduce()
    def substitute(self, rules): #Given new variable should never collide with bound variable! also, we assume that variable in self.variable is immutable
        self.body = self.body.substitute(rules)
        return self
    def reduce(self):   #Extra function to facilitate recursive reduction when recurson of Application encounters this class
>>>>>>> Davy_the_sequel
        self.body=self.body.reduce()
        return self

class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

<<<<<<< HEAD
    def __init__(self, function, argument): #implementeer Alfa-conversie om name collisions te voorkomen
=======
    def __init__(self, function, argument): #Implementeer Alfa-conversie om name collisions te voorkomen
>>>>>>> Davy_the_sequel
        self.function = function
        self.argument = argument
    def __repr__(self):
        return 'Application('+repr(self.function)+', '+repr(self.argument)+')'
    def __str__(self):
<<<<<<< HEAD
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
=======
        return '('+str(self.function)+str(self.argument)+')'
    def substitute(self, rules):
        self.function.substitute(rules)
        self.argument.substitute(rules)
        return self
    def reduce(self):
>>>>>>> Davy_the_sequel
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
<<<<<<< HEAD
            return (type(self.function), type(self.argument)) 
            
=======
            return (type(self.function), type(self.argument))
>>>>>>> Davy_the_sequel
