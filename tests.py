from readCFG import process_file_to_production_rules as getCFG
import algs

def example_test():
    cfg = getCFG("tests/1")
    d2l = algs.derivesToLambda(cfg, "A")
    first = algs.firstSet(cfg, "A", "", set())
    follow = algs.followSet(cfg, "A")


    assert(d2l == True)
    # ...
    print(d2l)
    print(sorted(first[0]))
    print(follow)
    
def main():
    example_test()
    
if __name__ == "__main__":
    main()

