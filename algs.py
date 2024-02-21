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
    pass

''' First Set '''

'''
Gets the set of terminals that begin the strings derivable from the NT.
@param CFG cfg : The cfg
@param String NT : The nonterminal
@returns Set<String> : the set of terminals
'''
def firstSet(cfg, NT):
    pass

''' Follow Set '''

'''
Gets the collection of terminal symbols that occur directly to the right of a nonterminal.
@param CFG cfg : The cfg
@param String NT : The nonterminal
@returns Set<String> : the set of terminals.
'''
def followSet(cfg, NT):
    pass