def maxset(A):
    i=0
    maxs=-1
    curr_sum=0
    flag=0
    max_lis=[]
    lis=[]
    while (i<len(A)):
        if(A[i]<0):
            curr_sum=0
            i+=1
        else:

            curr_sum+=A[i]
            lis.append(A[i])
            if(maxs<curr_sum):
                maxs=curr_sum
                if(i<len(A)-1 and A[i+1]<0):
                    max_lis.append(lis)
                    lis=[]
                    
            
            
            i+=1
            
    print(max_lis) 

A =[ 1, 2, 5, -7, 2, 5 ]     
maxset(A)    
    