class Solution:
    def countVowelPermutation(self, n: int) -> int:
        cache = [1 for _ in range(5)] # a e i o u
        for i in range(1, n):
            temp = [0 for _ in range(5)]
            temp[0] = cache[1] + cache[2] + cache[4]
            temp[1] = cache[0] + cache[2]
            temp[2] = cache[1] + cache[3]
            temp[3] = cache[2]
            temp[4] = cache[2] + cache[3]
            cache = temp
        return sum(cache) % (10**9 + 7)
