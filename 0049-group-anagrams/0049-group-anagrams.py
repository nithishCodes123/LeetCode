class Solution:
    def groupAnagrams(self, strs) :
        from collections import defaultdict
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())