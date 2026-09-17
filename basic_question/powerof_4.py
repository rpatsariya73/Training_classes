def isPowerof_4(n :int)->bool:
    flag = False
    while n>0:
        if n==1 : 
            return True 
        elif n%4==0 :
            n//=4
            flag = True
        else :
            flag=False
            break
    return flag



print(isPowerof_4(64))