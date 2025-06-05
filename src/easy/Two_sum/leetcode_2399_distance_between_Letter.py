# 2399. check distance between letters

'''
You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. 
You are also given a 0-indexed integer array distance of length 26.Each letter in the alphabet is numbered 
from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).In a well-spaced string, the number of letters 
between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be 
ignored.Return true if s is a well-spaced string, otherwise return false.

So basiaclly there is an input string and a distance list like in below example for a the distance is 1 that means there should be only 1 element between a similarly for b the distance list is 3 that means there should be 3 element in s between b
for c the distance list is 0 that means there should be no element between 2 c and for D the distance list is 5 so there should be 5 element between d but d is not present in example.

As all the element are as per distance list. Hence it return True.

Example 1:

Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: true

Explanation:
- 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
- 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
- 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
Return true because s is a well-spaced string.

Example 2:

Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: false

Explanation:
- 'a' appears at indices 0 and 1 so there are zero letters between them.
Because distance[0] = 1(which means there should be 1 element between a which is false here), s is not a well-spaced string.

Logic , 2nd occurence of element index - 1st occurence of element index - 1 == distance.

'''
def checkDistances(str1, distance):
    first_occurence = {}
    
    for second_occurence,char in enumerate(str1):
        index = ord(char) - ord('a')
        if char in first_occurence:
            expected = distance[index]
            actual = second_occurence - first_occurence - 1
            if actual != expected:
                return False
            else:
                first_occurence[char] = i
    return True




if __name__ == '__main__':
    print("Enter the input string s:")
    str1 = list(input())

    print("Enter the distance:")
    distance = list(input())

    result = checkDistances(str1,distance)
    print(f"Result is : {result}")


