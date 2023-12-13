

def function_with_error(i):
    try:
        l = [0]
        return l[i]
    finally:
        print("Finally in function_function_with_error")


def ok_function():
    return function_with_error(6)

