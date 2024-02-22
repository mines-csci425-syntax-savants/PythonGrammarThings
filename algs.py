''' Helper functions '''
# put stuff here that is useful and might be used in multiple different algs


''' Derives to Lambda'''

'''
Determines if a given nonterminal will ever derive to lambda
@param CFG cfg: The cfg
@param String NT: The nonterminal to test
@returns bool
'''
def derivesToLambda(cfg, NT):
    T = [] # create an empty stack using python lists
    rhs = cfg.production_rules[NT] # get the production rules for our given non-terminal NT
    for element in rhs:
        #print(element) # for testing
        if element in T: # if element in T, continue loop - we've already looked at it
            continue
        
        for symbol in element:
            if symbol in list(cfg.terminals):
                continue
        
        if element == ['lambda']: # if element in rhs directly derives to lambda, the NT clearly derives to lambda
            return True
            
        allderivelambda = False
        for symbol in element:
            if symbol in list(cfg.nonterminals):
                T.append(NT)
                allderivelambda = derivesToLambda(cfg, symbol)
                T.pop()
                if not allderivelambda:
                    break
        if allderivelambda:
            return True
        
    return False
    

''' First Set '''

'''
Gets the set of terminals that begin the strings derivable from the NT.
@param CFG cfg : The cfg
@param String X: a part of XB, which constructs a valid sequence of grammar elements
@param String Beta: see above
@param Set T : empty set on first call, as per the first set pseudocode
@returns Set<String> : the set of terminals
'''
def firstSet(cfg, X, B, T):
    #input parsing
        #all terminals & the dollar sign
    terminalSet = set(cfg.terminals)
    terminalSet.add('$')
    
    # if NT is a terminal, then the first set is itself
    if X in terminalSet:
        return {X}, T
    
    # define first set
    f = set()
    if X not in T:
        T.add(X) # add it to T
        for item in cfg.production_rules[X]:
            if item[0] != 'lambda':
                G, I = firstSet(cfg, item[0],"", T)
                f.update(G)
                         
    if derivesToLambda(cfg, X) and len(B) > 0:
        G, I = firstSet(cfg, B, "", T)
        f.update(G)
    
    return f, T

''' Follow Set '''

'''
Gets the collection of terminal symbols that occur directly to the right of a nonterminal.
@param CFG cfg : The cfg
@param String NT : The nonterminal
@returns Set<String> : the set of terminals.
'''
def followSet(cfg, NT):
    pass