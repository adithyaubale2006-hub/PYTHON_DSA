n = "anagram"
s = "nagaram"

# Step 1: length check
if len(n) != len(s):
    print("False")
else:
    count = {}

    # Step 2: count characters in n
    for ch in n:
        count[ch] = count.get(ch, 0) + 1

    # Step 3: subtract characters using s
    for ch in s:
        if ch not in count:
            print("False")
            break
        count[ch] -= 1
    else:
        # Step 4: final check
        for val in count.values():
            if val != 0:
                print("False")
                break
        else:
            print("True")
