# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:10:44 2019

test

@author: bramp
"""

def alpha_prevention(M, N):
    #gegeven twee lambdatermen, hernoemt deze fucntie alle variabelen in beide expressies zodat deze niet botsen.
    
    # omzetten naar lijst format als input een str is, anders onveranderd
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