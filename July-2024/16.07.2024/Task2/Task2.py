def sumzero(num):
    result = {}
    found_pair = 0
    for i in num:
            if -i in num:
                  result[i] = -i
                  found_pair +=1
                  if found_pair == 2:
                        break
                  
    if not found_pair:
          print("there is no pair")      
    return result

num = [1,2,-1,-2,3,4,0,0]
x = sumzero(num)
print(x)