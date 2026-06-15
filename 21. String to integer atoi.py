class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] in ['-','+']:
            if s[0]=='-':
                sign = -1
            s = s[1:]
        res = 0
        for char in s:
            if char.isdigit():
                res= res*10+int(char)
            else:
                break
        res = res*sign
        if res<INT_MIN:
            return INT_MIN
        elif res>INT_MAX :
            return INT_MAX 
        else:
            return res
