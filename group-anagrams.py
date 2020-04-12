class Solution:
    '''
    >>> strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    >>> solution = Solution()
    >>> solution.groupAnagrams(strs)
    [["ate","eat","tea"], ["nat","tan"],["bat"]]
    '''
    def groupAnagrams(self, strs):
        anagram_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(list(word)))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        return list(anagram_dict.values())

import doctest
if doctest.testmod(verbose=True).failed == 0:
    print('all tests passed')