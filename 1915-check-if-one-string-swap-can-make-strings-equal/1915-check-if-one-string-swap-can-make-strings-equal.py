class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        check_diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                check_diff.append(i)

        if len(check_diff) != 2:
            return False
        
        i,j = check_diff
        return s1[i] == s2[j] and s1[j] == s2[i]