# 387. First Unique character in a string

'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input:  s = "leetcode"
Output: 0

Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Logic - counter will be a creating a dictionary with frequence of each charter in string and then in for loop we are checking chracter which is having count of 1(which means single occurence)
'''

from collections import Counter

def firstUniqChar(str1):
    count = Counter(str1)

    for index,char in enumerate(str1):
        if count[char]==1:
            return index,char
    return -1,-1


if __name__=='__main__':
    print("Enter the string:")

    string = input()

    result,char = firstUniqChar(string)

    if char == -1:
        print(f"There is no non repeating character in string \"{string}\" ")

    else:
        print(f"The index of first non repeating character {char} is : {result}")

