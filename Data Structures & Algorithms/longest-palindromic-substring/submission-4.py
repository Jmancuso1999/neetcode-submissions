class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) time and O(1) Space
        maxSubstring = s[0]
        for i in range(len(s)):
            left, right = i, i
            # Odd Palidrome (left and right would start onthe same)
            oddPalidrome = self.largestPalidrome(s, left, right)
            if len(oddPalidrome) >= len(maxSubstring):
                maxSubstring = oddPalidrome
            
            # Even Palidrome (left and right start NEXT to each other)
            left, right = i, i + 1
            evenPalidrome = self.largestPalidrome(s, left, right)
            if len(evenPalidrome) >= len(maxSubstring):
                maxSubstring = evenPalidrome

        return maxSubstring

    def largestPalidrome(self, word, left, right):
        if left < 0 or right >= len(word) or word[left] != word[right]:
            return word[0]
        
        currLeft = left
        currRight = right

        while left >= 0 and right < len(word) and word[left] == word[right]:
            currLeft = left
            currRight = right
            left -= 1
            right += 1
        
        return word[currLeft: currRight + 1]