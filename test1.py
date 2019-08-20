# test1 por Vinicio Valbuena

class T1:
    def __init__(self, *args, **kwargs):
        print('__init__', args, kwargs)

    def __call__(self, *args, **kwargs):
        print('__call__', args, kwargs)

    def __eq__(self, other):
        return isinstance(other, T1)

def main():
    print('- A')
    objA = T1()   # __init__
    objA()        # __call__

    print('- B')
    objB = T1()   # __init__
    objB('hello') # __call__

    print('- C')
    objC = T1('hello') # __init__
    objC()             # __call__

    print('compare A == B  ',   objA == objB)  # __eq__
    print('compare A == C  ',   objA == objC)  # __eq__
    print('compare C == str',   objC == str()) # __eq__

if __name__ == '__main__':
    main()
