#To find the character occurence in the string#
def concc(str):
    x = {}
    for i in str:
        if i in x:
            x[i]+=1
        else:
            x[i] =1    

    return x

str = "ritujaa"
res = concc(str)
print(res)
