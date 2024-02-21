# PythonGrammarThings

## The CFG Object
The main information that the CFG object provides is ```production rules```. 
Production rules is a dictionary. The key is the LHS as a string. The value 
is a 2D list containing each output to the given production rule.

The CFG also contains **untested** helper methods ```getRHS()``` and ```getAllOccurencesOfRHS()```. Note that the latter returns the whole production rule where a symbol is found on the RHS as a 2D list, not just the spots where it was found.

## The algorithms
Some basic starting methods and their parameters have been outlined in ```algs.py```. **This is where most of your work should take place.**

## Testing
Testing exists in ```tests.py``` and the test input files exist in the ```tests``` directory.

## Entry point
If generating the CFG object from another file, the entry point is
```process_file_to_production_rules```. There should be a valid entry point while testing, or you can create a function in the ```tests.py``` file to run and call your algorithm with a specified input file.