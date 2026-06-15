from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            freq=Counter()
            for j in range(i, len(s)):
                freq[s[j]]+=1
                maxf = max(freq.values())
                minf = min(freq.values())
                if len(freq)>1:
                    total += maxf-minf
        return total
