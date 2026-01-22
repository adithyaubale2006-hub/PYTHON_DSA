def percentageLetter(s, letter):
        frq= {}

        for i in s:
            frq[i] = 1+frq.get(i, 0)

        for i, v in frq.items():
            if letter == i:
                return  int(v/(len(s)) * 100)
        
        return 0

s = "foober"
letter = "o"
print(percentageLetter(s, letter))