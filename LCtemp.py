#!/usr/bin/env python3


class LambdaTerm:
    """Abstract Base Class for lambda terms."""

    def fromstring(self):
        """Construct a lambda term from a string."""
        raise NotImplementedError

    def substitute(self, rules):
        """Substitute values for keys where they occur."""
        raise NotImplementedError

    def reduce(self):
        """Beta-reduce."""
        raise NotImplementedError


class Variable(LambdaTerm):
    """Represents a variable."""
    def __init__(self, symbol): raise NotImplementedError

    def __repr__(self): raise NotImplementedError

    def __str__(self): raise NotImplementedError

    def substitute(self, rules): raise NotImplementedError


class Abstraction(LambdaTerm):
    """Represents a lambda term of the form (λx.M)."""

    def __init__(self, variable, body): raise NotImplementedError

    def __repr__(self): raise NotImplementedError

    def __str__(self): raise NotImplementedError

    def __call__(self, argument): raise NotImplementedError

    def substitute(self, rules): raise NotImplementedError


class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

    def __init__(self, function, argument): raise NotImplementedError

    def __repr__(self): raise NotImplementedError

    def __str__(self): raise NotImplementedError

    def substitute(self, rules): raise NotImplementedError

    def reduce(self): raise NotImplementedError

'''  
numbers:
    0 == (λsz.z)
    1 == (λsz.s(sz))
    2 == (λsz.s(s(sz)))

succession:
    Name: S
    Profile: (λxyz.y(xyz))
    inputs: m
    outputs: n = m+1
    Usage: Sm

Addition:
    Name: A
    Profile: S == (λxyz.y(xyz))
    inputs: a, b
    outputs: c = a+b
    Usage: aAb

Multiplication:
    Name: M
    Profile: (λxyz.x(yz))
    inputs: a,b
    outputs: c = a*b
    Usage: Mab
    
Predecessor:
    Name: P
    Profile: ((λn.nQ(λz.z00))F)1
    where
        Name: Q
        Profile: Profile: (λpz.z(S(pT))(pT))
        inputs: (a, b)
        outputs: (S(a), b)
        usage: Q(a,b)
    and F will be defined down below
    inputs: N, where N is a natural number
    outputs: N-1 
    Usage: PN

Subtraction:
    Name: B
    Profile: (λxy.yPx)
    inputs: m, n
    outputs: l = m - n
    Usage: Bmn

Booleans:
    True: T == (λsz.s)
    False: F == 0 == (λsz.z)
    
AND operator:
    Name: ∧
    Profile: (λxy.xy(λuv.v)) == λxy.xyF
    inputs: M, N
    outputs: M ∧ N == (T or F)
    Usage: ∧MN
    
OR operator:
    Name: ∨
    Profile: (λxy.x(λuv.u)y) == λxy.xTy
    inputs: M, N
    outputs: M ∨ N == (T or F)
    Usage: ∨MN

Negation:
    Name: ¬
    Profile: (λx.x(λuv.v)(λab.a)) == λx.xFT
    inputs: M
    outputs: N == negation of M
    Usage: ¬ M
'''