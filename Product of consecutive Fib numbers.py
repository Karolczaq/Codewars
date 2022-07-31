###5kyu
def productFib(prod):
    n1 = 0
    n2 = 1
    while True:
        if n1*n2 == prod:
            return [n1,n2, True]
            break
        elif n1*n2 > prod:
            return [n1,n2, False]
            break
        else:
            nth = n1 + n2
            n1,n2 = n2,nth