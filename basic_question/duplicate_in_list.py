def find_duplicate(l:list):
    dupes = []
    s = set()
    for i in l:
        if i in s :
            dupes.append(i)
        else:
            s.add(i)
    return dupes            

print(find_duplicate([1,2,3,4,3,3,5,6]))