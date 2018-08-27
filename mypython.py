 
"""  *** Slugger ***
            
"""
################### IMPORT #############################

#import math
from sys import stdin, stdout
#from collections import Counter,deque,OrderedDict
#from itertools import permutations
from heapq import heapify,heappush,heappop,heappushpop,heapify,heapreplace,nlargest,nsmallest
import heapq as hp #for priority queue
import bisect as bi #for binary search

####################### INPUT ####################### 
 
def si():
    return str(stdin.readline())
def ii():
    return int(input())
def mi():
    return map(int, stdin.readline().split())
def li():
    return list(map(int,input().split()))

###################### Main ###############################

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
        

m,n=mi()

k=li()
print(k)

