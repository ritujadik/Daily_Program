x = [1,2,3,4,5,-2,-1,-3]
x1 = []
unique = []
for i in range(len(x)):
    for j in range(i+1,len(x)):
        for k in range(i+2,len(x)):
            if x[i] + x[j] + x[k] == 0;
                triplet = tuple(sorted([x[i],x[j],x[k]]))
                if triplet not in unique:
                    unique.add(triplet)
                    x1.extend(triplet)
print(x1)        