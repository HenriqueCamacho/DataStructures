def substring(word, subword):
    count = 0
    for i in range(len(word)):
        for j in range(len(subword)):
            if(word[i+j]!=subword[j]):
                break
            if j== len(subword)-1:
                count+=1
    return count
            

p = "azoazuloazul"
q = "azul"
print("Vezes que a palavra "+q+" aparece na palavra "+p + " = "+ str(substring(p, q)))
            
         

