def pow(bs, exp):
    if(exp==0):
        return 0
    elif(exp<0):
        print("Negative exponent")
        return -1
    elif(exp==1):
        return bs
    return bs*pow(bs,exp-1) 

print(pow(-2,3))
