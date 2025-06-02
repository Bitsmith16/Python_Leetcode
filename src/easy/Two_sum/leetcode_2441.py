# 2441. Largest positive integer that exist with its Negative 
'''
Given an integer array nums that does not contain any zeros, find the largest positive integer k 
such that -k also exists in the array.Return the positive integer k. If there is no such integer, return -1.

 

Example 1:
Input       : nums = [-1,2,-3,3]
Output      : 3
Explanation : 3 is the only valid k we can find in the array.

Example 2:
Input       : nums = [-1,10,6,7,-7,1] -7 -1 1 6 7 10
Output      : 7
Explanation : Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Example 3:

Input       : nums = [-10,8,6,7,-2,-3]
Output      : -1
Explanation : There is no a single valid k, we return -1.
'''
def findMaxk(nums):
    nums.sort()
    left =0
    right= len(nums) -1
    while(left<right):
        if nums[right] == -(nums[left]):
            return nums[right]
        right -=1
    return -1


if __name__=='__main__':
    print("Enter the int array elements (space-separated):")
    num=list(map(int,input().split()))

    result = findMaxk(num)
    print(f"Result is {result}")

    

    
