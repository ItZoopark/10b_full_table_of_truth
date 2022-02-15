def f(x, y, z, w):
    return ((x <= y) and (not z)) or w


def f_1626(x, y, z, w):
    return (x <= (y and (not z))) or w


def pol_1626():
    print('x y z w')
    print('-------')
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    if f_1626(x, y, z, w) == 0:
                        print(x, y, z, w)


def f_4146(a, b, c, d):
    return (a <= b) and (not (b == c) and (d <= a))


def pol_4146():
    print('a b c d')
    print('-------')
    for a in range(0, 2):
        for b in range(0, 2):
            for c in range(0, 2):
                for d in range(0, 2):
                    if f_4146(a, b, c, d) == 1:
                        print(a, b, c, d)


# pol_4146()

def f_56(a, b, c):
    return (a and c) or ((not a) and (c <= b))


def pol_56():
    print('a b c')
    print('-----')
    for a in range(0, 2):
        for b in range(0, 2):
            for c in range(0, 2):
                if f_56(a, b, c) == 0:
                    print(a, b, c)


pol_56()
