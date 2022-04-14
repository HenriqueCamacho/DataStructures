def fac(numb):
    if numb==1:
        return 1
    return numb*fac(numb-1)

print(fac(5))
