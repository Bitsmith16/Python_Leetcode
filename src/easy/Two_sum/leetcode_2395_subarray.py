# 2395. Find subarray with equal sum

'''
Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. 
Note that the two subarrays must begin at different indices.
Return true if these subarrays exist, and false otherwise.
A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:
Input       : nums = [4,2,4]
Output      : true
Explanation : The subarrays with elements [4,2] and [2,4] have the same sum of 6.

Example 2:
Input       : nums = [1,2,3,4,5]
Output      : false
Explanation : No two subarrays of continous sequence of size 2 have the same sum.We have pair (1,5) & (2,4) whose sum is 6 but those are not coninious element in main array hence its False

Example 3:
Input       : nums = [0,0,0]
Output      : true
Explanation : The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0. 
Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.


'''

def findSubarrays(nums):
    count = 0
    seen = []
    for i in range(len(nums)-1):
        target = nums[i] + num[i+1]
        if target in seen:
            return True
        else:
            seen.append(target)
    return False



if __name__ =='__main__':
    print("Enter the int array elements (space-separated):")

    num = list(map(int,input().split()))

    result = findSubarrays(num)
    print(f"Result is : {result}")

## We are adding sum of adjent number to empty list seen and if the sum already exist in seen then we are returning True.