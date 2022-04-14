def rec(numb):
    if numb==1:
        return 1
    return numb+rec(numb-1)

print(rec(5))
