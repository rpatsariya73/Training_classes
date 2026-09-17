def integerInList(l:list):
    freq = dict()
    for i in l:
        if i in freq.keys():
            freq[i]+=1
        else:freq[i]=1

    for i in freq.keys():
        print(freq[i],end=' ')             

integerInList([1,2,3,2,2,4,5,5])