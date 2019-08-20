# test2 por Vinicio Valbuena
from django.utils.module_loading import import_string
from django.utils.deconstruct import deconstructible

@deconstructible
class T2:
    def __init__(self, *args, **kwargs):
        print('__init__', args, kwargs)

    def __call__(self, *args, **kwargs):
        print('__call__', args, kwargs)

    def __eq__(self, other):
        return isinstance(other, T2)

def main():
    print('- A')
    objA = T2('vinicio', job='dev')
    path, args, kwargs = objA.deconstruct()

    print(path)
    print(args)
    print(kwargs)

    print('_T2')
    _T2 = import_string(path)

    print('- B')
    objB = _T2(*args, **kwargs)

    print('- C')
    objC = _T2('vicky', job='design')

    print('compare A == B  ',   objA == objB)
    print('compare A == C  ',   objA == objC)

if __name__ == '__main__':
    main()
