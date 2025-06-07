# 2351. First letter to apper Twice

'''
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
 

Example 1:
Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

Example 2:
Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
'''

def repeatedCharacter(s):
    seen ={}
    for index,char in enumerate(s):
        if char in seen:
            return char
        else:
            seen[char] = index
    return -1

     

if __name__=='__main__':
    print("Enter the string:")

    string = input()
    result = repeatedCharacter(string)

    if result == -1 :
        print(f"There is no letter that appear twice in a given string '{string}'")
    else:
        print(f"The letter '{result}' is the first letter to appear twice in string {string}")
