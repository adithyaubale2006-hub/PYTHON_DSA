class Solution:
    def frequencySort(nums):
        h1 = {}
        res = [[] for i in range(len(nums)+1)]
        for i in nums:
            h1[i] = 1+h1.get(i, 0)

        for i, v in h1.items():
            res[v].append(i)

        #LEarn this imp
        ans = []
        for f in range(1, len(res)):
            for num in sorted(res[f], reverse= True):
                ans.extend([num] * f)

        return ans

    nums = [1,1,1,2,2,3]
    print(frequencySort(nums))