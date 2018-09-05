def minSwap(t, n):
    sortList = sorted(t)
    dic = dict()
    for i in range(n):
        dic[sortList[i]] = i
    
    visited = set()
    result = 0
    for i in range(n):
        cyclesize = 1
        if t[i] not in visited:
            visited.add(t[i])
            cur = dic[t[i]]
            
            while cur != i:
                visited.add(t[cur])
                cur = dic[t[cur]]
                cyclesize += 1
        result += (cyclesize-1)
    return result
 
 

    
root=None
arr=[7,2,5,4,8]

print(minSwap(arr,5))
