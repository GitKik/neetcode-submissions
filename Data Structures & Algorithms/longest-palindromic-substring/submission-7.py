class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.is_palindrome(s):
            return s
        for split_size in range(0,len(s)+1) :
            substrings = [s[i:i+1+(len(s) - split_size)] for i in range(0,split_size)]
            print(substrings)
            for substr in substrings :
                if self.is_palindrome(substr):
                    return substr
    
    def is_palindrome(self, s:str) -> bool :
        if s == s[::-1]: 
            return True
        return False 