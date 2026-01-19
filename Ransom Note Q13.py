#leetcode 383
def canConstruct(ransomNote, magazine):
        c = {}
        for i in magazine:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1

        for i in ransomNote:
            if i not in c:
                return False
            elif c[i] == 1:
                del c[i]
            else:
                c[i] -= 1
        return True

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))