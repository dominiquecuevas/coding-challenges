'''
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
Example 4:

Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
Example 5:

Input: s = "friend", t = "family"
Output: 4
'''

# dictionary of char counts of s string
# steps variable to keep track of differences
# loop through t
# if t character in dictionary, decrement value
    # after decrementing, if value reaches 0, delete from dictionary
# if t character not in dictionary, increment steps
# return steps

class Solution:
    '''
    >>> solution = Solution()
    >>> s = "bab"
    >>> t = "aba"
    >>> solution.minSteps(s, t)
    1
    >>> s = "leetcode"
    >>> t = "practice"
    >>> solution.minSteps(s, t)
    5
    '''
    def minSteps(self, s, t):
        char_counts = {}
        steps = 0
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        for char in t:
            if char not in char_counts:
                steps += 1
            elif char_counts[char] > 0:
                char_counts[char] = char_counts[char] - 1
                if char_counts[char] == 0:
                    del char_counts[char]
        return steps

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')        