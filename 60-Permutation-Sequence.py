class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        prod = 1
        for num in range(1, n):
            prod *= num
        output = ""
        while len(output) < n - 1:
            div = k // prod
            mod = k % prod
            if mod == 0:
                div -= 1
            output += str(nums[div])
            nums.pop(div)
            k -= div * prod
            prod = prod // len(nums)
        output += str(nums[0])
        return output
