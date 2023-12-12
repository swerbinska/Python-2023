print(1, 2, 6, 5)


def test_var_args(farg, *args):
    print("formal arg:", farg)
    print(args)
    for arg in args:
        print ("another arg:", arg)

test_var_args(1, "two", 3)


def test_var_kwargs(farg, **kwargs):
    print ("formal arg:", farg)
    for key in kwargs:
        print ("another keyword arg: %s: %s" % (key, kwargs[key]))
    print (kwargs)
    return farg, kwargs
jedynka, slownik = test_var_kwargs(farg=1, myarg2="two", myarg3=3)