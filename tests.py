from readCFG import process_file_to_production_rules as getCFG
import algs

def example_test():
    cfg = getCFG("tests/1")
    d2l = algs.derivesToLambda(cfg, "A")
    first = algs.firstSet(cfg, "A")
    follow = algs.followSet(cfg, "A")

    assert(d2l == True)
    # ...
    print(d2l)
    print(first)
    print(follow)


