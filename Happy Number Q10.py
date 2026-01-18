#Better Solution
class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        while True:
            if n == 1:
                return True

            if n in hashset:
                return False

            hashset.add(n)
            n = self.addSquares(n)

    def addSquares(self, n: int) -> int:
        count = 0

        while n > 0:
            digit = n % 10
            count += digit * digit
            n //= 10

        return count

#My solution
class Solution:
    def isHappy(n):
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            total = 0
            while n > 0:
                digit = n%10
                total+=digit*digit
                n //= 10
            n = total

        return True
    
    n = 19
    print(isHappy(n))