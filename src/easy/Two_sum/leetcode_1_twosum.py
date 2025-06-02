# 1. Two Sum

'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

'''
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

def twoSum(nums, target):
    # Write your code here 
    final_ele = {}                         # creating a dictionary where we will have element
    for index in range(len(nums)):              
        second_num = target - nums[index]       # 2nd number is target minus firt number
        if second_num in final_ele:                  # if 2nd number exist in Final_ele dictionary then returning current number index and 2nd number index
            return [index,final_ele[second_num]]
        final_ele[nums[index]] = index          # entering number in dictionary having key as number and value is its index
    
    return [-1, -1]  # placeholder


if __name__ == '__main__':
    print("Enter number of element:")
    n = int(input())
    print("Enter the int array element")
    nums = list(map(int, input().split()))
    print("Enter the Target")
    target = int(input())

    result = twoSum(nums, target)
    print(result[0], result[1])

## Optimized solution

'''
def twosum(nums,target):
    seen = {}
    for index,num in enumerate(nums):            # Enumerate will return index & num.
        complement = target - num               # complement is the 2nd number which we need with respect to current number in order to meet the target
        if complement in seen:                  # if complement exist in seen then we will retrieve its value(which is index of this element)
            return (index,seen[complement])
        seen[num] = index
    return [-1,-1]    


