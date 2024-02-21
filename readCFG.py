from string import ascii_uppercase
from collections import OrderedDict

'''
Class that contains the detected information of a CFG in one spot.
'''
class CFG:
    def __init__(self):
        self.terminals = {}
        self.nonterminals = {}
        self.production_rules = OrderedDict()
        self.start = None
        self.reserved_words = {"lambda", "->", "|", "$"}

    '''
    Gets the RHS of a production rule
    @param String NT : the name of the nonterminal to get the RHS for.
    @returns a 2D list containing the information on the RHS of the production rule
    '''
    def getRHS(self, NT):
        return self.production_rules[NT]
    
    '''
    Gets all production rules that contain NT on the RHS
    @param String NT: the name of the nonterminal to search for
    @returns OrderedDict occurs: The production rules where NT is on the RHS
    '''
    def getAllOccurencesOfRHS(self, NT):
        occurs = OrderedDict()
        for rule in self.production_rules:
            for entry in self.production_rules[rule]:
                if NT in entry:
                    occurs[rule] = self.production_rules[rule]
        return occurs

    '''
    Formats the output for printing a CFG.
    '''
    def print(self):
        print("Grammar Non-Terminals")
        print(", ".join(list(self.nonterminals)))
        print("Grammar Symbols")
        terminals = ", ".join(sorted(list(self.terminals)))
        nonterminals = ", ".join(sorted(list(self.nonterminals)))
        print(terminals + ", " +  nonterminals)

        i = 1
        for NT in self.production_rules:
            rhs = self.production_rules[NT]
            for element in rhs:
                print(f"({i})\t{NT} -> {" ".join(element)}")
                i += 1

        print(f"Grammar Start Symbol or Goal: {self.start}")

'''
Used to take a production rule, detect deliminators on the RHS (such as |),
then convert the 1D list into a 2D list, where each inside list is the 
production rule that is deliminated by the | symbol.
@param List<String> list : the RHS of an unformatted production rule
@param String delim : the deliminating string.
@returns List<List<String>> whole_list: 2D list of production rules, split by |.
'''
def group_list_by_delim(list, delim):
    whole_list = []
    new_list = []
    for element in list:
        for e in element:
            if e != delim:
                new_list.append(e)
            else:
                whole_list.append(new_list)
                new_list = []
        if new_list not in whole_list:
            whole_list.append(new_list)
            new_list = []
    return whole_list

'''
Takes a CFG input file and generates a CFG object.
@param List<String> lines : File content.
@returns CFG : CFG object
'''
def process_file_to_production_rules(lines):
    cfg = CFG()
    lines = lines.split()
    for i, token in enumerate(lines):
        # get the production rule mappings
        if token == "->":
            lhs = lines[i-1]
            if "->" in lines[i+1:]:
                next_t = lines[i+1:].index("->") + i+1
            else:
                next_t = len(lines) + 1

            # remove the | symbol
            rhs = lines[i+1:next_t - 1]
            if lhs in cfg.production_rules:
                cfg.production_rules[lhs].append(rhs)
            else:
                cfg.production_rules[lhs] = [rhs]
                if cfg.start == None and "$" in rhs:
                    cfg.start = lhs

        # see if token contains nonterminal
        for char in token:
            if char in ascii_uppercase:
                cfg.nonterminals[token] = None
                break
        
        # add the terminals
        if token not in cfg.reserved_words and token not in cfg.nonterminals:
            cfg.terminals[token] = None

    # group items in the production rules
    for N in cfg.production_rules:
        rhs = cfg.production_rules[N]
        rhs = group_list_by_delim(rhs, "|")
        cfg.production_rules[N] = rhs

    return cfg

def main():
    input = "1"
    with open(input, "r") as f:
        lines = f.read()

    cfg = process_file_to_production_rules(lines)
    cfg.print()

if __name__ == "__main__":
   main()