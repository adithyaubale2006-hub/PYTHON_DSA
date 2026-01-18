#My SOL (50% ai)
def longestPalindrome(s):
        h1 = {}

        for i in s:
            h1[i] = 1+h1.get(i, 0)

        length = 0
        has_odd = False

        for c in h1.values():
            if c%2 == 0:
                length += c
            else:
                length += c-1
                has_odd= True
        
        if has_odd:
            length+=1

        return length

s = "abccccdd"
print(longestPalindrome(s))

#Best Sol in LC
def longestPalindrome(s):
        d = {}
        r = 0
        for c in s:
            d[c] = d.get(c, 0) + 1
        for v in d.values():
            r += v if v % 2 == 0 else v - 1
        return r + 1 if r < len(s) else r