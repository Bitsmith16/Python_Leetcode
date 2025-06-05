# 2367 Number of Arthimetic Triplet

'''
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

 

Example 1:

Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
Example 2:

Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

Logic - its sorted array so need to start from the right. Take the difference of element at right and diff. We get our first element then check
if this element is present in input array if yes then again take the diffrence we get the 2nd element if this element present in input array
that means we got our first triplet and hence increment the count and at the end returning count.

'''
def arithmeticTriplets( nums, diff):
    count =0
    
    for right in range(len(nums)-1,0,-1):
        element = nums[right] - diff
        
        if element in nums:
            element2 = element - diff
            if element2 in nums:
                count += 1
    return count



if __name__=='__main__':
    print("Enter the int array elements (space-separated):")

    num = list(map(int,input().split()))
    print("Enter the difference")

    difference = int(input())

    result = arithmeticTriplets(num,difference)

    print(f"Result is : {result}")
