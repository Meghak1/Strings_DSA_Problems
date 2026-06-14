from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        res = sorted(freq.items(),key = lambda x: x[1], reverse = True)
        return "".join([i*j for i,j in res])
