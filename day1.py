#DAY 1 - Coding
'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

#Brute force
"""
def sumup (arr,k):
    for i in range (len(arr)):
        j=i+1
        while j<len(arr):
            if arr[i]+arr[j]==k:
                return True
            j+=1
    return False
"""

def sumup(arr,k):
    seen=set()
    for x in arr:
        comple = k-x
        if comple in seen:
            return True
        else:
            seen.add(x)
    return False
if __name__ == "__main__":
    arr=[10,15,3,7]
    k=17
    print(sumup(arr,k))


