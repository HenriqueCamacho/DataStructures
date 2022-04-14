def rev(word):
    if(len(word)==1):
        return word[0]
    return word[len(word)-1] + rev(word[:len(word)-1])

print(rev("abcd"))
