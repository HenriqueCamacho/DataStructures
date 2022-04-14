def hashh(word, vocab):
    hash_value = 0
    aux= 0
    for i in range(len(word)-1, -1, -1):
        hash_value += vocab[word[aux]]*len(vocab)**i        
        aux+=1      

    return hash_value



'''
def rabinKarp(string, substring):
    vocab = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}
    pattern_hashh = hashh(substring, vocab)  
    for i in range(len(string)-len(substring)+1):
        hassh_value = hashh(string[i:i+len(substring)], vocab)
        
        hassh_value = (value-vocab[string[i-1] ]*len(vocab)**(len(substring)-1) )  * len(vocab)+ vocab[string[i+2]]                
                
        if hassh_value == pattern_hashh:
            if string[i:i+len(substring)]==substring:
                return True
    return False
'''

def rabinKarp(string, substring):
    vocab = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}
    pattern_hashh = hashh(substring, vocab)  
    hassh_value = hashh(string[0:0+len(substring)], vocab)
    for i in range(0, len(string)-len(substring)+1):
        if i>=1:
            hassh_value = (hassh_value-vocab[string[i-1] ]*len(vocab)**(len(substring)-1) )  * len(vocab)+ vocab[string[i+len(substring)-1]]
        if hassh_value == pattern_hashh:
            for l in range(0, len(substring)):
                if string[i+l] != substring[l]:
                    break
                if l==len(substring)-1:
                    return True                    
    return False


print(rabinKarp('daccaccaaedbiadbaa', 'caccaae') )
