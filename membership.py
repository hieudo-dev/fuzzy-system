def curry(x, argc=None):
    if argc is None:
        argc = x.__code__.co_argcount
    def p(*a):
        if len(a) == argc:
            return x(*a)
        def q(*b):
            return x(*(a + b))
        return curry(q, argc - len(a))
    return p

@curry
def Pi(a, b, c, d, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    if c <= x <= d:
        return (d - x) / (d - c)
    return 1 if b <= x <= c else 0

@curry
def Triangular(a, b, m, x):
    if x <= a or x >= b:
        return 0
    elif a < x <= m:
        return (x-a)/(m-a)
    return (b-x)/(b-m)