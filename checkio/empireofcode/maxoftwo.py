def my_max(a, b):
    if a > b:
        return a
    else:
        return b

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert my_max(3, 3) == 3, "First"
    assert my_max(0, 1) == 1, "Second"
    assert my_max(3, 2) == 3, "Third"

    print("All set? Click \"Check\" to review your code and earn rewards!")
