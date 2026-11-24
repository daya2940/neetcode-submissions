class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency={}
        for k in s:
            if k in frequency:
                frequency[k]=frequency[k]+1
            else:
                frequency[k]=1
        for m in t:
            if m in frequency:
                frequency[m]=frequency[m]-1
            else:
                return False
        if set(frequency.values()) == {0}:
            return True
        else:
            return False
