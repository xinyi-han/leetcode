class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashMap = {char: 0 for char in "balloon"}
        for char in text:
            if char in hashMap:
                hashMap[char] += 1
        nums = [v//2 if k in "lo" else v for k, v in hashMap.items()]
        return min(nums)
