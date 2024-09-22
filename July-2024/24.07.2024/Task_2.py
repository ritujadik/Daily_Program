def uppercase(strings):
    x = strings.split(" ")
    result = []
    for i in x:
        if i and i[0].islower():
            result.append(i[0].upper() + i[1:])
        else:
            result.append(i)    
    return " ".join(result)       

print(uppercase("hi how are you . what's up"))  