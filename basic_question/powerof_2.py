def isPowerof_2(n :int)->bool:
    flag = False
    while n>0:
        if n==1 : 
            return True 
        elif n%2==0 :
            n//=2 
            flag = True
        else :
            flag=False
            break
    return flag



print(isPowerof_2(127))