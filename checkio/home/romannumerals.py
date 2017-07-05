def checkio(number):
    roman = ""

    while number > 0:
        if number >= 1000:
            roman += str('M')
            number -= 1000
        elif number >= 900:
            roman += str('CM')
            number -= 900
        elif number >= 500:
            roman += str('D')
            number -= 500
        elif number >= 400:
            roman += str('CD')
            number -= 400
        elif number >= 100:
            roman += str('C')
            number -= 100
        elif number >= 90:
            roman += str('XC')
            number -= 90
        elif number >= 50:
            roman += str('L')
            number -= 50
        elif number >= 40:
            roman += str('XL')
            number -= 40
        elif number >= 10:
            roman += str('X')
            number -= 10
        elif number >= 9:
            roman += str('IX')
            number -= 9
        elif number >= 5:
            roman += str('V')
            number -= 5
        elif number >= 4:
            roman += str('IV')
            number -= 4
        else:
            roman += ('I')
            number -= 1

    return roman

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    import timeit
    #These "asserts" using only for self-checking and not necessary for auto-testing
    wrapped=wrapper(checkio, 6)
    print(timeit.timeit(wrapped, number=100000))
    wrapped=wrapper(checkio, 76)
    print(timeit.timeit(wrapped, number=100000))
    wrapped=wrapper(checkio, 499)
    print(timeit.timeit(wrapped, number=100000))
    wrapped=wrapper(checkio, 3888)
    print(timeit.timeit(wrapped, number=100000))
    #assert checkio(6) == 'VI', '6'
    #assert checkio(76) == 'LXXVI', '76'
    #assert checkio(499) == 'CDXCIX', '499'
    #assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
