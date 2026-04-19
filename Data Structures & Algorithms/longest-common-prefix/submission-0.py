class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] 

        # Find smallest word
        for word in strs:
            if len(word) < len(prefix):
                prefix = word

        for currWord in range(1, len(strs)):
            startPos = 0
            while startPos < len(prefix):
                if prefix[startPos] != strs[currWord][startPos]:
                    break # End's while loop
                startPos += 1

            # Updates for every word we visit and resets it with next
            # smallest prefix (if there)
            prefix = prefix[:startPos] 
        
        return prefix

"""


"""