class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_sub = len(s1)
        if len_sub > len(s2) :
            return False
        c = Counter(s1)
        for i in range(0, len(s2) - len_sub + 1) : 
            sub = s2[i:i+len_sub]
            c_c = Counter(sub)
            print(sub)
            if c == c_c :
                return True
        return False