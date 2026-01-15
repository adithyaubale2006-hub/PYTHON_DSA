def checkPrimeFrequency(nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        for count in freq.values():
            if isPrime(count):
                return True

        return False

nums = [1,2,3,4,3,5]
print(checkPrimeFrequency(nums))
