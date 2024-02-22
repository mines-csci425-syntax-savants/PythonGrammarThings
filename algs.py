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
    def follow_set_recursive(at: str, seen: set[str]):
        if at in seen:
            return set(), seen
        
        seen.add(at)
        follow_set = set()
        for n in cfg.production_rules:
            for p in cfg.production_rules[n]:
                for i in range(len(p)):
                    if p[i] == at:
                        after = p[i+1:]
                        if len(after) > 0:
                            g = firstSet(cfg, after)
                            follow_set.update(g)
                        
                        if len(after) == 0 or len(cfg.terminals.union({"$"}).intersection(after)) == 0 and all(map(derivesToLambda, after)):
                            g, _ = follow_set_recursive(n, seen)
                            follow_set.update(g)
        return follow_set, seen

    result, _ = follow_set_recursive(NT, set())
    return result