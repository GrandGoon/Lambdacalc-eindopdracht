# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:10:44 2019

test

@author: bramp
"""

def alpha_prevention(M, N):
    #gegeven twee lambdatermen, hernoemt deze fucntie alle variabelen in beide expressies zodat deze niet botsen.
    
    # omzetten naar list format als input een str is, anders onveranderd
    M = [M[a] for a in range(0, len(M))]
    N = [N[a] for a in range(0, len(N))]
    
    def list_symbols(lambdaterm):
        #Geeft een lijst van alle symbolen in een lambdaterm.
        #Nodig voor het voorkomen van fouten door gelijke symbolen, door alfareductie.
        symbols = []
        for i in range(0, len(lambdaterm)):
            if not lambdaterm[i] in ['(', ')', 'λ', '.', ' ']:
                if not lambdaterm[i] in symbols:
                    symbols.append(lambdaterm[i])
        return symbols

    Msym = list_symbols(M)
    Nsym = list_symbols(N)
    if not bool(set(Msym)&set(Nsym)):
        return M, N
    else:
        for i in range(0,len(Msym)):
            for k in range(0, len(N)):
                if N[k] == Msym[i]:
                    newsym = N[k]
                    while newsym in Nsym or newsym in Msym or ord(newsym) in range(91, 97):
                        newsym = chr((((ord(newsym)+1)-65)%57)+65) #finds next unused symbol by scrolling through ASCII codes
                    Nsym.append(newsym)
                    for z in range(0, len(N)):
                        if N[z] == N[k]:
                            N[z] = newsym
        return M, N

def application(abstraction, variables):
    #perform alpha reduction to avoid naming conflicts
    originalvariables = variables
    abstraction, variables = alpha_prevention(abstraction, variables)
    variables_string = ''
    for c in range(0, len(variables)):
        variables_string += str(variables[c])
    if originalvariables != variables_string:
        print('Changed original variables '+originalvariables+' to new variables '+variables_string)
    #find arg part of abstraction
    for i in range(0, len(abstraction)):
        if abstraction[i]=='λ':
            argstart = i
    for j in range(argstart, len(abstraction)):
        if abstraction[j] == '.':
            argend = j
    args=[]
    for i in range(argstart+1, argend):
        args.append(abstraction[i])
    while len(variables)>0 and len(args)>0:
        for j in range(argend+1, len(abstraction)):
            if abstraction[j]==args[0]:
                abstraction[j]=variables[0]
        del args[0]
        del variables[0]
    if len(args) > len(variables):
        newterm = ['λ']
        newterm.extend(args)
        newterm.append('.')
        newterm.extend(abstraction[argend+1:])
        newterm_string=''
        for c in range(0, len(newterm)):
            newterm_string += str(newterm[c])
        return newterm_string
    elif len(args) < len(variables):
        newterm = abstraction[argend+1:]
        newterm.extend(variables)
        newterm_string=''
        for c in range(0, len(newterm)):
            newterm_string += str(newterm[c])
        return newterm_string
    elif len(args) == len(variables):
        newterm = abstraction[argend+1:]
        newterm_string=''
        for c in range(0, len(newterm)):
            newterm_string += str(newterm[c])
        return newterm_string



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