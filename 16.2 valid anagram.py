class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps={}
        mapt={}
        for i in s:
            maps[i]=maps.get(i,0)+1
        for j in t:
            mapt[j]=mapt.get(j,0)+1
        return maps == mapt
        
