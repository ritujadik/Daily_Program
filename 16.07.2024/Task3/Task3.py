def sortstring(str):
    x = {}
    for i in str:
        x[i] = ord(i)
        sortdict = {key:value for key,value in sorted(x.items(),key=lambda item:item[1])}
    return sortdict
    

str="RiTuJA"
m = sortstring(str)
print(m)