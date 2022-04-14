def hash(key, arrlen):
    total = 0
    weird_prime = 31
    for i in range(0, min(100, len(key))):
        char = key[i]
        value = ord(char)
        total = (total*weird_prime + value) % arrlen
        
    return key
