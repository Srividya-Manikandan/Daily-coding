"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""
#Brute force
'''
def prodarray(arr):
    result = []
    for i in range(len(arr)):
        prod=1
        for j in range(len(arr)):
            if i!=j:
                prod*=arr[j]
        result.append(prod)
    return result
'''

def prodarray(nums):
    result=[]
    prod=1
    #collect the product of prefixes. (prod of all numbers before this number)
    for i in range(len(nums)):
        result.append(prod)
        prod*=nums[i]
    prod=1
    #collect the product of sufixes. (prod of all numbers after this number)
    for i in range(len(nums)-1,-1,-1):
        result[i]*=prod
        prod*=nums[i]
    #so except this number, every other numbers product is taken
    return result
if __name__ == "__main__":
    arr1 = [1,2,3,4,5]
    print(prodarray(arr1))
    arr2 = [3,2,1]
    print(prodarray(arr2))