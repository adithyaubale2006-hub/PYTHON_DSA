#Leetcode 771

def j_s(jewels, stones):
    s = set(jewels)
    count = 0

    for stone in stones:
        if stone in s:
            count+=1

    return count

jewels= "aA"
stones = "aAAbbbb"
print(j_s(jewels, stones))