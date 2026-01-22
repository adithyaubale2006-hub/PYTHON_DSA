words = ["i","love","leetcode","i","love","coding"]
k = 2
freq = {}
count = [[] for i in range(len(words)+1)]

for i in words:
    freq[i] = 1 + freq.get(i, 0)

for i, v in freq.items():
    count[v].append(i)
  
res = []
for i in range(len(count)-1, 0, -1):
    if count[i]:
        for words in count[i]:
            res.append(words)
            if len(res) == k:
                print(res)
                break