class Solution:
    def countAndSay(self, n: int) -> str:
        output = "1"
        i = 1
        while i < n:
            j = 0
            temp = ""
            while j < len(output):
                k = 0
                while j + k < len(output) and output[j] == output[j + k]:
                    k += 1
                temp += str(k) + output[j]
                j += k
            i += 1
            output = temp
        return output
