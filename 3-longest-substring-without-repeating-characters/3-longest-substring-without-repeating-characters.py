class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j, ml = 0, 0, 0
        d = {}
        for j in range(len(s)):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            if len(d) == j -i + 1:
                ml = max(ml, j -i + 1)
                j += 1
            elif len(d) < j - i + 1:
                while len(d) < j - i + 1:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        d.pop(s[i])
                    i += 1
                j += 1
        return ml
        