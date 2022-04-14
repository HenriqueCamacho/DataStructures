'''Metodo 1 com ajuda de helper'''

def helper(word):

    def rev(word_1):
        if(len(word_1)==1):
            return word_1[0]
        return word_1[len(word_1)-1] + rev(word_1[:len(word_1)-1])
    
    reverse = rev(word)

    return reverse==word

palavra = 'tacocat'
print("Is "+palavra+" PAlindrome? "+ str(helper(palavra)) )

def palind(word):
    if len(word)==1:
        return True

    elif(word[0]!=word[len(word)-1]):   
        return False
    
 
    return palind(word[1:len(word)-1]) #No python, ao usar slicing, ele exclui o end, para ambos os lados do :

print("Is "+palavra+" PAlindrome? "+ str(palind(palavra)) )
