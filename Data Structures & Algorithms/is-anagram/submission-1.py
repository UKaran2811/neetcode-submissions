class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else: return False
        #return Counter(s) == Counter(t)